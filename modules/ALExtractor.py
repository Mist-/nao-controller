from naoqi import ALProxy
from network.const import PORT, IP
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALExtractor', IP, PORT)

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

def subscribe(params):
	if len(params) < 3:
		print 'Error: function \'subscribe\' takes 2 params'
		return 'Error: function \'subscribe\' takes 2 params'
	subscribedName = parse(params[0])
	period = parse(params[1])
	precision = parse(params[2])
	return proxy.subscribe(subscribedName,period,precision)

def subscribe(params):
	if len(params) < 1:
		print 'Error: function \'subscribe\' takes 2 params'
		return 'Error: function \'subscribe\' takes 2 params'
	subscribedName = parse(params[0])
	return proxy.subscribe(subscribedName)

def unsubscribe(params):
	if len(params) < 1:
		print 'Error: function \'unsubscribe\' takes 2 params'
		return 'Error: function \'unsubscribe\' takes 2 params'
	subscribedName = parse(params[0])
	return proxy.unsubscribe(subscribedName)

def updatePeriod(params):
	if len(params) < 2:
		print 'Error: function \'updatePeriod\' takes 2 params'
		return 'Error: function \'updatePeriod\' takes 2 params'
	subscribedName = parse(params[0])
	period = parse(params[1])
	return proxy.updatePeriod(subscribedName,period)

def updatePrecision(params):
	if len(params) < 2:
		print 'Error: function \'updatePrecision\' takes 2 params'
		return 'Error: function \'updatePrecision\' takes 2 params'
	subscribedName = parse(params[0])
	precision = parse(params[1])
	return proxy.updatePrecision(subscribedName,precision)

def getCurrentPeriod(params):
	return proxy.getCurrentPeriod()

def getCurrentPrecision(params):
	return proxy.getCurrentPrecision()

def getEventList(params):
	return proxy.getEventList()

def getMemoryKeyList(params):
	return proxy.getMemoryKeyList()

def getMyPeriod(params):
	if len(params) < 1:
		print 'Error: function \'getMyPeriod\' takes 2 params'
		return 'Error: function \'getMyPeriod\' takes 2 params'
	subscribedName = parse(params[0])
	return proxy.getMyPeriod(subscribedName)

def getMyPrecision(params):
	if len(params) < 1:
		print 'Error: function \'getMyPrecision\' takes 2 params'
		return 'Error: function \'getMyPrecision\' takes 2 params'
	subscribedName = parse(params[0])
	return proxy.getMyPrecision(subscribedName)

def getOutputNames(params):
	if len(params) < 1:
		print 'Error: function \'getOutputNames\' takes 2 params'
		return 'Error: function \'getOutputNames\' takes 2 params'
	void = parse(params[0])
	return proxy.getOutputNames(void)

def getSubscribersInfo(params):
	return proxy.getSubscribersInfo()

