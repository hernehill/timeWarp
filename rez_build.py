"""Install for REZ"""

# Standard
import sys

print("Appending rez_build_api.py to sys.path")
sys.path.append("/mnt/tools/rez_pipe/hh_rez_pckSetup")
import rez_build_api


# -----------------------------------------------
# The lists below will be 'copied' or 'symlinked' to destination.
# If building locally, user has the option to build with symlink.
# If releasing, symlink is not allowed.
DIRECTORY_LIST = ["src"]  # destination will preserve full sub-paths
LEAF_DIRS = []  # only the leaf subdir will be copied/symlinked
FILE_LIST = []


if __name__ == "__main__":

    rez_build_api.build(
        DIRECTORY_LIST,
        FILE_LIST,
        has_otls=False,
        leafs=LEAF_DIRS
    )
