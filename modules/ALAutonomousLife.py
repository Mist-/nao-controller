from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALAutonomousLife', '127.0.0.1', PORT)

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

def setState(params):
	if len(params) < 1:
		print 'Error: function \'setState\' takes 2 params'
		return 'Error: function \'setState\' takes 2 params'
	state = parse(params[0])
	return proxy.setState(state)

def getState(params):
	return proxy.getState()

def setRobotOffsetFromFloor(params):
	if len(params) < 1:
		print 'Error: function \'setRobotOffsetFromFloor\' takes 2 params'
		return 'Error: function \'setRobotOffsetFromFloor\' takes 2 params'
	offset = parse(params[0])
	return proxy.setRobotOffsetFromFloor(offset)

def getRobotOffsetFromFloor(params):
	return proxy.getRobotOffsetFromFloor()

def setSafeguardEnabled(params):
	if len(params) < 1:
		print 'Error: function \'setSafeguardEnabled\' takes 2 params'
		return 'Error: function \'setSafeguardEnabled\' takes 2 params'
	name = parse(params[0])
	return proxy.setSafeguardEnabled(name)

def isSafeguardEnabled(params):
	if len(params) < 1:
		print 'Error: function \'isSafeguardEnabled\' takes 2 params'
		return 'Error: function \'isSafeguardEnabled\' takes 2 params'
	name = parse(params[0])
	return proxy.isSafeguardEnabled(name)

def focusedActivity(params):
	return proxy.focusedActivity()

def switchFocus(params):
	return proxy.switchFocus()

def switchFocus(params):
	if len(params) < 1:
		print 'Error: function \'switchFocus\' takes 2 params'
		return 'Error: function \'switchFocus\' takes 2 params'
	activity_name = parse(params[0])
	return proxy.switchFocus(activity_name)

def switchFocus(params):
	if len(params) < 2:
		print 'Error: function \'switchFocus\' takes 2 params'
		return 'Error: function \'switchFocus\' takes 2 params'
	activity_name = parse(params[0])
	flags = parse(params[1])
	return proxy.switchFocus(activity_name,flags)

def stopFocus(params):
	return proxy.stopFocus()

def stopAll(params):
	return proxy.stopAll()

def getLifeTime(params):
	return proxy.getLifeTime()

def getActivityStatistics(params):
	return proxy.getActivityStatistics()

def getAutonomousActivityStatistics(params):
	return proxy.getAutonomousActivityStatistics()

def getFocusHistory(params):
	return proxy.getFocusHistory()

def getFocusHistory(params):
	return proxy.getFocusHistory()

def getFocusHistory(params):
	if len(params) < 1:
		print 'Error: function \'getFocusHistory\' takes 2 params'
		return 'Error: function \'getFocusHistory\' takes 2 params'
	depth = parse(params[0])
	return proxy.getFocusHistory(depth)

def getStateHistory(params):
	return proxy.getStateHistory()

def getStateHistory(params):
	return proxy.getStateHistory()

def getStateHistory(params):
	if len(params) < 1:
		print 'Error: function \'getStateHistory\' takes 2 params'
		return 'Error: function \'getStateHistory\' takes 2 params'
	depth = parse(params[0])
	return proxy.getStateHistory(depth)

def getActivityNature(params):
	if len(params) < 1:
		print 'Error: function \'getActivityNature\' takes 2 params'
		return 'Error: function \'getActivityNature\' takes 2 params'
	activity_name = parse(params[0])
	return proxy.getActivityNature(activity_name)

