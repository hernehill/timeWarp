""" QT File to set the correct type to allow for Maya 2026+"""
try:
    from PySide2 import QtCore, QtGui, QtWidgets, QtOpenGL
    from PySide2.QtWidgets import QAction
    import shiboken2 as shiboken

except ImportError:
    from PySide6 import QtCore, QtGui, QtWidgets, QtOpenGL
    import shiboken6 as shiboken


    if not hasattr(QtCore.Qt, 'MatchRegExp'):
        QtCore.Qt.MatchRegExp = QtCore.Qt.MatchRegularExpression
    if not hasattr(QtGui, 'QRegExpValidator'):
        QtGui.QRegExpValidator = QtGui.QRegularExpressionValidator
    if not hasattr(QtCore, 'QRegExp'):
        QtCore.QRegExp = QtCore.QRegularExpression
    if not hasattr(QtGui.QPalette, 'Background'):
        QtGui.QPalette.Background = QtGui.QPalette.Window
    if not hasattr(QtWidgets, 'QAction'):
        QtWidgets.QAction = QtGui.QAction


qt_version_split = QtCore.qVersion().split(".")

class QtVersion(object):
    major=None
    minor=None
    patch=None

qt_version = QtVersion()
qt_version.major = int(qt_version_split[0])
qt_version.minor = int(qt_version_split[1])
qt_version.patch = int(qt_version_split[2])

# Make sure the old == the new.
if qt_version.major == 6:
    if qt_version.minor >= 7:
        QtWidgets.QCheckBox.stateChanged = QtWidgets.QCheckBox.checkStateChanged