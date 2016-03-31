from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALVisionRecognition', '127.0.0.1', PORT)

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

def changeDatabase(params):
	if len(params) < 2:
		print 'Error: function \'changeDatabase\' takes 2 params'
		return 'Error: function \'changeDatabase\' takes 2 params'
	databasePath = parse(params[0])
	databaseName = parse(params[1])
	return proxy.changeDatabase(databasePath,databaseName)

def getParam(params):
	if len(params) < 1:
		print 'Error: function \'getParam\' takes 2 params'
		return 'Error: function \'getParam\' takes 2 params'
	paramName = parse(params[0])
	return proxy.getParam(paramName)

def setParam(params):
	if len(params) < 2:
		print 'Error: function \'setParam\' takes 2 params'
		return 'Error: function \'setParam\' takes 2 params'
	paramName = parse(params[0])
	paramValue = parse(params[1])
	return proxy.setParam(paramName,paramValue)

