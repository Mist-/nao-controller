from naoqi import ALProxy
from network.const import PORT, IP
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALLeds', IP, PORT)

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

def createGroup(params):
	if len(params) < 2:
		print 'Error: function \'createGroup\' takes 2 params'
		return 'Error: function \'createGroup\' takes 2 params'
	groupName = parse(params[0])
	ledNames = parse(params[1])
	return proxy.createGroup(groupName,ledNames)

def earLedsSetAngle(params):
	if len(params) < 3:
		print 'Error: function \'earLedsSetAngle\' takes 2 params'
		return 'Error: function \'earLedsSetAngle\' takes 2 params'
	degrees = parse(params[0])
	duration = parse(params[1])
	leaveOnAtEnd = parse(params[2])
	return proxy.earLedsSetAngle(degrees,duration,leaveOnAtEnd)

def fade(params):
	if len(params) < 3:
		print 'Error: function \'fade\' takes 2 params'
		return 'Error: function \'fade\' takes 2 params'
	name = parse(params[0])
	intensity = parse(params[1])
	duration = parse(params[2])
	return proxy.fade(name,intensity,duration)

def fadeListRGB(params):
	if len(params) < 3:
		print 'Error: function \'fadeListRGB\' takes 2 params'
		return 'Error: function \'fadeListRGB\' takes 2 params'
	name = parse(params[0])
	rgbList = parse(params[1])
	timeList = parse(params[2])
	return proxy.fadeListRGB(name,rgbList,timeList)

def fadeRGB(params):
	if len(params) < 5:
		print 'Error: function \'fadeRGB\' takes 2 params'
		return 'Error: function \'fadeRGB\' takes 2 params'
	name = parse(params[0])
	red = parse(params[1])
	green = parse(params[2])
	blue = parse(params[3])
	duration = parse(params[4])
	return proxy.fadeRGB(name,red,green,blue,duration)

def fadeRGB(params):
	if len(params) < 3:
		print 'Error: function \'fadeRGB\' takes 2 params'
		return 'Error: function \'fadeRGB\' takes 2 params'
	name = parse(params[0])
	colorName = parse(params[1])
	duration = parse(params[2])
	return proxy.fadeRGB(name,colorName,duration)

def fadeRGB(params):
	if len(params) < 3:
		print 'Error: function \'fadeRGB\' takes 2 params'
		return 'Error: function \'fadeRGB\' takes 2 params'
	name = parse(params[0])
	rgb = parse(params[1])
	duration = parse(params[2])
	return proxy.fadeRGB(name,rgb,duration)

def getIntensity(params):
	if len(params) < 1:
		print 'Error: function \'getIntensity\' takes 2 params'
		return 'Error: function \'getIntensity\' takes 2 params'
	name = parse(params[0])
	return proxy.getIntensity(name)

def listGroup(params):
	if len(params) < 1:
		print 'Error: function \'listGroup\' takes 2 params'
		return 'Error: function \'listGroup\' takes 2 params'
	groupName = parse(params[0])
	return proxy.listGroup(groupName)

def listGroups(params):
	return proxy.listGroups()

def listLED(params):
	if len(params) < 1:
		print 'Error: function \'listLED\' takes 2 params'
		return 'Error: function \'listLED\' takes 2 params'
	arg1 = parse(params[0])
	return proxy.listLED(arg1)

def listLEDs(params):
	return proxy.listLEDs()

def off(params):
	if len(params) < 1:
		print 'Error: function \'off\' takes 2 params'
		return 'Error: function \'off\' takes 2 params'
	name = parse(params[0])
	return proxy.off(name)

def on(params):
	if len(params) < 1:
		print 'Error: function \'on\' takes 2 params'
		return 'Error: function \'on\' takes 2 params'
	name = parse(params[0])
	return proxy.on(name)

def randomEyes(params):
	if len(params) < 1:
		print 'Error: function \'randomEyes\' takes 2 params'
		return 'Error: function \'randomEyes\' takes 2 params'
	duration = parse(params[0])
	return proxy.randomEyes(duration)

def rasta(params):
	if len(params) < 1:
		print 'Error: function \'rasta\' takes 2 params'
		return 'Error: function \'rasta\' takes 2 params'
	duration = parse(params[0])
	return proxy.rasta(duration)

def reset(params):
	if len(params) < 1:
		print 'Error: function \'reset\' takes 2 params'
		return 'Error: function \'reset\' takes 2 params'
	name = parse(params[0])
	return proxy.reset(name)

def rotateEyes(params):
	if len(params) < 3:
		print 'Error: function \'rotateEyes\' takes 2 params'
		return 'Error: function \'rotateEyes\' takes 2 params'
	rgb = parse(params[0])
	timeForRotation = parse(params[1])
	totalDuration = parse(params[2])
	return proxy.rotateEyes(rgb,timeForRotation,totalDuration)

def setIntensity(params):
	if len(params) < 2:
		print 'Error: function \'setIntensity\' takes 2 params'
		return 'Error: function \'setIntensity\' takes 2 params'
	name = parse(params[0])
	intensity = parse(params[1])
	return proxy.setIntensity(name,intensity)

