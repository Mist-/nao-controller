from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALDialog', '127.0.0.1', PORT)

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

def loadTopic(params):
	if len(params) < 1:
		print 'Error: function \'loadTopic\' takes 2 params'
		return 'Error: function \'loadTopic\' takes 2 params'
	topicPath = parse(params[0])
	return proxy.loadTopic(topicPath)

def unloadTopic(params):
	if len(params) < 1:
		print 'Error: function \'unloadTopic\' takes 2 params'
		return 'Error: function \'unloadTopic\' takes 2 params'
	topicName = parse(params[0])
	return proxy.unloadTopic(topicName)

def activateTopic(params):
	if len(params) < 1:
		print 'Error: function \'activateTopic\' takes 2 params'
		return 'Error: function \'activateTopic\' takes 2 params'
	topicName = parse(params[0])
	return proxy.activateTopic(topicName)

def deactivateTopic(params):
	if len(params) < 1:
		print 'Error: function \'deactivateTopic\' takes 2 params'
		return 'Error: function \'deactivateTopic\' takes 2 params'
	topicName = parse(params[0])
	return proxy.deactivateTopic(topicName)

def setLanguage(params):
	if len(params) < 1:
		print 'Error: function \'setLanguage\' takes 2 params'
		return 'Error: function \'setLanguage\' takes 2 params'
	language = parse(params[0])
	return proxy.setLanguage(language)

def setFocus(params):
	if len(params) < 1:
		print 'Error: function \'setFocus\' takes 2 params'
		return 'Error: function \'setFocus\' takes 2 params'
	topicName = parse(params[0])
	return proxy.setFocus(topicName)

def activateTag(params):
	if len(params) < 2:
		print 'Error: function \'activateTag\' takes 2 params'
		return 'Error: function \'activateTag\' takes 2 params'
	tagName = parse(params[0])
	topicName = parse(params[1])
	return proxy.activateTag(tagName,topicName)

def deactivateTag(params):
	if len(params) < 2:
		print 'Error: function \'deactivateTag\' takes 2 params'
		return 'Error: function \'deactivateTag\' takes 2 params'
	tagName = parse(params[0])
	topicName = parse(params[1])
	return proxy.deactivateTag(tagName,topicName)

def gotoTopic(params):
	if len(params) < 1:
		print 'Error: function \'gotoTopic\' takes 2 params'
		return 'Error: function \'gotoTopic\' takes 2 params'
	topicName = parse(params[0])
	return proxy.gotoTopic(topicName)

def setConcept(params):
	if len(params) < 3:
		print 'Error: function \'setConcept\' takes 2 params'
		return 'Error: function \'setConcept\' takes 2 params'
	conceptName = parse(params[0])
	language = parse(params[1])
	content = parse(params[2])
	return proxy.setConcept(conceptName,language,content)

def setAnimatedSpeechConfiguration(params):
	if len(params) < 1:
		print 'Error: function \'setAnimatedSpeechConfiguration\' takes 2 params'
		return 'Error: function \'setAnimatedSpeechConfiguration\' takes 2 params'
	animatedSpeechConfiguration = parse(params[0])
	return proxy.setAnimatedSpeechConfiguration(animatedSpeechConfiguration)

def setASRConfidenceThreshold(params):
	if len(params) < 1:
		print 'Error: function \'setASRConfidenceThreshold\' takes 2 params'
		return 'Error: function \'setASRConfidenceThreshold\' takes 2 params'
	threshold = parse(params[0])
	return proxy.setASRConfidenceThreshold(threshold)

def getASRConfidenceThreshold(params):
	return proxy.getASRConfidenceThreshold()

def forceOutput(params):
	return proxy.forceOutput()

def forceInput(params):
	if len(params) < 1:
		print 'Error: function \'forceInput\' takes 2 params'
		return 'Error: function \'forceInput\' takes 2 params'
	input = parse(params[0])
	return proxy.forceInput(input)

def getLoadedTopics(params):
	if len(params) < 1:
		print 'Error: function \'getLoadedTopics\' takes 2 params'
		return 'Error: function \'getLoadedTopics\' takes 2 params'
	language = parse(params[0])
	return proxy.getLoadedTopics(language)

def getActivatedTopics(params):
	return proxy.getActivatedTopics()

def setVariablePath(params):
	if len(params) < 3:
		print 'Error: function \'setVariablePath\' takes 2 params'
		return 'Error: function \'setVariablePath\' takes 2 params'
	topicName = parse(params[0])
	eventName = parse(params[1])
	path = parse(params[2])
	return proxy.setVariablePath(topicName,eventName,path)

def getUserList(params):
	return proxy.getUserList()

def openSession(params):
	if len(params) < 1:
		print 'Error: function \'openSession\' takes 2 params'
		return 'Error: function \'openSession\' takes 2 params'
	id = parse(params[0])
	return proxy.openSession(id)

def closeSession(params):
	return proxy.closeSession()

def insertUserData(params):
	if len(params) < 3:
		print 'Error: function \'insertUserData\' takes 2 params'
		return 'Error: function \'insertUserData\' takes 2 params'
	variableName = parse(params[0])
	variableValue = parse(params[1])
	userID = parse(params[2])
	return proxy.insertUserData(variableName,variableValue,userID)

def getUserData(params):
	if len(params) < 2:
		print 'Error: function \'getUserData\' takes 2 params'
		return 'Error: function \'getUserData\' takes 2 params'
	variableName = parse(params[0])
	userID = parse(params[1])
	return proxy.getUserData(variableName,userID)

def getUserDataList(params):
	if len(params) < 1:
		print 'Error: function \'getUserDataList\' takes 2 params'
		return 'Error: function \'getUserDataList\' takes 2 params'
	userID = parse(params[0])
	return proxy.getUserDataList(userID)

def compileAll(params):
	return proxy.compileAll()

def startPush(params):
	return proxy.startPush()

def stopPush(params):
	return proxy.stopPush()

def startApp(params):
	if len(params) < 3:
		print 'Error: function \'startApp\' takes 2 params'
		return 'Error: function \'startApp\' takes 2 params'
	UNUSED_name = parse(params[0])
	val = parse(params[1])
	UNUSED_message = parse(params[2])
	return proxy.startApp(UNUSED_name,val,UNUSED_message)

def resetAll(params):
	return proxy.resetAll()

def startUpdate(params):
	if len(params) < 3:
		print 'Error: function \'startUpdate\' takes 2 params'
		return 'Error: function \'startUpdate\' takes 2 params'
	UNUSED_name = parse(params[0])
	val = parse(params[1])
	UNUSED_message = parse(params[2])
	return proxy.startUpdate(UNUSED_name,val,UNUSED_message)

def generateSentences(params):
	if len(params) < 3:
		print 'Error: function \'generateSentences\' takes 2 params'
		return 'Error: function \'generateSentences\' takes 2 params'
	destination = parse(params[0])
	topic = parse(params[1])
	language = parse(params[2])
	return proxy.generateSentences(destination,topic,language)

def tell(params):
	if len(params) < 1:
		print 'Error: function \'tell\' takes 2 params'
		return 'Error: function \'tell\' takes 2 params'
	input = parse(params[0])
	return proxy.tell(input)

def connectionChanged(params):
	return proxy.connectionChanged()

def endOfUtteranceCallback(params):
	return proxy.endOfUtteranceCallback()

def eventReceived(params):
	return proxy.eventReceived()

def packageInstalled(params):
	return proxy.packageInstalled()

def setPushMode(params):
	return proxy.setPushMode()

def statusChanged(params):
	return proxy.statusChanged()

def wordRecognized(params):
	return proxy.wordRecognized()

def wordsRecognizedCallback(params):
	return proxy.wordsRecognizedCallback()

