from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALResourceManager', '127.0.0.1', PORT)

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

def areResourcesFree(params):
	if len(params) < 1:
		print 'Error: function \'areResourcesFree\' takes 2 params'
		return 'Error: function \'areResourcesFree\' takes 2 params'
	resourceNames = parse(params[0])
	return proxy.areResourcesFree(resourceNames)

def areResourcesOwnedBy(params):
	if len(params) < 2:
		print 'Error: function \'areResourcesOwnedBy\' takes 2 params'
		return 'Error: function \'areResourcesOwnedBy\' takes 2 params'
	resourceNameList = parse(params[0])
	ownerName = parse(params[1])
	return proxy.areResourcesOwnedBy(resourceNameList,ownerName)

def createResource(params):
	if len(params) < 2:
		print 'Error: function \'createResource\' takes 2 params'
		return 'Error: function \'createResource\' takes 2 params'
	resourceName = parse(params[0])
	parentResourceName = parse(params[1])
	return proxy.createResource(resourceName,parentResourceName)

def createResourcesList(params):
	if len(params) < 2:
		print 'Error: function \'createResourcesList\' takes 2 params'
		return 'Error: function \'createResourcesList\' takes 2 params'
	resourceNameList = parse(params[0])
	strModule = parse(params[1])
	return proxy.createResourcesList(resourceNameList,strModule)

def deleteResource(params):
	if len(params) < 1:
		print 'Error: function \'deleteResource\' takes 2 params'
		return 'Error: function \'deleteResource\' takes 2 params'
	resourceName = parse(params[0])
	return proxy.deleteResource(resourceName)

def deleteResource(params):
	if len(params) < 2:
		print 'Error: function \'deleteResource\' takes 2 params'
		return 'Error: function \'deleteResource\' takes 2 params'
	resourceName = parse(params[0])
	deleteChildResources = parse(params[1])
	return proxy.deleteResource(resourceName,deleteChildResources)

def enableStateResource(params):
	if len(params) < 2:
		print 'Error: function \'enableStateResource\' takes 2 params'
		return 'Error: function \'enableStateResource\' takes 2 params'
	resourceName = parse(params[0])
	enabled = parse(params[1])
	return proxy.enableStateResource(resourceName,enabled)

def isInGroup(params):
	if len(params) < 2:
		print 'Error: function \'isInGroup\' takes 2 params'
		return 'Error: function \'isInGroup\' takes 2 params'
	resourceGroupName = parse(params[0])
	resourceName = parse(params[1])
	return proxy.isInGroup(resourceGroupName,resourceName)

def releaseResources(params):
	if len(params) < 2:
		print 'Error: function \'releaseResources\' takes 2 params'
		return 'Error: function \'releaseResources\' takes 2 params'
	resourceNames = parse(params[0])
	ownerName = parse(params[1])
	return proxy.releaseResources(resourceNames,ownerName)

def acquireResource(params):
	if len(params) < 4:
		print 'Error: function \'acquireResource\' takes 2 params'
		return 'Error: function \'acquireResource\' takes 2 params'
	resourceName = parse(params[0])
	moduleName = parse(params[1])
	callbackName = parse(params[2])
	timeoutSeconds = parse(params[3])
	return proxy.acquireResource(resourceName,moduleName,callbackName,timeoutSeconds)

def acquireResourcesTree(params):
	if len(params) < 4:
		print 'Error: function \'acquireResourcesTree\' takes 2 params'
		return 'Error: function \'acquireResourcesTree\' takes 2 params'
	resourceNameList = parse(params[0])
	moduleName = parse(params[1])
	callbackName = parse(params[2])
	pnTimeOutMillisec = parse(params[3])
	return proxy.acquireResourcesTree(resourceNameList,moduleName,callbackName,pnTimeOutMillisec)

def releaseResource(params):
	if len(params) < 2:
		print 'Error: function \'releaseResource\' takes 2 params'
		return 'Error: function \'releaseResource\' takes 2 params'
	resourceName = parse(params[0])
	ownerName = parse(params[1])
	return proxy.releaseResource(resourceName,ownerName)

def getResources(params):
	return proxy.getResources()

def isResourceFree(params):
	if len(params) < 1:
		print 'Error: function \'isResourceFree\' takes 2 params'
		return 'Error: function \'isResourceFree\' takes 2 params'
	ResourceName = parse(params[0])
	return proxy.isResourceFree(ResourceName)

def ownersGet(params):
	return proxy.ownersGet()

def waitForOptionalResourcesTree(params):
	if len(params) < 5:
		print 'Error: function \'waitForOptionalResourcesTree\' takes 2 params'
		return 'Error: function \'waitForOptionalResourcesTree\' takes 2 params'
	pResourceNameList = parse(params[0])
	pOwner = parse(params[1])
	pLooseCallbackName = parse(params[2])
	pnTimeOutMillisec = parse(params[3])
	pOptionalResourceNameList = parse(params[4])
	return proxy.waitForOptionalResourcesTree(pResourceNameList,pOwner,pLooseCallbackName,pnTimeOutMillisec,pOptionalResourceNameList)

def waitForResourcesTree(params):
	if len(params) < 4:
		print 'Error: function \'waitForResourcesTree\' takes 2 params'
		return 'Error: function \'waitForResourcesTree\' takes 2 params'
	pResourceNameList = parse(params[0])
	pOwner = parse(params[1])
	pLooseCallbackName = parse(params[2])
	pnTimeOutMillisec = parse(params[3])
	return proxy.waitForResourcesTree(pResourceNameList,pOwner,pLooseCallbackName,pnTimeOutMillisec)

def waitForResource(params):
	if len(params) < 4:
		print 'Error: function \'waitForResource\' takes 2 params'
		return 'Error: function \'waitForResource\' takes 2 params'
	resourceName = parse(params[0])
	ownerName = parse(params[1])
	callbackName = parse(params[2])
	timeoutSeconds = parse(params[3])
	return proxy.waitForResource(resourceName,ownerName,callbackName,timeoutSeconds)

