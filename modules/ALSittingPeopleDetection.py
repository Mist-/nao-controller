from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALSittingPeopleDetection', '127.0.0.1', PORT)

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

def getSittingThreshold(params):
	return proxy.getSittingThreshold()

def setSittingThreshold(params):
	if len(params) < 1:
		print 'Error: function \'setSittingThreshold\' takes 2 params'
		return 'Error: function \'setSittingThreshold\' takes 2 params'
	threshold = parse(params[0])
	return proxy.setSittingThreshold(threshold)

