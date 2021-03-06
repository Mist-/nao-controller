from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALRedBallTracker', '127.0.0.1', PORT)

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

def getPosition(params):
	return proxy.getPosition()

def isActive(params):
	return proxy.isActive()

def isNewData(params):
	return proxy.isNewData()

def setWholeBodyOn(params):
	if len(params) < 1:
		print 'Error: function \'setWholeBodyOn\' takes 2 params'
		return 'Error: function \'setWholeBodyOn\' takes 2 params'
	wholeBodyOn = parse(params[0])
	return proxy.setWholeBodyOn(wholeBodyOn)

def startTracker(params):
	return proxy.startTracker()

def stopTracker(params):
	return proxy.stopTracker()

