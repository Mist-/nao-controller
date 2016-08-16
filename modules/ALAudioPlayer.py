from naoqi import ALProxy
from network.const import PORT, IP
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALAudioPlayer', IP, PORT)

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

def getCurrentPosition(params):
	if len(params) < 1:
		print 'Error: function \'getCurrentPosition\' takes 2 params'
		return 'Error: function \'getCurrentPosition\' takes 2 params'
	taskId = parse(params[0])
	return proxy.getCurrentPosition(taskId)

def getFileLength(params):
	if len(params) < 1:
		print 'Error: function \'getFileLength\' takes 2 params'
		return 'Error: function \'getFileLength\' takes 2 params'
	taskId = parse(params[0])
	return proxy.getFileLength(taskId)

def getInstalledSoundSetsList(params):
	return proxy.getInstalledSoundSetsList()

def getLoadedFilesIds(params):
	return proxy.getLoadedFilesIds()

def getLoadedFilesNames(params):
	return proxy.getLoadedFilesNames()

def getLoadedSoundSetsList(params):
	return proxy.getLoadedSoundSetsList()

def getSoundSetFileNames(params):
	if len(params) < 1:
		print 'Error: function \'getSoundSetFileNames\' takes 2 params'
		return 'Error: function \'getSoundSetFileNames\' takes 2 params'
	setName = parse(params[0])
	return proxy.getSoundSetFileNames(setName)

def getMasterVolume(params):
	return proxy.getMasterVolume()

def getVolume(params):
	if len(params) < 1:
		print 'Error: function \'getVolume\' takes 2 params'
		return 'Error: function \'getVolume\' takes 2 params'
	taskId = parse(params[0])
	return proxy.getVolume(taskId)

def goTo(params):
	if len(params) < 2:
		print 'Error: function \'goTo\' takes 2 params'
		return 'Error: function \'goTo\' takes 2 params'
	taskId = parse(params[0])
	position = parse(params[1])
	return proxy.goTo(taskId,position)

def isSoundSetFileInstalled(params):
	if len(params) < 2:
		print 'Error: function \'isSoundSetFileInstalled\' takes 2 params'
		return 'Error: function \'isSoundSetFileInstalled\' takes 2 params'
	soundSet = parse(params[0])
	soundSetFile = parse(params[1])
	return proxy.isSoundSetFileInstalled(soundSet,soundSetFile)

def isSoundSetInstalled(params):
	if len(params) < 1:
		print 'Error: function \'isSoundSetInstalled\' takes 2 params'
		return 'Error: function \'isSoundSetInstalled\' takes 2 params'
	soundSet = parse(params[0])
	return proxy.isSoundSetInstalled(soundSet)

def isSoundSetLoaded(params):
	if len(params) < 1:
		print 'Error: function \'isSoundSetLoaded\' takes 2 params'
		return 'Error: function \'isSoundSetLoaded\' takes 2 params'
	soundSet = parse(params[0])
	return proxy.isSoundSetLoaded(soundSet)

def loadFile(params):
	if len(params) < 1:
		print 'Error: function \'loadFile\' takes 2 params'
		return 'Error: function \'loadFile\' takes 2 params'
	fileName = parse(params[0])
	return proxy.loadFile(fileName)

def loadSoundSet(params):
	if len(params) < 1:
		print 'Error: function \'loadSoundSet\' takes 2 params'
		return 'Error: function \'loadSoundSet\' takes 2 params'
	setName = parse(params[0])
	return proxy.loadSoundSet(setName)

def pause(params):
	if len(params) < 1:
		print 'Error: function \'pause\' takes 2 params'
		return 'Error: function \'pause\' takes 2 params'
	taskId = parse(params[0])
	return proxy.pause(taskId)

def play(params):
	if len(params) < 1:
		print 'Error: function \'play\' takes 2 params'
		return 'Error: function \'play\' takes 2 params'
	taskId = parse(params[0])
	return proxy.play(taskId)

def play(params):
	if len(params) < 3:
		print 'Error: function \'play\' takes 2 params'
		return 'Error: function \'play\' takes 2 params'
	taskId = parse(params[0])
	volume = parse(params[1])
	pan = parse(params[2])
	return proxy.play(taskId,volume,pan)

def playFile(params):
	if len(params) < 1:
		print 'Error: function \'playFile\' takes 2 params'
		return 'Error: function \'playFile\' takes 2 params'
	fileName = parse(params[0])
	return proxy.playFile(fileName)

def playFile(params):
	if len(params) < 3:
		print 'Error: function \'playFile\' takes 2 params'
		return 'Error: function \'playFile\' takes 2 params'
	fileName = parse(params[0])
	volume = parse(params[1])
	pan = parse(params[2])
	return proxy.playFile(fileName,volume,pan)

def playFileFromPosition(params):
	if len(params) < 2:
		print 'Error: function \'playFileFromPosition\' takes 2 params'
		return 'Error: function \'playFileFromPosition\' takes 2 params'
	fileName = parse(params[0])
	position = parse(params[1])
	return proxy.playFileFromPosition(fileName,position)

def playFileFromPosition(params):
	if len(params) < 4:
		print 'Error: function \'playFileFromPosition\' takes 2 params'
		return 'Error: function \'playFileFromPosition\' takes 2 params'
	fileName = parse(params[0])
	position = parse(params[1])
	volume = parse(params[2])
	pan = parse(params[3])
	return proxy.playFileFromPosition(fileName,position,volume,pan)

def playFileInLoop(params):
	if len(params) < 1:
		print 'Error: function \'playFileInLoop\' takes 2 params'
		return 'Error: function \'playFileInLoop\' takes 2 params'
	fileName = parse(params[0])
	return proxy.playFileInLoop(fileName)

def playFileInLoop(params):
	if len(params) < 3:
		print 'Error: function \'playFileInLoop\' takes 2 params'
		return 'Error: function \'playFileInLoop\' takes 2 params'
	fileName = parse(params[0])
	volume = parse(params[1])
	pan = parse(params[2])
	return proxy.playFileInLoop(fileName,volume,pan)

def playInLoop(params):
	if len(params) < 1:
		print 'Error: function \'playInLoop\' takes 2 params'
		return 'Error: function \'playInLoop\' takes 2 params'
	taskId = parse(params[0])
	return proxy.playInLoop(taskId)

def playInLoop(params):
	if len(params) < 3:
		print 'Error: function \'playInLoop\' takes 2 params'
		return 'Error: function \'playInLoop\' takes 2 params'
	taskId = parse(params[0])
	volume = parse(params[1])
	pan = parse(params[2])
	return proxy.playInLoop(taskId,volume,pan)

def playSine(params):
	if len(params) < 4:
		print 'Error: function \'playSine\' takes 2 params'
		return 'Error: function \'playSine\' takes 2 params'
	frequence = parse(params[0])
	gain = parse(params[1])
	pan = parse(params[2])
	duration = parse(params[3])
	return proxy.playSine(frequence,gain,pan,duration)

def playSoundSetFile(params):
	if len(params) < 1:
		print 'Error: function \'playSoundSetFile\' takes 2 params'
		return 'Error: function \'playSoundSetFile\' takes 2 params'
	fileName = parse(params[0])
	return proxy.playSoundSetFile(fileName)

def playSoundSetFile(params):
	if len(params) < 2:
		print 'Error: function \'playSoundSetFile\' takes 2 params'
		return 'Error: function \'playSoundSetFile\' takes 2 params'
	soundSetName = parse(params[0])
	fileName = parse(params[1])
	return proxy.playSoundSetFile(soundSetName,fileName)

def playSoundSetFile(params):
	if len(params) < 6:
		print 'Error: function \'playSoundSetFile\' takes 2 params'
		return 'Error: function \'playSoundSetFile\' takes 2 params'
	soundSetName = parse(params[0])
	fileName = parse(params[1])
	position = parse(params[2])
	volume = parse(params[3])
	pan = parse(params[4])
	loop = parse(params[5])
	return proxy.playSoundSetFile(soundSetName,fileName,position,volume,pan,loop)

def playWebStream(params):
	if len(params) < 3:
		print 'Error: function \'playWebStream\' takes 2 params'
		return 'Error: function \'playWebStream\' takes 2 params'
	streamName = parse(params[0])
	volume = parse(params[1])
	pan = parse(params[2])
	return proxy.playWebStream(streamName,volume,pan)

def setMasterVolume(params):
	if len(params) < 1:
		print 'Error: function \'setMasterVolume\' takes 2 params'
		return 'Error: function \'setMasterVolume\' takes 2 params'
	volume = parse(params[0])
	return proxy.setMasterVolume(volume)

def setPanorama(params):
	if len(params) < 1:
		print 'Error: function \'setPanorama\' takes 2 params'
		return 'Error: function \'setPanorama\' takes 2 params'
	pan = parse(params[0])
	return proxy.setPanorama(pan)

def setVolume(params):
	if len(params) < 2:
		print 'Error: function \'setVolume\' takes 2 params'
		return 'Error: function \'setVolume\' takes 2 params'
	taskId = parse(params[0])
	volume = parse(params[1])
	return proxy.setVolume(taskId,volume)

def stopAll(params):
	return proxy.stopAll()

def unloadAllFiles(params):
	return proxy.unloadAllFiles()

def unloadFile(params):
	if len(params) < 1:
		print 'Error: function \'unloadFile\' takes 2 params'
		return 'Error: function \'unloadFile\' takes 2 params'
	taskId = parse(params[0])
	return proxy.unloadFile(taskId)

def unloadSoundSet(params):
	if len(params) < 1:
		print 'Error: function \'unloadSoundSet\' takes 2 params'
		return 'Error: function \'unloadSoundSet\' takes 2 params'
	setName = parse(params[0])
	return proxy.unloadSoundSet(setName)

