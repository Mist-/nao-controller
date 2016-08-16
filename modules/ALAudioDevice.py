from naoqi import ALProxy
from network.const import PORT, IP
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALAudioDevice', IP, PORT)

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

def disableEnergyComputation(params):
	return proxy.disableEnergyComputation()

def enableEnergyComputation(params):
	return proxy.enableEnergyComputation()

def flushAudioOutputs(params):
	return proxy.flushAudioOutputs()

def getFrontMicEnergy(params):
	return proxy.getFrontMicEnergy()

def getLeftMicEnergy(params):
	return proxy.getLeftMicEnergy()

def getOutputVolume(params):
	return proxy.getOutputVolume()

def getParameter(params):
	if len(params) < 1:
		print 'Error: function \'getParameter\' takes 2 params'
		return 'Error: function \'getParameter\' takes 2 params'
	parameter = parse(params[0])
	return proxy.getParameter(parameter)

def getRearMicEnergy(params):
	return proxy.getRearMicEnergy()

def getRightMicEnergy(params):
	return proxy.getRightMicEnergy()

def isAudioOutMuted(params):
	return proxy.isAudioOutMuted()

def muteAudioOut(params):
	if len(params) < 1:
		print 'Error: function \'muteAudioOut\' takes 2 params'
		return 'Error: function \'muteAudioOut\' takes 2 params'
	mute = parse(params[0])
	return proxy.muteAudioOut(mute)

def openAudioInputs(params):
	return proxy.openAudioInputs()

def openAudioOutputs(params):
	return proxy.openAudioOutputs()

def playSine(params):
	if len(params) < 4:
		print 'Error: function \'playSine\' takes 2 params'
		return 'Error: function \'playSine\' takes 2 params'
	frequence = parse(params[0])
	gain = parse(params[1])
	pan = parse(params[2])
	duration = parse(params[3])
	return proxy.playSine(frequence,gain,pan,duration)

def sendLocalBufferToOutput(params):
	if len(params) < 2:
		print 'Error: function \'sendLocalBufferToOutput\' takes 2 params'
		return 'Error: function \'sendLocalBufferToOutput\' takes 2 params'
	nbOfFrames = parse(params[0])
	buffer = parse(params[1])
	return proxy.sendLocalBufferToOutput(nbOfFrames,buffer)

def sendRemoteBufferToOutput(params):
	if len(params) < 2:
		print 'Error: function \'sendRemoteBufferToOutput\' takes 2 params'
		return 'Error: function \'sendRemoteBufferToOutput\' takes 2 params'
	nbOfFrames = parse(params[0])
	buffer = parse(params[1])
	return proxy.sendRemoteBufferToOutput(nbOfFrames,buffer)

def setClientPreferences(params):
	if len(params) < 4:
		print 'Error: function \'setClientPreferences\' takes 2 params'
		return 'Error: function \'setClientPreferences\' takes 2 params'
	name = parse(params[0])
	sampleRate = parse(params[1])
	channels = parse(params[2])
	deinterleaved = parse(params[3])
	return proxy.setClientPreferences(name,sampleRate,channels,deinterleaved)

def setFileAsInput(params):
	if len(params) < 1:
		print 'Error: function \'setFileAsInput\' takes 2 params'
		return 'Error: function \'setFileAsInput\' takes 2 params'
	fileName = parse(params[0])
	return proxy.setFileAsInput(fileName)

def setOutputVolume(params):
	if len(params) < 1:
		print 'Error: function \'setOutputVolume\' takes 2 params'
		return 'Error: function \'setOutputVolume\' takes 2 params'
	volume = parse(params[0])
	return proxy.setOutputVolume(volume)

def setParameter(params):
	if len(params) < 2:
		print 'Error: function \'setParameter\' takes 2 params'
		return 'Error: function \'setParameter\' takes 2 params'
	parameter = parse(params[0])
	value = parse(params[1])
	return proxy.setParameter(parameter,value)

def startMicrophonesRecording(params):
	if len(params) < 1:
		print 'Error: function \'startMicrophonesRecording\' takes 2 params'
		return 'Error: function \'startMicrophonesRecording\' takes 2 params'
	fileName = parse(params[0])
	return proxy.startMicrophonesRecording(fileName)

def stopMicrophonesRecording(params):
	return proxy.stopMicrophonesRecording()

def subscribe(params):
	if len(params) < 1:
		print 'Error: function \'subscribe\' takes 2 params'
		return 'Error: function \'subscribe\' takes 2 params'
	module = parse(params[0])
	return proxy.subscribe(module)

def unsubscribe(params):
	if len(params) < 1:
		print 'Error: function \'unsubscribe\' takes 2 params'
		return 'Error: function \'unsubscribe\' takes 2 params'
	module = parse(params[0])
	return proxy.unsubscribe(module)

def closeAudioInputs(params):
	return proxy.closeAudioInputs()

def closeAudioOutputs(params):
	return proxy.closeAudioOutputs()

def isInputClosed(params):
	return proxy.isInputClosed()

def isOutputClosed(params):
	return proxy.isOutputClosed()

