from naoqi import ALProxy
from network.const import PORT, IP
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALFaceDetection', IP, PORT)

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

def clearDatabase(params):
	return proxy.clearDatabase()

def forgetPerson(params):
	if len(params) < 1:
		print 'Error: function \'forgetPerson\' takes 2 params'
		return 'Error: function \'forgetPerson\' takes 2 params'
	name = parse(params[0])
	return proxy.forgetPerson(name)

def getLearnedFacesList(params):
	return proxy.getLearnedFacesList()

def getRecognitionConfidenceThreshold(params):
	return proxy.getRecognitionConfidenceThreshold()

def importOldDatabase(params):
	if len(params) < 1:
		print 'Error: function \'importOldDatabase\' takes 2 params'
		return 'Error: function \'importOldDatabase\' takes 2 params'
	policy = parse(params[0])
	return proxy.importOldDatabase(policy)

def isRecognitionEnabled(params):
	return proxy.isRecognitionEnabled()

def isTrackingEnabled(params):
	return proxy.isTrackingEnabled()

def learnFace(params):
	if len(params) < 1:
		print 'Error: function \'learnFace\' takes 2 params'
		return 'Error: function \'learnFace\' takes 2 params'
	name = parse(params[0])
	return proxy.learnFace(name)

def reLearnFace(params):
	if len(params) < 1:
		print 'Error: function \'reLearnFace\' takes 2 params'
		return 'Error: function \'reLearnFace\' takes 2 params'
	name = parse(params[0])
	return proxy.reLearnFace(name)

def setRecognitionConfidenceThreshold(params):
	if len(params) < 1:
		print 'Error: function \'setRecognitionConfidenceThreshold\' takes 2 params'
		return 'Error: function \'setRecognitionConfidenceThreshold\' takes 2 params'
	threshold = parse(params[0])
	return proxy.setRecognitionConfidenceThreshold(threshold)

def setRecognitionEnabled(params):
	if len(params) < 1:
		print 'Error: function \'setRecognitionEnabled\' takes 2 params'
		return 'Error: function \'setRecognitionEnabled\' takes 2 params'
	enable = parse(params[0])
	return proxy.setRecognitionEnabled(enable)

def setTrackingEnabled(params):
	if len(params) < 1:
		print 'Error: function \'setTrackingEnabled\' takes 2 params'
		return 'Error: function \'setTrackingEnabled\' takes 2 params'
	enable = parse(params[0])
	return proxy.setTrackingEnabled(enable)

def enableRecognition(params):
	if len(params) < 1:
		print 'Error: function \'enableRecognition\' takes 2 params'
		return 'Error: function \'enableRecognition\' takes 2 params'
	enable = parse(params[0])
	return proxy.enableRecognition(enable)

def enableTracking(params):
	if len(params) < 1:
		print 'Error: function \'enableTracking\' takes 2 params'
		return 'Error: function \'enableTracking\' takes 2 params'
	enable = parse(params[0])
	return proxy.enableTracking(enable)

