from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALVisionExtractor', '127.0.0.1', PORT)

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

def setFrameRate(params):
	if len(params) < 2:
		print 'Error: function \'setFrameRate\' takes 2 params'
		return 'Error: function \'setFrameRate\' takes 2 params'
	pSubscribedName = parse(params[0])
	framerate = parse(params[1])
	return proxy.setFrameRate(pSubscribedName,framerate)

def setFrameRate(params):
	if len(params) < 1:
		print 'Error: function \'setFrameRate\' takes 2 params'
		return 'Error: function \'setFrameRate\' takes 2 params'
	framerate = parse(params[0])
	return proxy.setFrameRate(framerate)

def setResolution(params):
	if len(params) < 1:
		print 'Error: function \'setResolution\' takes 2 params'
		return 'Error: function \'setResolution\' takes 2 params'
	resolution = parse(params[0])
	return proxy.setResolution(resolution)

def setActiveCamera(params):
	if len(params) < 1:
		print 'Error: function \'setActiveCamera\' takes 2 params'
		return 'Error: function \'setActiveCamera\' takes 2 params'
	cameraId = parse(params[0])
	return proxy.setActiveCamera(cameraId)

def pause(params):
	if len(params) < 1:
		print 'Error: function \'pause\' takes 2 params'
		return 'Error: function \'pause\' takes 2 params'
	paused = parse(params[0])
	return proxy.pause(paused)

def getFrameRate(params):
	return proxy.getFrameRate()

def getResolution(params):
	return proxy.getResolution()

def getActiveCamera(params):
	return proxy.getActiveCamera()

def isPaused(params):
	return proxy.isPaused()

def isProcessing(params):
	return proxy.isProcessing()

def setParameter(params):
	if len(params) < 2:
		print 'Error: function \'setParameter\' takes 2 params'
		return 'Error: function \'setParameter\' takes 2 params'
	paramName = parse(params[0])
	paramValue = parse(params[1])
	return proxy.setParameter(paramName,paramValue)

