from PyQt4 import QtCore, QtGui
import sys

from view import *
from mainWindow import *
from scene import *

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv);
	mainWindow = MainWindow()
	mainWindow.show()
	sys.exit(app.exec_())

	