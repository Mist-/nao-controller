from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALSoundLocalization', '127.0.0.1', PORT)

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

def setParameter(params):
	if len(params) < 2:
		print 'Error: function \'setParameter\' takes 2 params'
		return 'Error: function \'setParameter\' takes 2 params'
	parameter = parse(params[0])
	value = parse(params[1])
	return proxy.setParameter(parameter,value)

def subscribe(params):
	if len(params) < 1:
		print 'Error: function \'subscribe\' takes 2 params'
		return 'Error: function \'subscribe\' takes 2 params'
	name = parse(params[0])
	return proxy.subscribe(name)

def unsubscribe(params):
	if len(params) < 1:
		print 'Error: function \'unsubscribe\' takes 2 params'
		return 'Error: function \'unsubscribe\' takes 2 params'
	name = parse(params[0])
	return proxy.unsubscribe(name)

