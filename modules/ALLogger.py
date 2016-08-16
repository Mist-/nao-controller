from naoqi import ALProxy
from network.const import PORT, IP
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALLogger', IP, PORT)

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

def debug(params):
	if len(params) < 2:
		print 'Error: function \'debug\' takes 2 params'
		return 'Error: function \'debug\' takes 2 params'
	moduleName = parse(params[0])
	message = parse(params[1])
	return proxy.debug(moduleName,message)

def error(params):
	if len(params) < 2:
		print 'Error: function \'error\' takes 2 params'
		return 'Error: function \'error\' takes 2 params'
	moduleName = parse(params[0])
	message = parse(params[1])
	return proxy.error(moduleName,message)

def fatal(params):
	if len(params) < 2:
		print 'Error: function \'fatal\' takes 2 params'
		return 'Error: function \'fatal\' takes 2 params'
	moduleName = parse(params[0])
	message = parse(params[1])
	return proxy.fatal(moduleName,message)

def info(params):
	if len(params) < 2:
		print 'Error: function \'info\' takes 2 params'
		return 'Error: function \'info\' takes 2 params'
	moduleName = parse(params[0])
	message = parse(params[1])
	return proxy.info(moduleName,message)

def logInFile(params):
	if len(params) < 1:
		print 'Error: function \'logInFile\' takes 2 params'
		return 'Error: function \'logInFile\' takes 2 params'
	fileName = parse(params[0])
	return proxy.logInFile(fileName)

def logInForwarder(params):
	if len(params) < 1:
		print 'Error: function \'logInForwarder\' takes 2 params'
		return 'Error: function \'logInForwarder\' takes 2 params'
	inputAddress = parse(params[0])
	return proxy.logInForwarder(inputAddress)

def logInStd(params):
	return proxy.logInStd()

def logInSys(params):
	return proxy.logInSys()

def lowDebug(params):
	if len(params) < 2:
		print 'Error: function \'lowDebug\' takes 2 params'
		return 'Error: function \'lowDebug\' takes 2 params'
	moduleName = parse(params[0])
	message = parse(params[1])
	return proxy.lowDebug(moduleName,message)

def lowInfo(params):
	if len(params) < 2:
		print 'Error: function \'lowInfo\' takes 2 params'
		return 'Error: function \'lowInfo\' takes 2 params'
	moduleName = parse(params[0])
	message = parse(params[1])
	return proxy.lowInfo(moduleName,message)

def removeHandler(params):
	if len(params) < 1:
		print 'Error: function \'removeHandler\' takes 2 params'
		return 'Error: function \'removeHandler\' takes 2 params'
	name = parse(params[0])
	return proxy.removeHandler(name)

def separator(params):
	return proxy.separator()

def setFilter(params):
	return proxy.setFilter()

def setVerbosity(params):
	if len(params) < 1:
		print 'Error: function \'setVerbosity\' takes 2 params'
		return 'Error: function \'setVerbosity\' takes 2 params'
	verbosity = parse(params[0])
	return proxy.setVerbosity(verbosity)

def verbosity(params):
	return proxy.verbosity()

def warn(params):
	if len(params) < 2:
		print 'Error: function \'warn\' takes 2 params'
		return 'Error: function \'warn\' takes 2 params'
	moduleName = parse(params[0])
	message = parse(params[1])
	return proxy.warn(moduleName,message)

