from naoqi import ALProxy
from network.const import PORT, IP
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALDarknessDetection', IP, PORT)

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

def getDarknessThreshold(params):
	return proxy.getDarknessThreshold()

def setDarknessThreshold(params):
	if len(params) < 1:
		print 'Error: function \'setDarknessThreshold\' takes 2 params'
		return 'Error: function \'setDarknessThreshold\' takes 2 params'
	threshold = parse(params[0])
	return proxy.setDarknessThreshold(threshold)

