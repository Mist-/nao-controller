from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALPreferenceManager', '127.0.0.1', PORT)

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

def getValue(params):
	if len(params) < 2:
		print 'Error: function \'getValue\' takes 2 params'
		return 'Error: function \'getValue\' takes 2 params'
	domain = parse(params[0])
	name = parse(params[1])
	return proxy.getValue(domain,name)

def getValueList(params):
	if len(params) < 1:
		print 'Error: function \'getValueList\' takes 2 params'
		return 'Error: function \'getValueList\' takes 2 params'
	domain = parse(params[0])
	return proxy.getValueList(domain)

def getDomainList(params):
	return proxy.getDomainList()

def importPrefFile(params):
	if len(params) < 4:
		print 'Error: function \'importPrefFile\' takes 2 params'
		return 'Error: function \'importPrefFile\' takes 2 params'
	domain = parse(params[0])
	applicationName = parse(params[1])
	filename = parse(params[2])
	override = parse(params[3])
	return proxy.importPrefFile(domain,applicationName,filename,override)

def removeValue(params):
	if len(params) < 2:
		print 'Error: function \'removeValue\' takes 2 params'
		return 'Error: function \'removeValue\' takes 2 params'
	domain = parse(params[0])
	name = parse(params[1])
	return proxy.removeValue(domain,name)

def removeDomainValues(params):
	if len(params) < 1:
		print 'Error: function \'removeDomainValues\' takes 2 params'
		return 'Error: function \'removeDomainValues\' takes 2 params'
	domain = parse(params[0])
	return proxy.removeDomainValues(domain)

def setValue(params):
	if len(params) < 3:
		print 'Error: function \'setValue\' takes 2 params'
		return 'Error: function \'setValue\' takes 2 params'
	domain = parse(params[0])
	name = parse(params[1])
	value = parse(params[2])
	return proxy.setValue(domain,name,value)

def update(params):
	return proxy.update()

