from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALVideoRecorder', '127.0.0.1', PORT)

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

def isRecording(params):
	return proxy.isRecording()

def getCameraID(params):
	return proxy.getCameraID()

def getColorSpace(params):
	return proxy.getColorSpace()

def getFrameRate(params):
	return proxy.getFrameRate()

def getResolution(params):
	return proxy.getResolution()

def getVideoFormat(params):
	return proxy.getVideoFormat()

def setCameraID(params):
	if len(params) < 1:
		print 'Error: function \'setCameraID\' takes 2 params'
		return 'Error: function \'setCameraID\' takes 2 params'
	cameraID = parse(params[0])
	return proxy.setCameraID(cameraID)

def setColorSpace(params):
	if len(params) < 1:
		print 'Error: function \'setColorSpace\' takes 2 params'
		return 'Error: function \'setColorSpace\' takes 2 params'
	colorSpace = parse(params[0])
	return proxy.setColorSpace(colorSpace)

def setFrameRate(params):
	if len(params) < 1:
		print 'Error: function \'setFrameRate\' takes 2 params'
		return 'Error: function \'setFrameRate\' takes 2 params'
	frameRate = parse(params[0])
	return proxy.setFrameRate(frameRate)

def setResolution(params):
	if len(params) < 1:
		print 'Error: function \'setResolution\' takes 2 params'
		return 'Error: function \'setResolution\' takes 2 params'
	resolution = parse(params[0])
	return proxy.setResolution(resolution)

def setVideoFormat(params):
	if len(params) < 1:
		print 'Error: function \'setVideoFormat\' takes 2 params'
		return 'Error: function \'setVideoFormat\' takes 2 params'
	videoFormat = parse(params[0])
	return proxy.setVideoFormat(videoFormat)

def startRecording(params):
	if len(params) < 2:
		print 'Error: function \'startRecording\' takes 2 params'
		return 'Error: function \'startRecording\' takes 2 params'
	folderPath = parse(params[0])
	fileName = parse(params[1])
	return proxy.startRecording(folderPath,fileName)

def startRecording(params):
	if len(params) < 3:
		print 'Error: function \'startRecording\' takes 2 params'
		return 'Error: function \'startRecording\' takes 2 params'
	folderPath = parse(params[0])
	fileName = parse(params[1])
	overwrite = parse(params[2])
	return proxy.startRecording(folderPath,fileName,overwrite)

def stopRecording(params):
	return proxy.stopRecording()

