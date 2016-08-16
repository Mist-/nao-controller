from naoqi import ALProxy
from network.const import PORT, IP
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALDiagnosis', IP, PORT)

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

def getActiveDiagnosis(params):
	return proxy.getActiveDiagnosis()

def getPassiveDiagnosis(params):
	return proxy.getPassiveDiagnosis()

def isNotificationEnabled(params):
	return proxy.isNotificationEnabled()

def setEnableNotification(params):
	if len(params) < 1:
		print 'Error: function \'setEnableNotification\' takes 2 params'
		return 'Error: function \'setEnableNotification\' takes 2 params'
	enable = parse(params[0])
	return proxy.setEnableNotification(enable)

