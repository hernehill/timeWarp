""" Drag and drop install information."""
# Python
from PySide2 import QtWidgets, QtGui, QtCore
import os
import sys
from shiboken2 import wrapInstance
# Set for Python 3
if sys.version_info > (3,):
    long = int


# Maya
import maya.OpenMayaUI as omui

# Custom
from scripts import install

ICON_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons')


class WarpInstall(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(WarpInstall, self).__init__(parent)

        self.parent = parent

        self.setWindowTitle("Time Warp Install")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QtGui.QIcon(os.path.join(ICON_PATH, 'WarpStatus.png')))
        self.setMinimumWidth(600)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setAlignment(QtCore.Qt.AlignTop)

        # Menu Bar.
        self.menu_bar = QtWidgets.QMenuBar()
        self.help_menu = self.menu_bar.addMenu("Help")
        main_layout.setMenuBar(self.menu_bar)

        help_action = QtWidgets.QAction("Docs", self)
        help_action.triggered.connect(lambda: QtGui.QDesktopServices.openUrl(
            QtCore.QUrl("http://www.adambakerart.com")))
        self.help_menu.addAction(help_action)

        version = QtWidgets.QAction("Version: 1.0", self)
        version.setEnabled(False)
        self.help_menu.addAction(version)

        script_layout = QtWidgets.QHBoxLayout(self)
        main_layout.addLayout(script_layout)

        self.scripts_label = QtWidgets.QLabel("Scripts Path  ")
        self.scripts_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        script_layout.addWidget(self.scripts_label, 6)

        script_path = install.get_script_path()
        self.script_path = QtWidgets.QLineEdit(script_path)
        script_layout.addWidget(self.script_path, 30)

        self.script_browse = QtWidgets.QPushButton(parent=self, text="...")
        self.script_browse.setMinimumWidth(30)
        self.script_browse.pressed.connect(self.browse_script_path)
        script_layout.addWidget(self.script_browse, 1)

        module_layout = QtWidgets.QHBoxLayout(self)
        main_layout.addLayout(module_layout)
        
        self.module_label = QtWidgets.QLabel("Module Path")
        self.module_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        module_layout.addWidget(self.module_label, 6)

        mod_path = install.get_module_path()
        self.module_path = QtWidgets.QLineEdit(mod_path)
        module_layout.addWidget(self.module_path, 30)
        
        self.module_browse = QtWidgets.QPushButton(parent=self, text="...")
        self.module_browse.setMinimumWidth(30)
        self.module_browse.pressed.connect(self.browse_modules_path)
        module_layout.addWidget(self.module_browse, 1)

        self.install_button = QtWidgets.QPushButton(parent=self, text="Install Time Warp")
        self.install_button.setStyleSheet("background-color : #16A085")
        self.install_button.clicked.connect(lambda: install.install(self.module_path.text()))
        main_layout.addWidget(self.install_button)

    def browse_modules_path(self):
        """ Open browser to set new module paths.

        Returns:
            None
        """
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                               "Set Modules Directory",
                                                               self.module_path.text())
        self.sender().setDown(False)  # unstuck the button
        if not directory:
            return
        self.module_path.setText(directory)

    def browse_script_path(self):
        """ Open browser to set new script paths.

        Returns:
            None
        """
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                               "Set Scripts Directory",
                                                               self.script_path.text())
        self.sender().setDown(False)  # unstuck the button
        if not directory:
            return
        self.script_path.setText(directory)

    def closeEvent(self, event):
        """ Close event.

        Args:
            event (QEvent): Event of close.

        Returns:
            None
        """
        self.close()


def mayaMainWindow():
    """ Get Maya Main widow.

    Returns:
        wrapped instance of maya main window.
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


def onMayaDroppedPythonFile(*args, **kwargs):
    """ Main function that runs when file is dragged into Maya.

    Args:
        *args (args): Arguments to pass onto command.
        **kwargs (kwargs): Keyable arguments to pass onto command.

    Returns:
        None
    """
    print('install')
    installer = WarpInstall(mayaMainWindow())
    installer.show()

