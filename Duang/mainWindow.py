from PyQt4 import QtCore, QtGui
import sys

from scene import *
from view import *

class MainWindow(QtGui.QMainWindow):
	interval =  40
	def __init__(self, *args, **kwargs):
		QtGui.QMainWindow.__init__(self, *args, **kwargs)
		self.scene = QtGui.QGraphicsScene(self)
		self.resize(width + 20, self.scene.height + 20)
		self.view = BricksView(self.scene, self)
		self.view.setRenderHint(QtGui.QPainter.Antialiasing)
		self.view.setScene(self.scene)
		self.view.setFocusPolicy(QtCore.Qt.NoFocus)
		self.view.resize(self.scene.width, self.scene.height)
		self.connect(self.view, QtCore.SIGNAL('keyRelease(event)'),self.userBrick.keyNextPos)
		self.connect(self.scene, QtCore.SIGNAL('gameOver()'),self.endGame)
		self.run = False
		self.createBricks()
		self.resetBricks()
		self.view.show()
		self.startTimer(interval)

	# def populate(self):
	# 	n = 4
	# 	self.bricks = list()
	# 	for i in range(n):
	# 		self.bricks.append(Brick(self))

	def createBricks(self):
		self.bricks = list()
		for i in range(4):
			self.bricks.append(Brick())
			self.scene.addItem(self.bricks[i])
		
		self.userBrick = UserBrick()
		self.scene.addItem(userbrick)
		

	def resetBricks(self):
		self.bricks[0].setRect(20, 20, 20, 20)
		self.bricks[1].setRect(width - 20, 20, 20, 20)
		self.bricks[2].setRect(20, height - 20, 20, 20)
		self.bricks[3].setRect(width - 20, height - 20, 20, 20)
		self.userBrick.setRect(width / 2, height / 2, 20, 20)

	def startGame(self):
		self.resetBricks()
		self.run = True

	def endGame(self):
		self.run = False


	def timerEvent(self, event):
		if not self.run:
			return
		for item in self.scene:
			if not isinstance(item, Brick):
				continue
			item.nextPos()



				