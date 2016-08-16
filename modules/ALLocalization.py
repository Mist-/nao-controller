from naoqi import ALProxy
from network.const import PORT, IP
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALLocalization', IP, PORT)

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

def clear(params):
	if len(params) < 1:
		print 'Error: function \'clear\' takes 2 params'
		return 'Error: function \'clear\' takes 2 params'
	pDirectory = parse(params[0])
	return proxy.clear(pDirectory)

def load(params):
	if len(params) < 1:
		print 'Error: function \'load\' takes 2 params'
		return 'Error: function \'load\' takes 2 params'
	pDirectory = parse(params[0])
	return proxy.load(pDirectory)

def save(params):
	if len(params) < 1:
		print 'Error: function \'save\' takes 2 params'
		return 'Error: function \'save\' takes 2 params'
	pDirectory = parse(params[0])
	return proxy.save(pDirectory)

def learnHome(params):
	return proxy.learnHome()

def getRobotPosition(params):
	if len(params) < 1:
		print 'Error: function \'getRobotPosition\' takes 2 params'
		return 'Error: function \'getRobotPosition\' takes 2 params'
	active = parse(params[0])
	return proxy.getRobotPosition(active)

def goToHome(params):
	return proxy.goToHome()

def stopAll(params):
	return proxy.stopAll()

def isRelocalizationRequired(params):
	return proxy.isRelocalizationRequired()

def isDataAvailable(params):
	return proxy.isDataAvailable()

def getMessageFromErrorCode(params):
	if len(params) < 1:
		print 'Error: function \'getMessageFromErrorCode\' takes 2 params'
		return 'Error: function \'getMessageFromErrorCode\' takes 2 params'
	pCode = parse(params[0])
	return proxy.getMessageFromErrorCode(pCode)

def goToPosition(params):
	if len(params) < 1:
		print 'Error: function \'goToPosition\' takes 2 params'
		return 'Error: function \'goToPosition\' takes 2 params'
	theta = parse(params[0])
	return proxy.goToPosition(theta)

def getRobotOrientation(params):
	if len(params) < 1:
		print 'Error: function \'getRobotOrientation\' takes 2 params'
		return 'Error: function \'getRobotOrientation\' takes 2 params'
	active = parse(params[0])
	return proxy.getRobotOrientation(active)

