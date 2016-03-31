from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALInfrared', '127.0.0.1', PORT)

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

def initReception(params):
	if len(params) < 1:
		print 'Error: function \'initReception\' takes 2 params'
		return 'Error: function \'initReception\' takes 2 params'
	RepeatThreshold = parse(params[0])
	return proxy.initReception(RepeatThreshold)

def send32(params):
	if len(params) < 1:
		print 'Error: function \'send32\' takes 2 params'
		return 'Error: function \'send32\' takes 2 params'
	Data_IR = parse(params[0])
	return proxy.send32(Data_IR)

def send32(params):
	if len(params) < 4:
		print 'Error: function \'send32\' takes 2 params'
		return 'Error: function \'send32\' takes 2 params'
	Byte1 = parse(params[0])
	Byte2 = parse(params[1])
	Byte3 = parse(params[2])
	Byte4 = parse(params[3])
	return proxy.send32(Byte1,Byte2,Byte3,Byte4)

def send8(params):
	if len(params) < 1:
		print 'Error: function \'send8\' takes 2 params'
		return 'Error: function \'send8\' takes 2 params'
	Byte = parse(params[0])
	return proxy.send8(Byte)

def sendIpAddress(params):
	if len(params) < 1:
		print 'Error: function \'sendIpAddress\' takes 2 params'
		return 'Error: function \'sendIpAddress\' takes 2 params'
	IP = parse(params[0])
	return proxy.sendIpAddress(IP)

def sendRemoteKey(params):
	if len(params) < 2:
		print 'Error: function \'sendRemoteKey\' takes 2 params'
		return 'Error: function \'sendRemoteKey\' takes 2 params'
	Remote = parse(params[0])
	Key = parse(params[1])
	return proxy.sendRemoteKey(Remote,Key)

def sendRemoteKeyWithTime(params):
	if len(params) < 3:
		print 'Error: function \'sendRemoteKeyWithTime\' takes 2 params'
		return 'Error: function \'sendRemoteKeyWithTime\' takes 2 params'
	Remote = parse(params[0])
	Key = parse(params[1])
	TimeMs = parse(params[2])
	return proxy.sendRemoteKeyWithTime(Remote,Key,TimeMs)

def confRemoteRecordSave(params):
	if len(params) < 1:
		print 'Error: function \'confRemoteRecordSave\' takes 2 params'
		return 'Error: function \'confRemoteRecordSave\' takes 2 params'
	void = parse(params[0])
	return proxy.confRemoteRecordSave(void)

