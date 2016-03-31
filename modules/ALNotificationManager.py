from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALNotificationManager', '127.0.0.1', PORT)

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

def add(params):
	if len(params) < 1:
		print 'Error: function \'add\' takes 2 params'
		return 'Error: function \'add\' takes 2 params'
	notification = parse(params[0])
	return proxy.add(notification)

def remove(params):
	if len(params) < 1:
		print 'Error: function \'remove\' takes 2 params'
		return 'Error: function \'remove\' takes 2 params'
	notificationId = parse(params[0])
	return proxy.remove(notificationId)

def notification(params):
	if len(params) < 1:
		print 'Error: function \'notification\' takes 2 params'
		return 'Error: function \'notification\' takes 2 params'
	notificationId = parse(params[0])
	return proxy.notification(notificationId)

def notifications(params):
	return proxy.notifications()

