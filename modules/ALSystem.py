from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALSystem', '127.0.0.1', PORT)

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

def robotName(params):
	return proxy.robotName()

def robotIcon(params):
	return proxy.robotIcon()

def setRobotName(params):
	if len(params) < 1:
		print 'Error: function \'setRobotName\' takes 2 params'
		return 'Error: function \'setRobotName\' takes 2 params'
	name = parse(params[0])
	return proxy.setRobotName(name)

def shutdown(params):
	return proxy.shutdown()

def reboot(params):
	return proxy.reboot()

def systemVersion(params):
	return proxy.systemVersion()

def timezone(params):
	return proxy.timezone()

def setTimezone(params):
	if len(params) < 1:
		print 'Error: function \'setTimezone\' takes 2 params'
		return 'Error: function \'setTimezone\' takes 2 params'
	timezone = parse(params[0])
	return proxy.setTimezone(timezone)

def freeMemory(params):
	return proxy.freeMemory()

def totalMemory(params):
	return proxy.totalMemory()

def diskFree(params):
	if len(params) < 1:
		print 'Error: function \'diskFree\' takes 2 params'
		return 'Error: function \'diskFree\' takes 2 params'
	all = parse(params[0])
	return proxy.diskFree(all)

def previousSystemVersion(params):
	return proxy.previousSystemVersion()

def changePassword(params):
	if len(params) < 2:
		print 'Error: function \'changePassword\' takes 2 params'
		return 'Error: function \'changePassword\' takes 2 params'
	old = parse(params[0])
	new = parse(params[1])
	return proxy.changePassword(old,new)

