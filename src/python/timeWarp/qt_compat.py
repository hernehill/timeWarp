""" QT File to set the correct type to allow for Maya 2026+"""
try:
    from PySide6 import QtCore, QtGui, QtWidgets
    from PySide6.QtGui import QAction
    from shiboken6 import wrapInstance

except ImportError:
    from PySide2 import QtCore, QtGui, QtWidgets
    from PySide2.QtWidgets import QAction
    from shiboken2 import wrapInstance