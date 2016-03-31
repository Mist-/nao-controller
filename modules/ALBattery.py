from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALBattery', '127.0.0.1', PORT)

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

def enablePowerMonitoring(params):
	if len(params) < 1:
		print 'Error: function \'enablePowerMonitoring\' takes 2 params'
		return 'Error: function \'enablePowerMonitoring\' takes 2 params'
	enable = parse(params[0])
	return proxy.enablePowerMonitoring(enable)

def getBatteryCharge(params):
	return proxy.getBatteryCharge()

