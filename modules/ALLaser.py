from naoqi import ALProxy
from network.const import PORT, IP
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALLaser', IP, PORT)

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

def laserOFF(params):
	return proxy.laserOFF()

def laserON(params):
	return proxy.laserON()

def setDetectingLength(params):
	if len(params) < 2:
		print 'Error: function \'setDetectingLength\' takes 2 params'
		return 'Error: function \'setDetectingLength\' takes 2 params'
	length_min_l = parse(params[0])
	length_max_l = parse(params[1])
	return proxy.setDetectingLength(length_min_l,length_max_l)

def setOpeningAngle(params):
	if len(params) < 2:
		print 'Error: function \'setOpeningAngle\' takes 2 params'
		return 'Error: function \'setOpeningAngle\' takes 2 params'
	angle_min_f = parse(params[0])
	angle_max_f = parse(params[1])
	return proxy.setOpeningAngle(angle_min_f,angle_max_f)

