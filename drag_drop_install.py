""" Drag and drop install information."""
# Python
from PySide2 import QtWidgets
import sys
from shiboken2 import wrapInstance
# Set for Python 3
if sys.version_info > (3,):
    long = int


# Maya
import maya.OpenMayaUI as omui

# Custom
from scripts import install


class WarpInstall(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(WarpInstall, self).__init__(parent)

        self.parent = parent

        self.setWindowTitle("timeWarp Install")
        self.setMinimumWidth(600)

        main_layout = QtWidgets.QVBoxLayout(self)
        module_layout = QtWidgets.QHBoxLayout(self)
        main_layout.addLayout(module_layout)
        
        self.module_label = QtWidgets.QLabel("Module Path")
        module_layout.addWidget(self.module_label, 6)

        mod_path = install.get_module_path()
        self.module_path = QtWidgets.QLineEdit(mod_path)
        module_layout.addWidget(self.module_path, 30)
        
        self.module_browse = QtWidgets.QPushButton(parent=self, text="...")
        self.module_browse.setMinimumWidth(30)
        self.module_browse.pressed.connect(self.browse_modules_path)
        module_layout.addWidget(self.module_browse, 1)

        self.install_button = QtWidgets.QPushButton(parent=self, text="Install timeWarp")
        self.install_button.clicked.connect(lambda: install.install(self.module_path.text()))
        main_layout.addWidget(self.install_button)

    def browse_modules_path(self):
        """ Open browser to set new module paths.

        Returns:
            None
        """
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                               "Set Modules Directory",
                                                               self.modulePathTxt.text())
        self.sender().setDown(False)  # unstuck the button
        if not directory:
            return
        self.modulePathTxt.setText(directory)

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

