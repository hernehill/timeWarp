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
        main_layout.addWidget(self.create_warp_btn)

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


def launch():
    """ Launch UI """

    global _WIDGET  # pylint: disable=global-statement

    if _WIDGET:
        _WIDGET.close()
        _WIDGET = None

    _WIDGET = TimeWarp()

    _WIDGET.show()


