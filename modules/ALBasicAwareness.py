from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALBasicAwareness', '127.0.0.1', PORT)

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

def startAwareness(params):
	return proxy.startAwareness()

def stopAwareness(params):
	return proxy.stopAwareness()

def isAwarenessRunning(params):
	return proxy.isAwarenessRunning()

def setStimulusDetectionEnabled(params):
	if len(params) < 2:
		print 'Error: function \'setStimulusDetectionEnabled\' takes 2 params'
		return 'Error: function \'setStimulusDetectionEnabled\' takes 2 params'
	stimType = parse(params[0])
	enable = parse(params[1])
	return proxy.setStimulusDetectionEnabled(stimType,enable)

def isStimulusDetectionEnabled(params):
	if len(params) < 1:
		print 'Error: function \'isStimulusDetectionEnabled\' takes 2 params'
		return 'Error: function \'isStimulusDetectionEnabled\' takes 2 params'
	stimType = parse(params[0])
	return proxy.isStimulusDetectionEnabled(stimType)

def setEngagementMode(params):
	if len(params) < 1:
		print 'Error: function \'setEngagementMode\' takes 2 params'
		return 'Error: function \'setEngagementMode\' takes 2 params'
	modeName = parse(params[0])
	return proxy.setEngagementMode(modeName)

def getEngagementMode(params):
	return proxy.getEngagementMode()

def engagePerson(params):
	if len(params) < 1:
		print 'Error: function \'engagePerson\' takes 2 params'
		return 'Error: function \'engagePerson\' takes 2 params'
	idPersonToEngage = parse(params[0])
	return proxy.engagePerson(idPersonToEngage)

def setTrackingMode(params):
	if len(params) < 1:
		print 'Error: function \'setTrackingMode\' takes 2 params'
		return 'Error: function \'setTrackingMode\' takes 2 params'
	trackingMode = parse(params[0])
	return proxy.setTrackingMode(trackingMode)

def getTrackingMode(params):
	return proxy.getTrackingMode()

def setParameter(params):
	if len(params) < 2:
		print 'Error: function \'setParameter\' takes 2 params'
		return 'Error: function \'setParameter\' takes 2 params'
	paramName = parse(params[0])
	paramValue = parse(params[1])
	return proxy.setParameter(paramName,paramValue)

def getParameter(params):
	if len(params) < 1:
		print 'Error: function \'getParameter\' takes 2 params'
		return 'Error: function \'getParameter\' takes 2 params'
	paramName = parse(params[0])
	return proxy.getParameter(paramName)

def resetAllParameters(params):
	return proxy.resetAllParameters()

