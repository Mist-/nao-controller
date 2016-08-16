from naoqi import ALProxy
from network.const import PORT, IP
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALAudioRecorder', IP, PORT)

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

def startMicrophonesRecording(params):
	if len(params) < 4:
		print 'Error: function \'startMicrophonesRecording\' takes 2 params'
		return 'Error: function \'startMicrophonesRecording\' takes 2 params'
	filename = parse(params[0])
	type = parse(params[1])
	samplerate = parse(params[2])
	channels = parse(params[3])
	return proxy.startMicrophonesRecording(filename,type,samplerate,channels)

def stopMicrophonesRecording(params):
	return proxy.stopMicrophonesRecording()

