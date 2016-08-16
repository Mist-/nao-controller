from naoqi import ALProxy
from network.const import PORT, IP
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALAnimatedSpeech', IP, PORT)

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

def say(params):
	if len(params) < 1:
		print 'Error: function \'say\' takes 2 params'
		return 'Error: function \'say\' takes 2 params'
	text = parse(params[0])
	return proxy.say(text)

def say(params):
	if len(params) < 2:
		print 'Error: function \'say\' takes 2 params'
		return 'Error: function \'say\' takes 2 params'
	text = parse(params[0])
	configuration = parse(params[1])
	return proxy.say(text,configuration)

def setBodyLanguageMode(params):
	if len(params) < 1:
		print 'Error: function \'setBodyLanguageMode\' takes 2 params'
		return 'Error: function \'setBodyLanguageMode\' takes 2 params'
	bodyLanguageMode = parse(params[0])
	return proxy.setBodyLanguageMode(bodyLanguageMode)

def setBodyLanguageModeFromStr(params):
	if len(params) < 1:
		print 'Error: function \'setBodyLanguageModeFromStr\' takes 2 params'
		return 'Error: function \'setBodyLanguageModeFromStr\' takes 2 params'
	stringBodyLanguageMode = parse(params[0])
	return proxy.setBodyLanguageModeFromStr(stringBodyLanguageMode)

def getBodyLanguageMode(params):
	return proxy.getBodyLanguageMode()

def getBodyLanguageModeToStr(params):
	return proxy.getBodyLanguageModeToStr()

def addTagsToWords(params):
	if len(params) < 1:
		print 'Error: function \'addTagsToWords\' takes 2 params'
		return 'Error: function \'addTagsToWords\' takes 2 params'
	tagsToWords = parse(params[0])
	return proxy.addTagsToWords(tagsToWords)

def declareAnimationsPackage(params):
	if len(params) < 1:
		print 'Error: function \'declareAnimationsPackage\' takes 2 params'
		return 'Error: function \'declareAnimationsPackage\' takes 2 params'
	animationsPackage = parse(params[0])
	return proxy.declareAnimationsPackage(animationsPackage)

def declareTagForAnimations(params):
	if len(params) < 1:
		print 'Error: function \'declareTagForAnimations\' takes 2 params'
		return 'Error: function \'declareTagForAnimations\' takes 2 params'
	tagsToAnimations = parse(params[0])
	return proxy.declareTagForAnimations(tagsToAnimations)

def setBodyLanguageEnabled(params):
	if len(params) < 1:
		print 'Error: function \'setBodyLanguageEnabled\' takes 2 params'
		return 'Error: function \'setBodyLanguageEnabled\' takes 2 params'
	enable = parse(params[0])
	return proxy.setBodyLanguageEnabled(enable)

def isBodyLanguageEnabled(params):
	return proxy.isBodyLanguageEnabled()

def setBodyTalkEnabled(params):
	if len(params) < 1:
		print 'Error: function \'setBodyTalkEnabled\' takes 2 params'
		return 'Error: function \'setBodyTalkEnabled\' takes 2 params'
	enable = parse(params[0])
	return proxy.setBodyTalkEnabled(enable)

def isBodyTalkEnabled(params):
	return proxy.isBodyTalkEnabled()
