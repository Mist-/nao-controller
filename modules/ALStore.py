from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALStore', '127.0.0.1', PORT)

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

def update(params):
	return proxy.update()

def stopUpdate(params):
	return proxy.stopUpdate()

