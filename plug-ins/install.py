"""Install setup for TimeWarp"""

import os
import glob

import maya.mel


MOD_INPUT_TEXT = "+ timeWarp 1.0 ABAB/timeWarp\n"\
                 "scripts: ./scripts"

TIMEWARP_MOD = "timeWarp.mod"


def get_script_path():
    """ Get Maya's scripts path at root level.

    Returns:
        str to path of modules.
    """

    return os.path.abspath(os.path.join(maya.mel.eval("internalVar -upd"), "../../scripts"))


def get_module_path():
    """ Get Maya's modules path at root level.

    Returns:
        str to path of modules.
    """

    return os.path.abspath(os.path.join(maya.mel.eval("internalVar -upd"), "../../modules"))


def installed_mod_path():
    """ Get installed module path if found.

    Returns:
        str of path to timeWarp.mod
    """
    for path in os.getenv("MAYA_MODULE_PATH").split(":"):
        if glob.glob(os.path.join(path, TIMEWARP_MOD)):
            return path


def build_mod_file(module_path, scripts_path):

    mod_text = MOD_INPUT_TEXT.replace("ABAB", scripts_path)

    # Check if "maya/modules" folder already exists
    module_file_path = os.path.join(module_path, TIMEWARP_MOD)
    if not os.path.isdir(module_path):
        try:
            os.mkdir(module_path)
        # In the case we can't make the folder we need to fail out.
        except:
            return False

    if os.path.isfile(module_file_path) and TIMEWARP_MOD in module_file_path:
        try:
            os.remove(module_file_path)
        # Make sure we can delete the file else we need to fail out.
        except:
            return False

    # Now we can write out the file.
    with open(module_file_path, "w") as fileInstance:
        fileInstance.write(mod_text)

    return True
