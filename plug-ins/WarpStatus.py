""" Warp Status Node"""

import maya.OpenMaya as om
import maya.OpenMayaMPx as ompx

from . import __version__, __doc__, __author__, __email__, __copyright__


class WarpStatus(ompx.MPxNode):

    TYPE_NAME = "WarpStatus"
    TYPE_ID = om.MTypeId(0x00000123)

    # Input attributes
    active_input = None
    warp = None
    time = None

    # Output attribute
    outputAttr = None

    def __init__(self, name=None):
        super(WarpStatus, self).__init__()

        self.nodeName = name or self.TYPE_NAME

    def compute(self, plug, data_block):
        """ Compute method to calculate the output value

        Args:
            plug (MPlug): Plug to compute.
            data_block: Data block to evaluate

        Returns:
            None
        """
        if plug == WarpStatus.outputAttr:

            # Get input values
            active_input = data_block.inputValue(WarpStatus.warpActiveAttr).asBool()
            warp = data_block.inputValue(WarpStatus.warpInputAttr).asFloat()
            time = data_block.inputValue(WarpStatus.timeInputAttr).asFloat()

            # Calculate the output value based on the active input
            if active_input:
                output = warp
            else:
                output = time

            # Set the output value
            output_handle = data_block.outputValue(WarpStatus.outputAttr)
            output_handle.setFloat(output)
            data_block.setClean(plug)

    @staticmethod
    def creator():
        """Creator function

        Returns:
            instance of the node
        """
        return ompx.asMPxPtr(WarpStatus())

    @staticmethod
    def initialize():
        """ Initializes attribute information

        Returns:
            None
        """
        attr = om.MFnNumericAttribute()

        # Create active input attribute
        WarpStatus.warpActiveAttr = attr.create("warpActive", "act", om.MFnNumericData.kBoolean, True)
        attr.setWritable(True)
        attr.setStorable(True)
        attr.setKeyable(True)
        WarpStatus.addAttribute(WarpStatus.warpActiveAttr)

        # Create warp attribute
        WarpStatus.warpInputAttr = attr.create("warpInput", "wi", om.MFnNumericData.kFloat, 0.0)
        attr.setWritable(True)
        attr.setStorable(True)
        attr.setKeyable(True)
        WarpStatus.addAttribute(WarpStatus.warpInputAttr)

        # Create time attribute
        WarpStatus.timeInputAttr = attr.create("timeInput", "ti", om.MFnNumericData.kFloat, 0.0)
        attr.setWritable(True)
        attr.setStorable(True)
        attr.setKeyable(True)
        WarpStatus.addAttribute(WarpStatus.timeInputAttr)

        # Create output attribute
        WarpStatus.outputAttr = attr.create("output", "out", om.MFnNumericData.kFloat, 0.0)
        attr.setWritable(False)
        attr.setStorable(False)
        attr.setReadable(True)
        WarpStatus.addAttribute(WarpStatus.outputAttr)

        # Attribute affects
        WarpStatus.attributeAffects(WarpStatus.warpActiveAttr, WarpStatus.outputAttr)
        WarpStatus.attributeAffects(WarpStatus.warpInputAttr, WarpStatus.outputAttr)
        WarpStatus.attributeAffects(WarpStatus.timeInputAttr, WarpStatus.outputAttr)


def initializePlugin(plugin):
    """ Initialize the plugin when Maya loads it.

    Args:
        plugin: Plugin to load.

    Returns:
        None
    """

    vendor = __author__
    version = __version__
    api_version = "Any"

    plugin_fn = ompx.MFnPlugin(plugin, vendor, version, api_version)
    try:
        plugin_fn.registerNode(WarpStatus.TYPE_NAME,
                               WarpStatus.TYPE_ID,
                               WarpStatus.creator,
                               WarpStatus.initialize)
    except:
        om.MGlobal.displayError("Failed to register node: {0}".format(WarpStatus.TYPE_NAME))


def uninitializePlugin(plugin):
    """ Un-initialize the plugin when Maya unloads it

    Args:
        plugin: Plugin to unload.

    Returns:
        Nome
    """
    plugin_fn = om.MFnPlugin(plugin)

    try:
        plugin_fn.deregisterNode(WarpStatus.TYPE_ID)
    except:
        om.MGlobal.displayError("Failed to unregister node: {0}".format(WarpStatus.TYPE_NAME))