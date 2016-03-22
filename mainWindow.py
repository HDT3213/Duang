from PyQt4 import QtCore, QtGui
import sys

from scene import *
from view import *

class MainWindow(QtGui.QMainWindow):
	def __init__(self, *args, **kwargs):
		QtGui.QMainWindow.__init__(self, *args, **kwargs)
		self.scene = BricksScene(self)
		self.view = BricksView(self)
		self.view.setRenderHint(QtGui.QPainter.Antialiasing)
		self.view.setScene(self.scene)
		self.view.setFocusPolicy(QtCore.Qt.NoFocus)

	# def populate(self):
	# 	n = 4
	# 	self.bricks = list()
	# 	for i in range(n):
	# 		self.bricks.append(Brick(self))

	def populate(self):
		brick1 = Brick()
		self.scene.addItem(brick1)
		brick2 = Brick()
		self.scene.addItem(brick2)
		brick3 = Brick()
		self.scene.addItem(brick3)
		brick4 = Brick()
		self.scene.addItem(brick4)
		self.userBrick = UserBrick()
		self.scene.show()

	interval =  40
	def startGame(self):
		self.startTimer(interval)

	def timerEvent(self, event):
		pass



				