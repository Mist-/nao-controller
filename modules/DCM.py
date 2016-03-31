from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy(DCM, '127.0.0.1', PORT)

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

def createAlias(params):
	if len(params) < 1:
		print 'Error: function \'createAlias\' takes 2 params'
		return 'Error: function \'createAlias\' takes 2 params'
	alias = parse(params[0])
	return proxy.createAlias(alias)

def getPrefix(params):
	return proxy.getPrefix()

def getTime(params):
	if len(params) < 1:
		print 'Error: function \'getTime\' takes 2 params'
		return 'Error: function \'getTime\' takes 2 params'
	offset = parse(params[0])
	return proxy.getTime(offset)

def set(params):
	if len(params) < 1:
		print 'Error: function \'set\' takes 2 params'
		return 'Error: function \'set\' takes 2 params'
	request = parse(params[0])
	return proxy.set(request)

def setAlias(params):
	if len(params) < 1:
		print 'Error: function \'setAlias\' takes 2 params'
		return 'Error: function \'setAlias\' takes 2 params'
	request = parse(params[0])
	return proxy.setAlias(request)

