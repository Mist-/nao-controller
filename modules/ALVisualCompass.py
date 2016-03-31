from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALVisualCompass', '127.0.0.1', PORT)

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

def enableReferenceRefresh(params):
	if len(params) < 1:
		print 'Error: function \'enableReferenceRefresh\' takes 2 params'
		return 'Error: function \'enableReferenceRefresh\' takes 2 params'
	refresh = parse(params[0])
	return proxy.enableReferenceRefresh(refresh)

def getMatchingQuality(params):
	return proxy.getMatchingQuality()

def getReferenceImage(params):
	return proxy.getReferenceImage()

def moveStraightTo(params):
	if len(params) < 1:
		print 'Error: function \'moveStraightTo\' takes 2 params'
		return 'Error: function \'moveStraightTo\' takes 2 params'
	pDistance = parse(params[0])
	return proxy.moveStraightTo(pDistance)

def moveTo(params):
	if len(params) < 3:
		print 'Error: function \'moveTo\' takes 2 params'
		return 'Error: function \'moveTo\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	return proxy.moveTo(x,y,theta)

def setCurrentImageAsReference(params):
	return proxy.setCurrentImageAsReference()

def waitUntilTargetReached(params):
	return proxy.waitUntilTargetReached()

