from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALPeoplePerception', '127.0.0.1', PORT)

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

def getMaximumDetectionRange(params):
	return proxy.getMaximumDetectionRange()

def getTimeBeforePersonDisappears(params):
	return proxy.getTimeBeforePersonDisappears()

def getTimeBeforeVisiblePersonDisappears(params):
	return proxy.getTimeBeforeVisiblePersonDisappears()

def isFaceDetectionEnabled(params):
	return proxy.isFaceDetectionEnabled()

def isFastModeEnabled(params):
	return proxy.isFastModeEnabled()

def isGraphicalDisplayEnabled(params):
	return proxy.isGraphicalDisplayEnabled()

def isMovementDetectionEnabled(params):
	return proxy.isMovementDetectionEnabled()

def resetPopulation(params):
	return proxy.resetPopulation()

def setFastModeEnabled(params):
	if len(params) < 1:
		print 'Error: function \'setFastModeEnabled\' takes 2 params'
		return 'Error: function \'setFastModeEnabled\' takes 2 params'
	enable = parse(params[0])
	return proxy.setFastModeEnabled(enable)

def setGraphicalDisplayEnabled(params):
	if len(params) < 1:
		print 'Error: function \'setGraphicalDisplayEnabled\' takes 2 params'
		return 'Error: function \'setGraphicalDisplayEnabled\' takes 2 params'
	enable = parse(params[0])
	return proxy.setGraphicalDisplayEnabled(enable)

def setMaximumDetectionRange(params):
	if len(params) < 1:
		print 'Error: function \'setMaximumDetectionRange\' takes 2 params'
		return 'Error: function \'setMaximumDetectionRange\' takes 2 params'
	range = parse(params[0])
	return proxy.setMaximumDetectionRange(range)

def setMovementDetectionEnabled(params):
	if len(params) < 1:
		print 'Error: function \'setMovementDetectionEnabled\' takes 2 params'
		return 'Error: function \'setMovementDetectionEnabled\' takes 2 params'
	enable = parse(params[0])
	return proxy.setMovementDetectionEnabled(enable)

def setTimeBeforePersonDisappears(params):
	if len(params) < 1:
		print 'Error: function \'setTimeBeforePersonDisappears\' takes 2 params'
		return 'Error: function \'setTimeBeforePersonDisappears\' takes 2 params'
	seconds = parse(params[0])
	return proxy.setTimeBeforePersonDisappears(seconds)

def setTimeBeforeVisiblePersonDisappears(params):
	if len(params) < 1:
		print 'Error: function \'setTimeBeforeVisiblePersonDisappears\' takes 2 params'
		return 'Error: function \'setTimeBeforeVisiblePersonDisappears\' takes 2 params'
	seconds = parse(params[0])
	return proxy.setTimeBeforeVisiblePersonDisappears(seconds)

def setFaceDetectionEnabled(params):
	if len(params) < 1:
		print 'Error: function \'setFaceDetectionEnabled\' takes 2 params'
		return 'Error: function \'setFaceDetectionEnabled\' takes 2 params'
	enable = parse(params[0])
	return proxy.setFaceDetectionEnabled(enable)

