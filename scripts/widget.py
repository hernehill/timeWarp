""" Build UI Template"""


# Qt
from PySide2 import QtCore, QtWidgets, QtGui

_WIDGET = None


class TimeWarp(QtWidgets.QDialog):
    """ Template Widget """

    def __init__(self):
        super(TimeWarp, self).__init__()

        # Build UI
        self.setWindowTitle('Time Warp')

        self.setGeometry(300, 300, 500, 600)

        main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(main_layout)


def launch():
    """ Launch UI """

    global _WIDGET  # pylint: disable=global-statement

    if _WIDGET:
        _WIDGET.close()
        _WIDGET = None

    _WIDGET = TimeWarp()

    _WIDGET.show()


