from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALFaceCharacteristics', '127.0.0.1', PORT)

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

def analyzeFaceCharacteristics(params):
	if len(params) < 1:
		print 'Error: function \'analyzeFaceCharacteristics\' takes 2 params'
		return 'Error: function \'analyzeFaceCharacteristics\' takes 2 params'
	id = parse(params[0])
	return proxy.analyzeFaceCharacteristics(id)

def getSmilingThreshold(params):
	return proxy.getSmilingThreshold()

def setSmilingThreshold(params):
	if len(params) < 1:
		print 'Error: function \'setSmilingThreshold\' takes 2 params'
		return 'Error: function \'setSmilingThreshold\' takes 2 params'
	threshold = parse(params[0])
	return proxy.setSmilingThreshold(threshold)

