from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALNavigation', '127.0.0.1', PORT)

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

def navigateTo(params):
	if len(params) < 2:
		print 'Error: function \'navigateTo\' takes 2 params'
		return 'Error: function \'navigateTo\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	return proxy.navigateTo(x,y)

def navigateTo(params):
	if len(params) < 3:
		print 'Error: function \'navigateTo\' takes 2 params'
		return 'Error: function \'navigateTo\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	config = parse(params[2])
	return proxy.navigateTo(x,y,config)

def moveAlong(params):
	if len(params) < 1:
		print 'Error: function \'moveAlong\' takes 2 params'
		return 'Error: function \'moveAlong\' takes 2 params'
	trajectory = parse(params[0])
	return proxy.moveAlong(trajectory)

def setSecurityDistance(params):
	if len(params) < 1:
		print 'Error: function \'setSecurityDistance\' takes 2 params'
		return 'Error: function \'setSecurityDistance\' takes 2 params'
	distance = parse(params[0])
	return proxy.setSecurityDistance(distance)

def getSecurityDistance(params):
	return proxy.getSecurityDistance()

def move(params):
	if len(params) < 3:
		print 'Error: function \'move\' takes 2 params'
		return 'Error: function \'move\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	return proxy.move(x,y,theta)

def move(params):
	if len(params) < 4:
		print 'Error: function \'move\' takes 2 params'
		return 'Error: function \'move\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	moveConfig = parse(params[3])
	return proxy.move(x,y,theta,moveConfig)

def moveToward(params):
	if len(params) < 3:
		print 'Error: function \'moveToward\' takes 2 params'
		return 'Error: function \'moveToward\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	return proxy.moveToward(x,y,theta)

def moveToward(params):
	if len(params) < 4:
		print 'Error: function \'moveToward\' takes 2 params'
		return 'Error: function \'moveToward\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	moveConfig = parse(params[3])
	return proxy.moveToward(x,y,theta,moveConfig)

def moveTo(params):
	if len(params) < 3:
		print 'Error: function \'moveTo\' takes 2 params'
		return 'Error: function \'moveTo\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	return proxy.moveTo(x,y,theta)

def moveTo(params):
	if len(params) < 4:
		print 'Error: function \'moveTo\' takes 2 params'
		return 'Error: function \'moveTo\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	moveConfig = parse(params[3])
	return proxy.moveTo(x,y,theta,moveConfig)

