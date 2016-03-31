from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALRecharge', '127.0.0.1', PORT)

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

def lookForStation(params):
	return proxy.lookForStation()

def moveInFrontOfStation(params):
	return proxy.moveInFrontOfStation()

def dockOnStation(params):
	return proxy.dockOnStation()

def goToStation(params):
	return proxy.goToStation()

def leaveStation(params):
	return proxy.leaveStation()

def getStatus(params):
	return proxy.getStatus()

def getStationPosition(params):
	return proxy.getStationPosition()

def stopAll(params):
	return proxy.stopAll()

