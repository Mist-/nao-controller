from naoqi import ALProxy
from network.const import PORT, IP
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALBehaviorManager', IP, PORT)

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

def addDefaultBehavior(params):
	if len(params) < 1:
		print 'Error: function \'addDefaultBehavior\' takes 2 params'
		return 'Error: function \'addDefaultBehavior\' takes 2 params'
	prefixedBehavior = parse(params[0])
	return proxy.addDefaultBehavior(prefixedBehavior)

def getBehaviorTags(params):
	if len(params) < 1:
		print 'Error: function \'getBehaviorTags\' takes 2 params'
		return 'Error: function \'getBehaviorTags\' takes 2 params'
	behavior = parse(params[0])
	return proxy.getBehaviorTags(behavior)

def getBehaviorsByTag(params):
	if len(params) < 1:
		print 'Error: function \'getBehaviorsByTag\' takes 2 params'
		return 'Error: function \'getBehaviorsByTag\' takes 2 params'
	tag = parse(params[0])
	return proxy.getBehaviorsByTag(tag)

def getBehaviorNature(params):
	if len(params) < 1:
		print 'Error: function \'getBehaviorNature\' takes 2 params'
		return 'Error: function \'getBehaviorNature\' takes 2 params'
	behavior = parse(params[0])
	return proxy.getBehaviorNature(behavior)

def getDefaultBehaviors(params):
	return proxy.getDefaultBehaviors()

def getInstalledBehaviors(params):
	return proxy.getInstalledBehaviors()

def getLoadedBehaviors(params):
	return proxy.getLoadedBehaviors()

def getRunningBehaviors(params):
	return proxy.getRunningBehaviors()

def getTagList(params):
	return proxy.getTagList()

def isBehaviorInstalled(params):
	if len(params) < 1:
		print 'Error: function \'isBehaviorInstalled\' takes 2 params'
		return 'Error: function \'isBehaviorInstalled\' takes 2 params'
	name = parse(params[0])
	return proxy.isBehaviorInstalled(name)

def isBehaviorLoaded(params):
	if len(params) < 1:
		print 'Error: function \'isBehaviorLoaded\' takes 2 params'
		return 'Error: function \'isBehaviorLoaded\' takes 2 params'
	name = parse(params[0])
	return proxy.isBehaviorLoaded(name)

def isBehaviorRunning(params):
	if len(params) < 1:
		print 'Error: function \'isBehaviorRunning\' takes 2 params'
		return 'Error: function \'isBehaviorRunning\' takes 2 params'
	name = parse(params[0])
	return proxy.isBehaviorRunning(name)

def playDefaultProject(params):
	return proxy.playDefaultProject()

def preloadBehavior(params):
	if len(params) < 1:
		print 'Error: function \'preloadBehavior\' takes 2 params'
		return 'Error: function \'preloadBehavior\' takes 2 params'
	name = parse(params[0])
	return proxy.preloadBehavior(name)

def removeDefaultBehavior(params):
	if len(params) < 1:
		print 'Error: function \'removeDefaultBehavior\' takes 2 params'
		return 'Error: function \'removeDefaultBehavior\' takes 2 params'
	name = parse(params[0])
	return proxy.removeDefaultBehavior(name)

def resolveBehaviorName(params):
	if len(params) < 1:
		print 'Error: function \'resolveBehaviorName\' takes 2 params'
		return 'Error: function \'resolveBehaviorName\' takes 2 params'
	behaviorName = parse(params[0])
	return proxy.resolveBehaviorName(behaviorName)

def runBehavior(params):
	if len(params) < 1:
		print 'Error: function \'runBehavior\' takes 2 params'
		return 'Error: function \'runBehavior\' takes 2 params'
	name = parse(params[0])
	return proxy.runBehavior(name)

def startBehavior(params):
	if len(params) < 1:
		print 'Error: function \'startBehavior\' takes 2 params'
		return 'Error: function \'startBehavior\' takes 2 params'
	name = parse(params[0])
	return proxy.startBehavior(name)

def stopAllBehaviors(params):
	return proxy.stopAllBehaviors()

def stopBehavior(params):
	if len(params) < 1:
		print 'Error: function \'stopBehavior\' takes 2 params'
		return 'Error: function \'stopBehavior\' takes 2 params'
	name = parse(params[0])
	return proxy.stopBehavior(name)

def getBehaviorNames(params):
	return proxy.getBehaviorNames()

def getSystemBehaviorNames(params):
	return proxy.getSystemBehaviorNames()

def getUserBehaviorNames(params):
	return proxy.getUserBehaviorNames()

def installBehavior(params):
	if len(params) < 3:
		print 'Error: function \'installBehavior\' takes 2 params'
		return 'Error: function \'installBehavior\' takes 2 params'
	absolutePath = parse(params[0])
	localPath = parse(params[1])
	overwrite = parse(params[2])
	return proxy.installBehavior(absolutePath,localPath,overwrite)

def installBehavior(params):
	if len(params) < 1:
		print 'Error: function \'installBehavior\' takes 2 params'
		return 'Error: function \'installBehavior\' takes 2 params'
	localPath = parse(params[0])
	return proxy.installBehavior(localPath)

def isBehaviorPresent(params):
	if len(params) < 1:
		print 'Error: function \'isBehaviorPresent\' takes 2 params'
		return 'Error: function \'isBehaviorPresent\' takes 2 params'
	prefixedBehavior = parse(params[0])
	return proxy.isBehaviorPresent(prefixedBehavior)

def removeBehavior(params):
	if len(params) < 1:
		print 'Error: function \'removeBehavior\' takes 2 params'
		return 'Error: function \'removeBehavior\' takes 2 params'
	name = parse(params[0])
	return proxy.removeBehavior(name)

def behaviorsRemoved(params):
	if len(params) < 1:
		print 'Error: function \'behaviorsRemoved\' takes 2 params'
		return 'Error: function \'behaviorsRemoved\' takes 2 params'
	behaviorsRemoved = parse(params[0])
	return proxy.behaviorsRemoved(behaviorsRemoved)

def behaviorFailed(params):
	if len(params) < 3:
		print 'Error: function \'behaviorFailed\' takes 2 params'
		return 'Error: function \'behaviorFailed\' takes 2 params'
	behaviorName = parse(params[0])
	boxName = parse(params[1])
	error = parse(params[2])
	return proxy.behaviorFailed(behaviorName,boxName,error)

def behaviorsAdded(params):
	if len(params) < 1:
		print 'Error: function \'behaviorsAdded\' takes 2 params'
		return 'Error: function \'behaviorsAdded\' takes 2 params'
	behaviorsAdded = parse(params[0])
	return proxy.behaviorsAdded(behaviorsAdded)

def behaviorStopped(params):
	if len(params) < 1:
		print 'Error: function \'behaviorStopped\' takes 2 params'
		return 'Error: function \'behaviorStopped\' takes 2 params'
	behaviorName = parse(params[0])
	return proxy.behaviorStopped(behaviorName)

def behaviorStarted(params):
	if len(params) < 1:
		print 'Error: function \'behaviorStarted\' takes 2 params'
		return 'Error: function \'behaviorStarted\' takes 2 params'
	behaviorName = parse(params[0])
	return proxy.behaviorStarted(behaviorName)

def behaviorLoaded(params):
	if len(params) < 1:
		print 'Error: function \'behaviorLoaded\' takes 2 params'
		return 'Error: function \'behaviorLoaded\' takes 2 params'
	behaviorName = parse(params[0])
	return proxy.behaviorLoaded(behaviorName)

