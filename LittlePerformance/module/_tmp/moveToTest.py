import time
import sys
from naoqi import ALProxy

args = sys.argv
IP = args[1]
PORT = int(args[2])

motion = ALProxy('ALMotion',IP,PORT)
motion.positionErrorThresholdPos = 0.0
motion.positionErrorThresholdAng = 0.0


def MoveTo(distX, distY, rotate):
	print "Move To:"
	print distX
	print distY
	print rotate

	import almath
	initPosition = almath.Pose2D(motion.getRobotPosition(True))
	targetDistance = almath.Pose2D(distX, distY, rotate * almath.PI / 180)
	expectedEndPosition = initPosition * targetDistance
	enableArms = False
	motion.setMoveArmsEnabled(enableArms, enableArms)
	motion.moveTo(distX, distY, rotate * almath.PI / 180)

	# The move is finished so output
	# realEndPosition = almath.Pose2D(motion.motion.getRobotPosition(False))
	# positionError = realEndPosition.diff(expectedEndPosition)
	# positionError.theta = almath.modulo2PI(positionError.theta)
	# if (abs(positionError.x) < motion.positionErrorThresholdPos
	#     and abs(positionError.y) < motion.positionErrorThresholdPos
	#     and abs(positionError.theta) < motion.positionErrorThresholdAng):
	#     self.onArrivedAtDestination()
	# else:
	#     self.onStoppedBeforeArriving(positionError.toVector())



MoveTo(0.0, 0.0, 180.0)
MoveTo(0.0, 0.0, -180.0)


