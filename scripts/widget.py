""" Build UI Template"""

# Python
import os

# Qt
from PySide2 import QtCore, QtWidgets, QtGui

from timeWarp.scripts import core
ICON_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../', 'icons')

_WIDGET = None


class TimeWarp(QtWidgets.QDialog):
    """ Template Widget """

    def __init__(self):
        super(TimeWarp, self).__init__()

        # Build UI
        self.setWindowTitle('Time Warp')
        self.setWindowIcon(QtGui.QIcon(os.path.join(ICON_PATH, 'WarpStatus.png')))

        self.setGeometry(300, 300, 500, 600)

        main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(main_layout)

        self.create_warp_btn = QtWidgets.QPushButton("Create Warp Node")
        self.create_warp_btn.clicked.connect(self.create_warp)
        main_layout.addWidget(self.create_warp_btn)

        self.warp_select = QtWidgets.QComboBox()
        self.warp_select.currentTextChanged.connect(self.on_select_change)
        main_layout.addWidget(self.create_warp_btn)

        self.active = QtWidgets.QCheckBox("Warp Active")
        self.active.toggled.connect(self.set_active_status)
        main_layout.addWidget(self.active)

        # add scene data to widgets.
        self.add_scene_data()

    def add_scene_data(self):
        """ Run this after building of GUI to set the widget based on scene.

        Returns:
            None
        """

        self.warp_select.blockSignals(True)
        self.active.blockSignals(True)

        # Add Scene warps to widget.
        self.warp_select.addItems(core.get_warp_nodes())

        # set warp status of current warp.
        current_warp = self.warp_select.currentText()

        if current_warp:
            status = core.is_warp_active(current_warp)
            self.active.setChecked(status)

        self.warp_select.blockSignals(False)
        self.active.blockSignals(False)

    def create_warp(self):
        """ Create warp and add to select.

        Returns:
            None
        """

        warp_name, create = QtWidgets.QInputDialog.getText(self, "Time Warp", "Warp Name:",
                                                           QtWidgets.QLineEdit.Normal, "atk_warpSettings")

        if warp_name and create:
            name = core.create_warp(warp_name=warp_name)
            self.warp_select.addItem(name)
            self.warp_select.setCurrentText(name)

    def set_active_status(self, status):
        """ Change active status of warp.

        Args:
            status (bool): Current state of checkbox.

        Returns:
            None
        """

        current_warp = self.warp_select.currentText()
        core.set_warp_status(current_warp, status)

    def on_select_change(self, current_warp):
        """ On change of warp select.

        Args:
            current_warp (str): Name of Current warp.

        Returns:
            None
        """

        status = core.is_warp_active(current_warp)
        self.active.setChecked(status)


def launch():
    """ Launch UI """

    global _WIDGET  # pylint: disable=global-statement

    if _WIDGET:
        _WIDGET.close()
        _WIDGET = None

    _WIDGET = TimeWarp()

    _WIDGET.show()


