from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALMovementDetection', '127.0.0.1', PORT)

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

def resetDetection(params):
	return proxy.resetDetection()

def getColorSensitivity(params):
	return proxy.getColorSensitivity()

def setColorSensitivity(params):
	if len(params) < 1:
		print 'Error: function \'setColorSensitivity\' takes 2 params'
		return 'Error: function \'setColorSensitivity\' takes 2 params'
	sensitivity = parse(params[0])
	return proxy.setColorSensitivity(sensitivity)

def getDepthSensitivity(params):
	return proxy.getDepthSensitivity()

def setDepthSensitivity(params):
	if len(params) < 1:
		print 'Error: function \'setDepthSensitivity\' takes 2 params'
		return 'Error: function \'setDepthSensitivity\' takes 2 params'
	sensitivity = parse(params[0])
	return proxy.setDepthSensitivity(sensitivity)

