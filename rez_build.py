"""Install for REZ"""

# Standard
import sys

print("Appending rez_build_api.py to sys.path")
bUseSymlinks = True
if sys.platform.startswith("win"):
    sys.path.append("T:/rez_pipe/hh_rez_pckSetup")
    bUseSymlinks = False
else:
    sys.path.append("/mnt/tools/rez_pipe/hh_rez_pckSetup")
import rez_build_api


# List of directories and files to be copied or symlinked (if building locally)
DIRECTORY_LIST = ["src"]
FILE_LIST = []


if __name__ == "__main__":

    rez_build_api.build(
        DIRECTORY_LIST,
        FILE_LIST,
        create_version_symlinks=bUseSymlinks,
        has_otls=False
    )
