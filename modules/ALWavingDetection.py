from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALWavingDetection', '127.0.0.1', PORT)

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

def getMaxDistance(params):
	return proxy.getMaxDistance()

def getMinSize(params):
	return proxy.getMinSize()

def setMaxDistance(params):
	if len(params) < 1:
		print 'Error: function \'setMaxDistance\' takes 2 params'
		return 'Error: function \'setMaxDistance\' takes 2 params'
	distance = parse(params[0])
	return proxy.setMaxDistance(distance)

def setMinSize(params):
	if len(params) < 1:
		print 'Error: function \'setMinSize\' takes 2 params'
		return 'Error: function \'setMinSize\' takes 2 params'
	size = parse(params[0])
	return proxy.setMinSize(size)

