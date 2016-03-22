from PyQt4 import QtCore, QtGui
import sys

class Brick(QtGui.QGraphicsItem):
	def __init__(self, parent = None):
		super(Brick, self).__init__(parent)
		self.x = 0
		self.y = 0
		self.width = 0
		self.height = 0
		self.forwardX = 0
		self.forwardY = 0
		self.rect = QtGui.QRecF(self.x, self.y, self.width, self.height)
		self.setPos(x,y)
	
	@property
	def brickType(self):
	    return self._brickType
	@brickType.setter
	def brickType(self, value):
	    self._brickType = value

	def setForward(self, forwardX , forwardY): 
		self.forwardX = forwardX
		self.forwardY = forwardY

	def getRect(self):
		return (self.x, self.y, self.width, self.height)

	def setRect(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.rect = QtGui.QRecF(self.x, self.y, self.width, self.height)

	def boundingRect(self):
		return self.rect

	dx = 20
	dy = 20
	def nextPos(self):
		self.x = self.x + self.dx * self.forwardX
		self.y = self.y + self.dy * self.forwardY
		self.setPos(self.x, self.y)

class UserBrick(Brick):
	def __init__(self, *arg):
		super(userBrick, self).__init__()

	def keyNextPos(self, keyEvent):
		if keyEvent.key() == QtCore.Qt.Key_Left:
			self.x = self.x - self.dx
		elif keyEvent.key() == QtCore.Qt.Key_Right:
			self.x = self.x + self.dx
		elif event.key() == QtCore.Qt.Key_Up:
			self.y = self.y - self.dy
		elif event.key() == QtCore.Qt.Key_Down:
			self.y = self.y + self.dy
		self.setPos(self.x, self.y)


class BricksScene(QtGui.QGraphicsScene):
	def __init__(self, parent = None):
		super(BricksScene, self).__init__()

	height = 300
	width = 400

	def event(self, event):
		items = self.items()
		for itemA in items:
			# border event
			border = hitBorder(itemA)
			if border != 0:
				handleBorder(itemA, border)
			# collision event
			for itemB in items:
				if itemA == itemB:
					continue
				if itemA.collidesWithPath(itemB.shape() ):
					handleCollision(itemA, itemB)
		return super(MainWindow, self).event(event)



# brick type: black:user red:rebound, yellow:attach, blue:through
def handleCollision(posBrick, negBrick):  # distribute collision event to handler for each type, set forward for posBrick
	if posBrick.brickType == 0: #user
		QtCore.QObject.emit(QtCore.SIGNAL('gameOver()'))
	elif posBrick.brickType == 1: #rebound
		reboundCollision(posBrick, negBrick)
	elif posBrick.brickType == 2: #attach
		attachCollision(posBrick, negBrick)
	elif posBrick.brickType == 3: #through
		throughCollision(posBrick, negBrick)

def reboundCollision(posBrick, negBrick): 
	pass

def attachCollision(posBrick, negBrick): 
	posBrick.setForward(negBrick.forwardX, negBrick.forwardY)

def throughCollision(posBrick, negBrick):
	pass

def hitBorder(brick):
	if brick.x <= 0:
		return 1 #left
	elif brick.x + brick.width >= BricksScene.width:
		return 2 #right
	elif brick.y <= 0:
		return 3 #up
	elif brick.y + brick.height < BricksScene.height:
		return 4 #down
	else:
		return 0 

def handleBorder(brick, border):
	if brick.brickType == 0: #user
		QtCore.QObject.emit(QtCore.SIGNAL('gameOver()'))
	elif brick.brickType == 1: #rebound
		reboundBorder(brick, border)
	elif brick.brickType == 2: #attach
		attachBorder(brick, border)
	elif brick.brickType == 3: #through
		throughCollision(brick, border)

def reboundBorder(brick, border):
	if border == 1 or border == 2:
		brick.setForward(- brick.forwardX, brick.forwardY)
	if border == 3 or border == 4:
		brick.setForward(brick.forwardX,- brick.forwardY)

def attachBorder(brick, border):
	reboundBorder(brick, border)

def throughBorder(brick, border):
	if border == 1:
		brick.x = BricksScene.width
	elif border == 2:
		brick.x = 0
	elif border == 3:
		brick.y = BricksScene.height
	elif border == 4:
		brick.y = 0
	

	



