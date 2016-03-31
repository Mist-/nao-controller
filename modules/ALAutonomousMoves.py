from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALAutonomousMoves', '127.0.0.1', PORT)

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

def setExpressiveListeningEnabled(params):
	if len(params) < 1:
		print 'Error: function \'setExpressiveListeningEnabled\' takes 2 params'
		return 'Error: function \'setExpressiveListeningEnabled\' takes 2 params'
	enabled = parse(params[0])
	return proxy.setExpressiveListeningEnabled(enabled)

def getExpressiveListeningEnabled(params):
	return proxy.getExpressiveListeningEnabled()

def setBackgroundStrategy(params):
	if len(params) < 1:
		print 'Error: function \'setBackgroundStrategy\' takes 2 params'
		return 'Error: function \'setBackgroundStrategy\' takes 2 params'
	stategy = parse(params[0])
	return proxy.setBackgroundStrategy(stategy)

def getBackgroundStrategy(params):
	return proxy.getBackgroundStrategy()

