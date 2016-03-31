from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALTextToSpeech', '127.0.0.1', PORT)

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

def disableNotifications(params):
	return proxy.disableNotifications()

def enableNotifications(params):
	return proxy.enableNotifications()

def getAvailableLanguages(params):
	return proxy.getAvailableLanguages()

def getAvailableVoices(params):
	return proxy.getAvailableVoices()

def getLanguage(params):
	return proxy.getLanguage()

def getParameter(params):
	if len(params) < 1:
		print 'Error: function \'getParameter\' takes 2 params'
		return 'Error: function \'getParameter\' takes 2 params'
	parameter = parse(params[0])
	return proxy.getParameter(parameter)

def getSupportedLanguages(params):
	return proxy.getSupportedLanguages()

def getVoice(params):
	return proxy.getVoice()

def getVolume(params):
	return proxy.getVolume()

def loadVoicePreference(params):
	if len(params) < 1:
		print 'Error: function \'loadVoicePreference\' takes 2 params'
		return 'Error: function \'loadVoicePreference\' takes 2 params'
	preferencesFileSuffix = parse(params[0])
	return proxy.loadVoicePreference(preferencesFileSuffix)

def locale(params):
	return proxy.locale()

def say(params):
	if len(params) < 1:
		print 'Error: function \'say\' takes 2 params'
		return 'Error: function \'say\' takes 2 params'
	stringToSay = parse(params[0])
	return proxy.say(stringToSay)

def say(params):
	if len(params) < 2:
		print 'Error: function \'say\' takes 2 params'
		return 'Error: function \'say\' takes 2 params'
	stringToSay = parse(params[0])
	language = parse(params[1])
	return proxy.say(stringToSay,language)

def sayToFile(params):
	if len(params) < 2:
		print 'Error: function \'sayToFile\' takes 2 params'
		return 'Error: function \'sayToFile\' takes 2 params'
	stringToSay = parse(params[0])
	fileName = parse(params[1])
	return proxy.sayToFile(stringToSay,fileName)

def sayToFileAndPlay(params):
	if len(params) < 1:
		print 'Error: function \'sayToFileAndPlay\' takes 2 params'
		return 'Error: function \'sayToFileAndPlay\' takes 2 params'
	stringToSay = parse(params[0])
	return proxy.sayToFileAndPlay(stringToSay)

def setLanguage(params):
	if len(params) < 1:
		print 'Error: function \'setLanguage\' takes 2 params'
		return 'Error: function \'setLanguage\' takes 2 params'
	language = parse(params[0])
	return proxy.setLanguage(language)

def setLanguageDefaultVoice(params):
	if len(params) < 2:
		print 'Error: function \'setLanguageDefaultVoice\' takes 2 params'
		return 'Error: function \'setLanguageDefaultVoice\' takes 2 params'
	language = parse(params[0])
	voice = parse(params[1])
	return proxy.setLanguageDefaultVoice(language,voice)

def setParameter(params):
	if len(params) < 2:
		print 'Error: function \'setParameter\' takes 2 params'
		return 'Error: function \'setParameter\' takes 2 params'
	parameter = parse(params[0])
	value = parse(params[1])
	return proxy.setParameter(parameter,value)

def setVoice(params):
	if len(params) < 1:
		print 'Error: function \'setVoice\' takes 2 params'
		return 'Error: function \'setVoice\' takes 2 params'
	voiceID = parse(params[0])
	return proxy.setVoice(voiceID)

def setVolume(params):
	if len(params) < 1:
		print 'Error: function \'setVolume\' takes 2 params'
		return 'Error: function \'setVolume\' takes 2 params'
	volume = parse(params[0])
	return proxy.setVolume(volume)

def stopAll(params):
	return proxy.stopAll()

def getLanguageEncoding(params):
	if len(params) < 1:
		print 'Error: function \'getLanguageEncoding\' takes 2 params'
		return 'Error: function \'getLanguageEncoding\' takes 2 params'
	languageName = parse(params[0])
	return proxy.getLanguageEncoding(languageName)

