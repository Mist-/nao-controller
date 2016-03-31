from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALWorldRepresentation', '127.0.0.1', PORT)

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

def addAttributeToCategory(params):
	if len(params) < 3:
		print 'Error: function \'addAttributeToCategory\' takes 2 params'
		return 'Error: function \'addAttributeToCategory\' takes 2 params'
	categoryName = parse(params[0])
	attributeName = parse(params[1])
	attributeFields = parse(params[2])
	return proxy.addAttributeToCategory(categoryName,attributeName,attributeFields)

def clearObject(params):
	if len(params) < 1:
		print 'Error: function \'clearObject\' takes 2 params'
		return 'Error: function \'clearObject\' takes 2 params'
	objectName = parse(params[0])
	return proxy.clearObject(objectName)

def clearOldPositions(params):
	if len(params) < 2:
		print 'Error: function \'clearOldPositions\' takes 2 params'
		return 'Error: function \'clearOldPositions\' takes 2 params'
	databaseName = parse(params[0])
	maxAge = parse(params[1])
	return proxy.clearOldPositions(databaseName,maxAge)

def createObjectCategory(params):
	if len(params) < 2:
		print 'Error: function \'createObjectCategory\' takes 2 params'
		return 'Error: function \'createObjectCategory\' takes 2 params'
	categoryName = parse(params[0])
	resetCategory = parse(params[1])
	return proxy.createObjectCategory(categoryName,resetCategory)

def deleteObjectAttribute(params):
	if len(params) < 3:
		print 'Error: function \'deleteObjectAttribute\' takes 2 params'
		return 'Error: function \'deleteObjectAttribute\' takes 2 params'
	objectName = parse(params[0])
	attributeName = parse(params[1])
	criterion = parse(params[2])
	return proxy.deleteObjectAttribute(objectName,attributeName,criterion)

def findObject(params):
	if len(params) < 1:
		print 'Error: function \'findObject\' takes 2 params'
		return 'Error: function \'findObject\' takes 2 params'
	objectName = parse(params[0])
	return proxy.findObject(objectName)

def getChildrenNames(params):
	if len(params) < 1:
		print 'Error: function \'getChildrenNames\' takes 2 params'
		return 'Error: function \'getChildrenNames\' takes 2 params'
	objectName = parse(params[0])
	return proxy.getChildrenNames(objectName)

def getObjectCategory(params):
	if len(params) < 1:
		print 'Error: function \'getObjectCategory\' takes 2 params'
		return 'Error: function \'getObjectCategory\' takes 2 params'
	objectName = parse(params[0])
	return proxy.getObjectCategory(objectName)

def getObjectNames(params):
	return proxy.getObjectNames()

def getObjectAttributes(params):
	if len(params) < 1:
		print 'Error: function \'getObjectAttributes\' takes 2 params'
		return 'Error: function \'getObjectAttributes\' takes 2 params'
	objectName = parse(params[0])
	return proxy.getObjectAttributes(objectName)

def getObjectLatestAttributes(params):
	if len(params) < 2:
		print 'Error: function \'getObjectLatestAttributes\' takes 2 params'
		return 'Error: function \'getObjectLatestAttributes\' takes 2 params'
	objectName = parse(params[0])
	latestCount = parse(params[1])
	return proxy.getObjectLatestAttributes(objectName,latestCount)

def getObjectAttributeValues(params):
	if len(params) < 3:
		print 'Error: function \'getObjectAttributeValues\' takes 2 params'
		return 'Error: function \'getObjectAttributeValues\' takes 2 params'
	objectName = parse(params[0])
	attributeName = parse(params[1])
	latestCount = parse(params[2])
	return proxy.getObjectAttributeValues(objectName,attributeName,latestCount)

def getObjectsInCategory(params):
	if len(params) < 1:
		print 'Error: function \'getObjectsInCategory\' takes 2 params'
		return 'Error: function \'getObjectsInCategory\' takes 2 params'
	objectName = parse(params[0])
	return proxy.getObjectsInCategory(objectName)

def getObjectParentName(params):
	if len(params) < 1:
		print 'Error: function \'getObjectParentName\' takes 2 params'
		return 'Error: function \'getObjectParentName\' takes 2 params'
	objectName = parse(params[0])
	return proxy.getObjectParentName(objectName)

def getPosition(params):
	if len(params) < 2:
		print 'Error: function \'getPosition\' takes 2 params'
		return 'Error: function \'getPosition\' takes 2 params'
	referenceName = parse(params[0])
	objectName = parse(params[1])
	return proxy.getPosition(referenceName,objectName)

def getPosition6D(params):
	if len(params) < 2:
		print 'Error: function \'getPosition6D\' takes 2 params'
		return 'Error: function \'getPosition6D\' takes 2 params'
	referenceName = parse(params[0])
	objectName = parse(params[1])
	return proxy.getPosition6D(referenceName,objectName)

def getPosition6DAtTime(params):
	if len(params) < 4:
		print 'Error: function \'getPosition6DAtTime\' takes 2 params'
		return 'Error: function \'getPosition6DAtTime\' takes 2 params'
	referenceName = parse(params[0])
	objectName = parse(params[1])
	secondsAgo = parse(params[2])
	interpType = parse(params[3])
	return proxy.getPosition6DAtTime(referenceName,objectName,secondsAgo,interpType)

def getRootName(params):
	return proxy.getRootName()

def removeObjectCategory(params):
	if len(params) < 1:
		print 'Error: function \'removeObjectCategory\' takes 2 params'
		return 'Error: function \'removeObjectCategory\' takes 2 params'
	categoryName = parse(params[0])
	return proxy.removeObjectCategory(categoryName)

def save(params):
	return proxy.save()

def select(params):
	if len(params) < 4:
		print 'Error: function \'select\' takes 2 params'
		return 'Error: function \'select\' takes 2 params'
	criterion = parse(params[0])
	categoryName = parse(params[1])
	attributeName = parse(params[2])
	fields = parse(params[3])
	return proxy.select(criterion,categoryName,attributeName,fields)

def selectWithOrder(params):
	if len(params) < 5:
		print 'Error: function \'selectWithOrder\' takes 2 params'
		return 'Error: function \'selectWithOrder\' takes 2 params'
	criterion = parse(params[0])
	orderBy = parse(params[1])
	categoryName = parse(params[2])
	attributeName = parse(params[3])
	fields = parse(params[4])
	return proxy.selectWithOrder(criterion,orderBy,categoryName,attributeName,fields)

def storeObject(params):
	if len(params) < 5:
		print 'Error: function \'storeObject\' takes 2 params'
		return 'Error: function \'storeObject\' takes 2 params'
	objectName = parse(params[0])
	parentName = parse(params[1])
	position6D = parse(params[2])
	categoryName = parse(params[3])
	attributes = parse(params[4])
	return proxy.storeObject(objectName,parentName,position6D,categoryName,attributes)

def storeObjectWithReference(params):
	if len(params) < 6:
		print 'Error: function \'storeObjectWithReference\' takes 2 params'
		return 'Error: function \'storeObjectWithReference\' takes 2 params'
	objectName = parse(params[0])
	referenceName = parse(params[1])
	parentName = parse(params[2])
	position6D = parse(params[3])
	categoryName = parse(params[4])
	attributes = parse(params[5])
	return proxy.storeObjectWithReference(objectName,referenceName,parentName,position6D,categoryName,attributes)

def storeObjectAttribute(params):
	if len(params) < 3:
		print 'Error: function \'storeObjectAttribute\' takes 2 params'
		return 'Error: function \'storeObjectAttribute\' takes 2 params'
	objectName = parse(params[0])
	attributeName = parse(params[1])
	attributeFields = parse(params[2])
	return proxy.storeObjectAttribute(objectName,attributeName,attributeFields)

def updatePosition(params):
	if len(params) < 3:
		print 'Error: function \'updatePosition\' takes 2 params'
		return 'Error: function \'updatePosition\' takes 2 params'
	objectName = parse(params[0])
	position6D = parse(params[1])
	storePosition = parse(params[2])
	return proxy.updatePosition(objectName,position6D,storePosition)

def updatePositionWithReference(params):
	if len(params) < 4:
		print 'Error: function \'updatePositionWithReference\' takes 2 params'
		return 'Error: function \'updatePositionWithReference\' takes 2 params'
	objectName = parse(params[0])
	referenceName = parse(params[1])
	position6D = parse(params[2])
	storePosition = parse(params[3])
	return proxy.updatePositionWithReference(objectName,referenceName,position6D,storePosition)

def updateAttribute(params):
	if len(params) < 4:
		print 'Error: function \'updateAttribute\' takes 2 params'
		return 'Error: function \'updateAttribute\' takes 2 params'
	objectName = parse(params[0])
	attributeName = parse(params[1])
	criterion = parse(params[2])
	attributeFields = parse(params[3])
	return proxy.updateAttribute(objectName,attributeName,criterion,attributeFields)

def load(params):
	return proxy.load()

def setObjectsLook(params):
	if len(params) < 2:
		print 'Error: function \'setObjectsLook\' takes 2 params'
		return 'Error: function \'setObjectsLook\' takes 2 params'
	const std::string& = parse(params[0])
	const ALValue& = parse(params[1])
	return proxy.setObjectsLook(const std::string&,const ALValue&)

def startDisplaying(params):
	return proxy.startDisplaying()

def stopDisplaying(params):
	return proxy.stopDisplaying()

