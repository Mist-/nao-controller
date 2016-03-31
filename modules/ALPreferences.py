from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALPreferences', '127.0.0.1', PORT)

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

def readPrefFile(params):
	if len(params) < 2:
		print 'Error: function \'readPrefFile\' takes 2 params'
		return 'Error: function \'readPrefFile\' takes 2 params'
	fileName = parse(params[0])
	autoGenerateMemoryNames = parse(params[1])
	return proxy.readPrefFile(fileName,autoGenerateMemoryNames)

def saveToMemory(params):
	if len(params) < 1:
		print 'Error: function \'saveToMemory\' takes 2 params'
		return 'Error: function \'saveToMemory\' takes 2 params'
	prefs = parse(params[0])
	return proxy.saveToMemory(prefs)

def writePrefFile(params):
	if len(params) < 3:
		print 'Error: function \'writePrefFile\' takes 2 params'
		return 'Error: function \'writePrefFile\' takes 2 params'
	fileName = parse(params[0])
	prefs = parse(params[1])
	ignoreMemoryNames = parse(params[2])
	return proxy.writePrefFile(fileName,prefs,ignoreMemoryNames)

def removePrefFile(params):
	if len(params) < 1:
		print 'Error: function \'removePrefFile\' takes 2 params'
		return 'Error: function \'removePrefFile\' takes 2 params'
	fileName = parse(params[0])
	return proxy.removePrefFile(fileName)

