from PyQt4 import QtCore, QtGui
import sys

import scene

class  BricksView(QtGui.QGraphicsView):
	def __init__(self, parent = None):
		super( BricksView, self).__init__(parent)

	def keyEvent(self, event):
		self.emit(QtCore.SIGNAL('KeyRelease(event)'))
		
