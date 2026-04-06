import maya.cmds as cmds


def check():
    """Check if the timeWarper plugin is loaded, and attempt to load it if not.

    Returns:
        True if the plugin is loaded, False otherwise.
    """
    plugin_name = "WarpStatus"

    if cmds.pluginInfo(plugin_name, query=True, loaded=True):
        return True

    try:
        cmds.loadPlugin(plugin_name)
        return True
    except RuntimeError:
        return False
