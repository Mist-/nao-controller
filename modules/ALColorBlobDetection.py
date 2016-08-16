from naoqi import ALProxy
from network.const import PORT, IP
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALColorBlobDetection', IP, PORT)

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

def setColor(params):
	if len(params) < 4:
		print 'Error: function \'setColor\' takes 2 params'
		return 'Error: function \'setColor\' takes 2 params'
	r = parse(params[0])
	g = parse(params[1])
	b = parse(params[2])
	colorThres = parse(params[3])
	return proxy.setColor(r,g,b,colorThres)

def setObjectProperties(params):
	if len(params) < 3:
		print 'Error: function \'setObjectProperties\' takes 2 params'
		return 'Error: function \'setObjectProperties\' takes 2 params'
	minSize = parse(params[0])
	span = parse(params[1])
	shape = parse(params[2])
	return proxy.setObjectProperties(minSize,span,shape)

def setObjectProperties(params):
	if len(params) < 2:
		print 'Error: function \'setObjectProperties\' takes 2 params'
		return 'Error: function \'setObjectProperties\' takes 2 params'
	minSize = parse(params[0])
	span = parse(params[1])
	return proxy.setObjectProperties(minSize,span)

def getCircle(params):
	return proxy.getCircle()

def getAutoExposure(params):
	return proxy.getAutoExposure()

def setAutoExposure(params):
	if len(params) < 1:
		print 'Error: function \'setAutoExposure\' takes 2 params'
		return 'Error: function \'setAutoExposure\' takes 2 params'
	mode = parse(params[0])
	return proxy.setAutoExposure(mode)

