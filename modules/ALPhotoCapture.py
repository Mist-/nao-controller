from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALPhotoCapture', '127.0.0.1', PORT)

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

def getCameraID(params):
	return proxy.getCameraID()

def getCaptureInterval(params):
	return proxy.getCaptureInterval()

def getColorSpace(params):
	return proxy.getColorSpace()

def getPictureFormat(params):
	return proxy.getPictureFormat()

def getResolution(params):
	return proxy.getResolution()

def halfPress(params):
	return proxy.halfPress()

def isHalfPressed(params):
	return proxy.isHalfPressed()

def isHalfPressEnabled(params):
	return proxy.isHalfPressEnabled()

def setCameraID(params):
	if len(params) < 1:
		print 'Error: function \'setCameraID\' takes 2 params'
		return 'Error: function \'setCameraID\' takes 2 params'
	cameraID = parse(params[0])
	return proxy.setCameraID(cameraID)

def setCaptureInterval(params):
	if len(params) < 1:
		print 'Error: function \'setCaptureInterval\' takes 2 params'
		return 'Error: function \'setCaptureInterval\' takes 2 params'
	captureInterval = parse(params[0])
	return proxy.setCaptureInterval(captureInterval)

def setColorSpace(params):
	if len(params) < 1:
		print 'Error: function \'setColorSpace\' takes 2 params'
		return 'Error: function \'setColorSpace\' takes 2 params'
	colorSpace = parse(params[0])
	return proxy.setColorSpace(colorSpace)

def setHalfPressEnabled(params):
	if len(params) < 1:
		print 'Error: function \'setHalfPressEnabled\' takes 2 params'
		return 'Error: function \'setHalfPressEnabled\' takes 2 params'
	enable = parse(params[0])
	return proxy.setHalfPressEnabled(enable)

def setPictureFormat(params):
	if len(params) < 1:
		print 'Error: function \'setPictureFormat\' takes 2 params'
		return 'Error: function \'setPictureFormat\' takes 2 params'
	pictureFormat = parse(params[0])
	return proxy.setPictureFormat(pictureFormat)

def setResolution(params):
	if len(params) < 1:
		print 'Error: function \'setResolution\' takes 2 params'
		return 'Error: function \'setResolution\' takes 2 params'
	resolution = parse(params[0])
	return proxy.setResolution(resolution)

def takePicture(params):
	if len(params) < 2:
		print 'Error: function \'takePicture\' takes 2 params'
		return 'Error: function \'takePicture\' takes 2 params'
	folderPath = parse(params[0])
	fileName = parse(params[1])
	return proxy.takePicture(folderPath,fileName)

def takePicture(params):
	if len(params) < 3:
		print 'Error: function \'takePicture\' takes 2 params'
		return 'Error: function \'takePicture\' takes 2 params'
	folderPath = parse(params[0])
	fileName = parse(params[1])
	overwrite = parse(params[2])
	return proxy.takePicture(folderPath,fileName,overwrite)

def takePictures(params):
	if len(params) < 3:
		print 'Error: function \'takePictures\' takes 2 params'
		return 'Error: function \'takePictures\' takes 2 params'
	numberOfPictures = parse(params[0])
	folderPath = parse(params[1])
	fileName = parse(params[2])
	return proxy.takePictures(numberOfPictures,folderPath,fileName)

def takePictures(params):
	if len(params) < 4:
		print 'Error: function \'takePictures\' takes 2 params'
		return 'Error: function \'takePictures\' takes 2 params'
	numberOfPictures = parse(params[0])
	folderPath = parse(params[1])
	fileName = parse(params[2])
	overwrite = parse(params[3])
	return proxy.takePictures(numberOfPictures,folderPath,fileName,overwrite)

