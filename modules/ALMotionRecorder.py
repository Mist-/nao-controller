from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALMotionRecorder', '127.0.0.1', PORT)

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

def startInteractiveRecording(params):
	if len(params) < 4:
		print 'Error: function \'startInteractiveRecording\' takes 2 params'
		return 'Error: function \'startInteractiveRecording\' takes 2 params'
	jointsToRecord = parse(params[0])
	nbPoses = parse(params[1])
	extensionAllowed = parse(params[2])
	mode = parse(params[3])
	return proxy.startInteractiveRecording(jointsToRecord,nbPoses,extensionAllowed,mode)

def startPeriodicRecording(params):
	if len(params) < 6:
		print 'Error: function \'startPeriodicRecording\' takes 2 params'
		return 'Error: function \'startPeriodicRecording\' takes 2 params'
	jointsToRecord = parse(params[0])
	nbPoses = parse(params[1])
	extensionAllowed = parse(params[2])
	timeStep = parse(params[3])
	jointsToReplay = parse(params[4])
	replayData = parse(params[5])
	return proxy.startPeriodicRecording(jointsToRecord,nbPoses,extensionAllowed,timeStep,jointsToReplay,replayData)

def stopAndGetRecording(params):
	return proxy.stopAndGetRecording()

