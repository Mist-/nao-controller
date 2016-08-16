from naoqi import ALProxy
from network.const import PORT, IP
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALMemory', IP,  PORT)

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

def declareEvent(params):
	if len(params) < 1:
		print 'Error: function \'declareEvent\' takes 2 params'
		return 'Error: function \'declareEvent\' takes 2 params'
	eventName = parse(params[0])
	return proxy.declareEvent(eventName)

def declareEvent(params):
	if len(params) < 2:
		print 'Error: function \'declareEvent\' takes 2 params'
		return 'Error: function \'declareEvent\' takes 2 params'
	eventName = parse(params[0])
	extractorName = parse(params[1])
	return proxy.declareEvent(eventName,extractorName)

def getData(params):
	if len(params) < 1:
		print 'Error: function \'getData\' takes 2 params'
		return 'Error: function \'getData\' takes 2 params'
	key = parse(params[0])
	return proxy.getData(key)

def getData(params):
	if len(params) < 2:
		print 'Error: function \'getData\' takes 2 params'
		return 'Error: function \'getData\' takes 2 params'
	key = parse(params[0])
	deprecatedParameter = parse(params[1])
	return proxy.getData(key,deprecatedParameter)

def getDataList(params):
	if len(params) < 1:
		print 'Error: function \'getDataList\' takes 2 params'
		return 'Error: function \'getDataList\' takes 2 params'
	filter = parse(params[0])
	return proxy.getDataList(filter)

def getDataListName(params):
	return proxy.getDataListName()

def getDataOnChange(params):
	if len(params) < 2:
		print 'Error: function \'getDataOnChange\' takes 2 params'
		return 'Error: function \'getDataOnChange\' takes 2 params'
	key = parse(params[0])
	deprecatedParameter = parse(params[1])
	return proxy.getDataOnChange(key,deprecatedParameter)

def getDataPtr(params):
	if len(params) < 1:
		print 'Error: function \'getDataPtr\' takes 2 params'
		return 'Error: function \'getDataPtr\' takes 2 params'
	key = parse(params[0])
	return proxy.getDataPtr(key)

def getDescriptionList(params):
	if len(params) < 1:
		print 'Error: function \'getDescriptionList\' takes 2 params'
		return 'Error: function \'getDescriptionList\' takes 2 params'
	keys = parse(params[0])
	return proxy.getDescriptionList(keys)

def getEventHistory(params):
	if len(params) < 1:
		print 'Error: function \'getEventHistory\' takes 2 params'
		return 'Error: function \'getEventHistory\' takes 2 params'
	pName = parse(params[0])
	return proxy.getEventHistory(pName)

def getEventList(params):
	return proxy.getEventList()

def getTimestamp(params):
	if len(params) < 1:
		print 'Error: function \'getTimestamp\' takes 2 params'
		return 'Error: function \'getTimestamp\' takes 2 params'
	memoryKey = parse(params[0])
	return proxy.getTimestamp(memoryKey)

def getExtractorEvent(params):
	if len(params) < 1:
		print 'Error: function \'getExtractorEvent\' takes 2 params'
		return 'Error: function \'getExtractorEvent\' takes 2 params'
	extractorName = parse(params[0])
	return proxy.getExtractorEvent(extractorName)

def getListData(params):
	if len(params) < 1:
		print 'Error: function \'getListData\' takes 2 params'
		return 'Error: function \'getListData\' takes 2 params'
	keyList = parse(params[0])
	return proxy.getListData(keyList)

def getMicroEventList(params):
	return proxy.getMicroEventList()

def getSubscribers(params):
	if len(params) < 1:
		print 'Error: function \'getSubscribers\' takes 2 params'
		return 'Error: function \'getSubscribers\' takes 2 params'
	name = parse(params[0])
	return proxy.getSubscribers(name)

def getType(params):
	if len(params) < 1:
		print 'Error: function \'getType\' takes 2 params'
		return 'Error: function \'getType\' takes 2 params'
	key = parse(params[0])
	return proxy.getType(key)

def insertData(params):
	if len(params) < 2:
		print 'Error: function \'insertData\' takes 2 params'
		return 'Error: function \'insertData\' takes 2 params'
	key = parse(params[0])
	value = parse(params[1])
	return proxy.insertData(key,value)

def insertData(params):
	if len(params) < 2:
		print 'Error: function \'insertData\' takes 2 params'
		return 'Error: function \'insertData\' takes 2 params'
	key = parse(params[0])
	value = parse(params[1])
	return proxy.insertData(key,value)

def insertData(params):
	if len(params) < 2:
		print 'Error: function \'insertData\' takes 2 params'
		return 'Error: function \'insertData\' takes 2 params'
	key = parse(params[0])
	value = parse(params[1])
	return proxy.insertData(key,value)

def insertData(params):
	if len(params) < 2:
		print 'Error: function \'insertData\' takes 2 params'
		return 'Error: function \'insertData\' takes 2 params'
	key = parse(params[0])
	data = parse(params[1])
	return proxy.insertData(key,data)

def insertListData(params):
	if len(params) < 1:
		print 'Error: function \'insertListData\' takes 2 params'
		return 'Error: function \'insertListData\' takes 2 params'
	list = parse(params[0])
	return proxy.insertListData(list)

def raiseEvent(params):
	if len(params) < 2:
		print 'Error: function \'raiseEvent\' takes 2 params'
		return 'Error: function \'raiseEvent\' takes 2 params'
	name = parse(params[0])
	value = parse(params[1])
	return proxy.raiseEvent(name,value)

def raiseMicroEvent(params):
	if len(params) < 2:
		print 'Error: function \'raiseMicroEvent\' takes 2 params'
		return 'Error: function \'raiseMicroEvent\' takes 2 params'
	name = parse(params[0])
	value = parse(params[1])
	return proxy.raiseMicroEvent(name,value)

def removeData(params):
	if len(params) < 1:
		print 'Error: function \'removeData\' takes 2 params'
		return 'Error: function \'removeData\' takes 2 params'
	key = parse(params[0])
	return proxy.removeData(key)

def removeMicroEvent(params):
	if len(params) < 1:
		print 'Error: function \'removeMicroEvent\' takes 2 params'
		return 'Error: function \'removeMicroEvent\' takes 2 params'
	name = parse(params[0])
	return proxy.removeMicroEvent(name)

def setDescription(params):
	if len(params) < 2:
		print 'Error: function \'setDescription\' takes 2 params'
		return 'Error: function \'setDescription\' takes 2 params'
	name = parse(params[0])
	description = parse(params[1])
	return proxy.setDescription(name,description)

def subscribeToEvent(params):
	if len(params) < 3:
		print 'Error: function \'subscribeToEvent\' takes 2 params'
		return 'Error: function \'subscribeToEvent\' takes 2 params'
	name = parse(params[0])
	callbackModule = parse(params[1])
	callbackMethod = parse(params[2])
	return proxy.subscribeToEvent(name,callbackModule,callbackMethod)

def subscribeToEvent(params):
	if len(params) < 4:
		print 'Error: function \'subscribeToEvent\' takes 2 params'
		return 'Error: function \'subscribeToEvent\' takes 2 params'
	name = parse(params[0])
	callbackModule = parse(params[1])
	callbackMessage = parse(params[2])
	callbackMethod = parse(params[3])
	return proxy.subscribeToEvent(name,callbackModule,callbackMessage,callbackMethod)

def subscribeToMicroEvent(params):
	if len(params) < 4:
		print 'Error: function \'subscribeToMicroEvent\' takes 2 params'
		return 'Error: function \'subscribeToMicroEvent\' takes 2 params'
	name = parse(params[0])
	callbackModule = parse(params[1])
	callbackMessage = parse(params[2])
	callbackMethod = parse(params[3])
	return proxy.subscribeToMicroEvent(name,callbackModule,callbackMessage,callbackMethod)

def unregisterModuleReference(params):
	if len(params) < 1:
		print 'Error: function \'unregisterModuleReference\' takes 2 params'
		return 'Error: function \'unregisterModuleReference\' takes 2 params'
	moduleName = parse(params[0])
	return proxy.unregisterModuleReference(moduleName)

def unsubscribeToEvent(params):
	if len(params) < 2:
		print 'Error: function \'unsubscribeToEvent\' takes 2 params'
		return 'Error: function \'unsubscribeToEvent\' takes 2 params'
	name = parse(params[0])
	callbackModule = parse(params[1])
	return proxy.unsubscribeToEvent(name,callbackModule)

def unsubscribeToMicroEvent(params):
	if len(params) < 2:
		print 'Error: function \'unsubscribeToMicroEvent\' takes 2 params'
		return 'Error: function \'unsubscribeToMicroEvent\' takes 2 params'
	name = parse(params[0])
	callbackModule = parse(params[1])
	return proxy.unsubscribeToMicroEvent(name,callbackModule)

