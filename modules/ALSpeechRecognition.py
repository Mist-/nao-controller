from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALSpeechRecognition', '127.0.0.1', PORT)

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

def getAvailableLanguages(params):
	return proxy.getAvailableLanguages()

def getLanguage(params):
	return proxy.getLanguage()

def setLanguage(params):
	if len(params) < 1:
		print 'Error: function \'setLanguage\' takes 2 params'
		return 'Error: function \'setLanguage\' takes 2 params'
	language = parse(params[0])
	return proxy.setLanguage(language)

def getParameter(params):
	if len(params) < 1:
		print 'Error: function \'getParameter\' takes 2 params'
		return 'Error: function \'getParameter\' takes 2 params'
	parameter = parse(params[0])
	return proxy.getParameter(parameter)

def setParameter(params):
	if len(params) < 2:
		print 'Error: function \'setParameter\' takes 2 params'
		return 'Error: function \'setParameter\' takes 2 params'
	parameter = parse(params[0])
	value = parse(params[1])
	return proxy.setParameter(parameter,value)

def loadVocabulary(params):
	if len(params) < 1:
		print 'Error: function \'loadVocabulary\' takes 2 params'
		return 'Error: function \'loadVocabulary\' takes 2 params'
	pathToGrammarfile = parse(params[0])
	return proxy.loadVocabulary(pathToGrammarfile)

def getAudioExpression(params):
	return proxy.getAudioExpression()

def setAudioExpression(params):
	if len(params) < 1:
		print 'Error: function \'setAudioExpression\' takes 2 params'
		return 'Error: function \'setAudioExpression\' takes 2 params'
	setOrNot = parse(params[0])
	return proxy.setAudioExpression(setOrNot)

def setVisualExpression(params):
	if len(params) < 1:
		print 'Error: function \'setVisualExpression\' takes 2 params'
		return 'Error: function \'setVisualExpression\' takes 2 params'
	setOrNot = parse(params[0])
	return proxy.setVisualExpression(setOrNot)

def setVocabulary(params):
	if len(params) < 2:
		print 'Error: function \'setVocabulary\' takes 2 params'
		return 'Error: function \'setVocabulary\' takes 2 params'
	vocabulary = parse(params[0])
	enableWordSpotting = parse(params[1])
	return proxy.setVocabulary(vocabulary,enableWordSpotting)

def setWordListAsVocabulary(params):
	if len(params) < 1:
		print 'Error: function \'setWordListAsVocabulary\' takes 2 params'
		return 'Error: function \'setWordListAsVocabulary\' takes 2 params'
	vocabulary = parse(params[0])
	return proxy.setWordListAsVocabulary(vocabulary)

def compile(params):
	if len(params) < 3:
		print 'Error: function \'compile\' takes 2 params'
		return 'Error: function \'compile\' takes 2 params'
	pathToInputBNFFile = parse(params[0])
	pathToOutputLCFFile = parse(params[1])
	language = parse(params[2])
	return proxy.compile(pathToInputBNFFile,pathToOutputLCFFile,language)

def addContext(params):
	if len(params) < 2:
		print 'Error: function \'addContext\' takes 2 params'
		return 'Error: function \'addContext\' takes 2 params'
	pathToLCFFile = parse(params[0])
	contextName = parse(params[1])
	return proxy.addContext(pathToLCFFile,contextName)

def removeContext(params):
	if len(params) < 1:
		print 'Error: function \'removeContext\' takes 2 params'
		return 'Error: function \'removeContext\' takes 2 params'
	contextName = parse(params[0])
	return proxy.removeContext(contextName)

def removeAllContext(params):
	return proxy.removeAllContext()

def saveContextSet(params):
	if len(params) < 1:
		print 'Error: function \'saveContextSet\' takes 2 params'
		return 'Error: function \'saveContextSet\' takes 2 params'
	saveName = parse(params[0])
	return proxy.saveContextSet(saveName)

def loadContextSet(params):
	if len(params) < 1:
		print 'Error: function \'loadContextSet\' takes 2 params'
		return 'Error: function \'loadContextSet\' takes 2 params'
	saveName = parse(params[0])
	return proxy.loadContextSet(saveName)

def eraseContextSet(params):
	if len(params) < 1:
		print 'Error: function \'eraseContextSet\' takes 2 params'
		return 'Error: function \'eraseContextSet\' takes 2 params'
	saveName = parse(params[0])
	return proxy.eraseContextSet(saveName)

def activateRule(params):
	if len(params) < 2:
		print 'Error: function \'activateRule\' takes 2 params'
		return 'Error: function \'activateRule\' takes 2 params'
	contextName = parse(params[0])
	ruleName = parse(params[1])
	return proxy.activateRule(contextName,ruleName)

def deactivateRule(params):
	if len(params) < 2:
		print 'Error: function \'deactivateRule\' takes 2 params'
		return 'Error: function \'deactivateRule\' takes 2 params'
	contextName = parse(params[0])
	ruleName = parse(params[1])
	return proxy.deactivateRule(contextName,ruleName)

def activateAllRules(params):
	if len(params) < 1:
		print 'Error: function \'activateAllRules\' takes 2 params'
		return 'Error: function \'activateAllRules\' takes 2 params'
	contextName = parse(params[0])
	return proxy.activateAllRules(contextName)

def deactivateAllRules(params):
	if len(params) < 1:
		print 'Error: function \'deactivateAllRules\' takes 2 params'
		return 'Error: function \'deactivateAllRules\' takes 2 params'
	contextName = parse(params[0])
	return proxy.deactivateAllRules(contextName)

def addWordListToSlot(params):
	if len(params) < 3:
		print 'Error: function \'addWordListToSlot\' takes 2 params'
		return 'Error: function \'addWordListToSlot\' takes 2 params'
	contextName = parse(params[0])
	slotName = parse(params[1])
	wordList = parse(params[2])
	return proxy.addWordListToSlot(contextName,slotName,wordList)

def removeWordListFromSlot(params):
	if len(params) < 2:
		print 'Error: function \'removeWordListFromSlot\' takes 2 params'
		return 'Error: function \'removeWordListFromSlot\' takes 2 params'
	contextName = parse(params[0])
	slotName = parse(params[1])
	return proxy.removeWordListFromSlot(contextName,slotName)

def getRules(params):
	if len(params) < 2:
		print 'Error: function \'getRules\' takes 2 params'
		return 'Error: function \'getRules\' takes 2 params'
	contextName = parse(params[0])
	typeName = parse(params[1])
	return proxy.getRules(contextName,typeName)

def pause(params):
	if len(params) < 1:
		print 'Error: function \'pause\' takes 2 params'
		return 'Error: function \'pause\' takes 2 params'
	isPaused = parse(params[0])
	return proxy.pause(isPaused)

def subscribe(params):
	if len(params) < 1:
		print 'Error: function \'subscribe\' takes 2 params'
		return 'Error: function \'subscribe\' takes 2 params'
	name = parse(params[0])
	return proxy.subscribe(name)

def unsubscribe(params):
	if len(params) < 1:
		print 'Error: function \'unsubscribe\' takes 2 params'
		return 'Error: function \'unsubscribe\' takes 2 params'
	name = parse(params[0])
	return proxy.unsubscribe(name)

