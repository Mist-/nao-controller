from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALModule', '127.0.0.1', PORT)

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

def isRunning(params):
	if len(params) < 1:
		print 'Error: function \'isRunning\' takes 2 params'
		return 'Error: function \'isRunning\' takes 2 params'
	id = parse(params[0])
	return proxy.isRunning(id)

def wait(params):
	if len(params) < 2:
		print 'Error: function \'wait\' takes 2 params'
		return 'Error: function \'wait\' takes 2 params'
	id = parse(params[0])
	timeout = parse(params[1])
	return proxy.wait(id,timeout)

def stop(params):
	if len(params) < 1:
		print 'Error: function \'stop\' takes 2 params'
		return 'Error: function \'stop\' takes 2 params'
	id = parse(params[0])
	return proxy.stop(id)

def exit(params):
	return proxy.exit()

def getBrokerName(params):
	return proxy.getBrokerName()

def getMethodList(params):
	return proxy.getMethodList()

def getMethodHelp(params):
	if len(params) < 1:
		print 'Error: function \'getMethodHelp\' takes 2 params'
		return 'Error: function \'getMethodHelp\' takes 2 params'
	methodName = parse(params[0])
	return proxy.getMethodHelp(methodName)

def getModuleHelp(params):
	return proxy.getModuleHelp()

def getUsage(params):
	if len(params) < 1:
		print 'Error: function \'getUsage\' takes 2 params'
		return 'Error: function \'getUsage\' takes 2 params'
	methodName = parse(params[0])
	return proxy.getUsage(methodName)

def ping(params):
	return proxy.ping()

def version(params):
	return proxy.version()

