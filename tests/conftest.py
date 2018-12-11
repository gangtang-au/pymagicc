# import os
# from os.path import exists


# import pytest


# from pymagicc import MAGICC6, MAGICC7


# def pytest_addoption(parser):
#     parser.addoption(
#         "--skip-slow", action="store_true", default=False, help="skip any slow tests"
#     )


# def pytest_collection_modifyitems(config, items):
#     if config.getoption("--skip-slow"):
#         # --skip-slow given in cli: skipping slow tests
#         skip_slow = pytest.mark.skip(reason="--skip-slow option was provided")
#         for item in items:
#             if "slow" in item.keywords:
#                 item.add_marker(skip_slow)


# @pytest.fixture(scope="function", params=[MAGICC6, MAGICC7])
# def package(request):
#     MAGICC_cls = request.param
#     p = MAGICC_cls()

#     if p.executable is None or not exists(p.original_dir):
#         magicc_x_unavailable = "MAGICC {} is not available.".format(p.version)
#         env_text = "Pymagicc related variables in your current environment are: {}.".format(
#             ";".join(
#                 [
#                     "{}: {}".format(k, v)
#                     for (k, v) in os.environ.items()
#                     if k.startswith("MAGICC_")
#                 ]
#             )
#         )
#         env_help = "If you set MAGICC_EXECUTABLE_X=/path/to/MAGICCX/binary then you will be able to run the tests with that binary for MAGICC_X."
#         pytest.skip("\n".join([magicc_x_unavailable, env_text, env_help]))
#     p.create_copy()
#     root_dir = p.root_dir
#     yield p
#     # Perform cleanup after tests are complete
#     p.remove_temp_copy()
#     assert not exists(root_dir)
