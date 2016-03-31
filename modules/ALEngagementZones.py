from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALEngagementZones', '127.0.0.1', PORT)

def proceed(cmd):
	cmd = Cmd(cmd)
	cmd.removeHead()
	print 'going to function:', cmd.getCommand()
	func = globals().get(cmd.getCommand())
	if func:
		return func(cmd.getValues('p'))
	else:
		print 'Error: Cannot find command:' + cmd.getCommand()
		return 'Error: Cannot find command:' + cmd.getCommand()

def computeEngagementZone(params):
	return proxy.computeEngagementZone()

def computeEngagementZone(params):
	if len(params) < 3:
		print 'Error: function \'computeEngagementZone\' takes 2 params'
		return 'Error: function \'computeEngagementZone\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	z = parse(params[2])
	return proxy.computeEngagementZone(x,y,z)

def computeEngagementZone(params):
	if len(params) < 4:
		print 'Error: function \'computeEngagementZone\' takes 2 params'
		return 'Error: function \'computeEngagementZone\' takes 2 params'
	xAngle = parse(params[0])
	yAngle = parse(params[1])
	distance = parse(params[2])
	cameraPositionRobot = parse(params[3])
	return proxy.computeEngagementZone(xAngle,yAngle,distance,cameraPositionRobot)

def getFirstLimitDistance(params):
	return proxy.getFirstLimitDistance()

def getLimitAngle(params):
	return proxy.getLimitAngle()

def getSecondLimitDistance(params):
	return proxy.getSecondLimitDistance()

def setFirstLimitDistance(params):
	if len(params) < 1:
		print 'Error: function \'setFirstLimitDistance\' takes 2 params'
		return 'Error: function \'setFirstLimitDistance\' takes 2 params'
	distance = parse(params[0])
	return proxy.setFirstLimitDistance(distance)

def setLimitAngle(params):
	if len(params) < 1:
		print 'Error: function \'setLimitAngle\' takes 2 params'
		return 'Error: function \'setLimitAngle\' takes 2 params'
	angle = parse(params[0])
	return proxy.setLimitAngle(angle)

def setSecondLimitDistance(params):
	if len(params) < 1:
		print 'Error: function \'setSecondLimitDistance\' takes 2 params'
		return 'Error: function \'setSecondLimitDistance\' takes 2 params'
	distance = parse(params[0])
	return proxy.setSecondLimitDistance(distance)

