from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALSensors', '127.0.0.1', PORT)

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

def getCurrentPeriod(params):
	return proxy.getCurrentPeriod()

def getCurrentPrecision(params):
	return proxy.getCurrentPrecision()

def getMyPeriod(params):
	if len(params) < 1:
		print 'Error: function \'getMyPeriod\' takes 2 params'
		return 'Error: function \'getMyPeriod\' takes 2 params'
	name = parse(params[0])
	return proxy.getMyPeriod(name)

def getMyPrecision(params):
	if len(params) < 1:
		print 'Error: function \'getMyPrecision\' takes 2 params'
		return 'Error: function \'getMyPrecision\' takes 2 params'
	name = parse(params[0])
	return proxy.getMyPrecision(name)

def getOutputNames(params):
	return proxy.getOutputNames()

def getSubscribersInfo(params):
	return proxy.getSubscribersInfo()

def run(params):
	return proxy.run()

def subscribe(params):
	if len(params) < 3:
		print 'Error: function \'subscribe\' takes 2 params'
		return 'Error: function \'subscribe\' takes 2 params'
	name = parse(params[0])
	period = parse(params[1])
	precision = parse(params[2])
	return proxy.subscribe(name,period,precision)

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

def updatePeriod(params):
	if len(params) < 2:
		print 'Error: function \'updatePeriod\' takes 2 params'
		return 'Error: function \'updatePeriod\' takes 2 params'
	name = parse(params[0])
	period = parse(params[1])
	return proxy.updatePeriod(name,period)

def updatePrecision(params):
	if len(params) < 2:
		print 'Error: function \'updatePrecision\' takes 2 params'
		return 'Error: function \'updatePrecision\' takes 2 params'
	name = parse(params[0])
	precision = parse(params[1])
	return proxy.updatePrecision(name,precision)

