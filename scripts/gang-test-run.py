"""
A test run for Gang's land carbon-nitrogen cycle

Do not use this long-term, make a notebook or something better instead.
"""

from __future__ import annotations

import os
from pathlib import Path

import matplotlib.pyplot as plt
import pymagicc
import scmdata

# Gang to change path if needed
ROOT_DIR_MAGICC_REPO = (Path(__file__).parents[2] / "magicc").absolute()
os.environ["MAGICC_EXECUTABLE_7"] = str(ROOT_DIR_MAGICC_REPO / "bin" / "magicc")


def main() -> None:
    ssp = "ssp126"
    ssp = "ssp245"
    scenario_filename = f"{ssp.upper()}_EMMS.SCEN7"
    scenario = pymagicc.MAGICCData(
        str(ROOT_DIR_MAGICC_REPO / "run" / scenario_filename)
    )
    # scenario["scenario"] = "ssp126"

    # # Generally, don't use this
    # with pymagicc.MAGICC7(root_dir=ROOT_DIR_MAGICC_REPO) as magicc:
    with pymagicc.MAGICC7() as magicc:
        res_l = []
        for cflxnpp0, cplsp0 in zip([40.0, 60.0], [200.0, 400.0]):
            res_run = magicc.run(
                scenario=scenario,
                out_dynamic_vars=[
                    "DAT_SURFACE_TEMP",
                    "DAT_CO2_CONC",
                    "DAT_CO2_LAND_POOL",
                    "DAT_CO2_NETATMOSLANDCO2FLUX",
                ],
                startyear=1850,
                endyear=2105,
                land_cn_parameters=dict(cplsp0=cplsp0, cflxnpp0=cflxnpp0)
                # TOOD: add variable handling
                # TODO: add argument passing
            )
            res_run["cplsp0"] = cplsp0
            res_run["cflxnpp0"] = cflxnpp0

            res_l.append(res_run)
            # breakpoint()

    res = scmdata.run_append(res_l)
    for vrun in res.filter(region="World").groupby("variable"):
        fig, ax = plt.subplots()
        vrun.lineplot(hue="cflxnpp0", style="variable", ax=ax)

    plt.show()


if __name__ == "__main__":
    main()
