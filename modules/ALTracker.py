from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALTracker', '127.0.0.1', PORT)

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

def addEffector(params):
	if len(params) < 1:
		print 'Error: function \'addEffector\' takes 2 params'
		return 'Error: function \'addEffector\' takes 2 params'
	Effector = parse(params[0])
	return proxy.addEffector(Effector)

def addTarget(params):
	if len(params) < 2:
		print 'Error: function \'addTarget\' takes 2 params'
		return 'Error: function \'addTarget\' takes 2 params'
	TargetName = parse(params[0])
	Param = parse(params[1])
	return proxy.addTarget(TargetName,Param)

def getActiveTarget(params):
	return proxy.getActiveTarget()

def getAvailableModes(params):
	return proxy.getAvailableModes()

def getEffector(params):
	return proxy.getEffector()

def getExtractorPeriod(params):
	if len(params) < 1:
		print 'Error: function \'getExtractorPeriod\' takes 2 params'
		return 'Error: function \'getExtractorPeriod\' takes 2 params'
	TargetName = parse(params[0])
	return proxy.getExtractorPeriod(TargetName)

def getManagedTargets(params):
	return proxy.getManagedTargets()

def getMaximumDistanceDetection(params):
	return proxy.getMaximumDistanceDetection()

def getMode(params):
	return proxy.getMode()

def getMoveConfig(params):
	return proxy.getMoveConfig()

def getRegisteredTargets(params):
	return proxy.getRegisteredTargets()

def getRelativePosition(params):
	return proxy.getRelativePosition()

def getRobotPosition(params):
	return proxy.getRobotPosition()

def getSupportedTargets(params):
	return proxy.getSupportedTargets()

def getTargetNames(params):
	return proxy.getTargetNames()

def getTargetCoordinates(params):
	return proxy.getTargetCoordinates()

def getTargetPosition(params):
	if len(params) < 1:
		print 'Error: function \'getTargetPosition\' takes 2 params'
		return 'Error: function \'getTargetPosition\' takes 2 params'
	Frame = parse(params[0])
	return proxy.getTargetPosition(Frame)

def getTargetPosition(params):
	return proxy.getTargetPosition()

def getTimeOut(params):
	return proxy.getTimeOut()

def isActive(params):
	return proxy.isActive()

def isNewTargetDetected(params):
	return proxy.isNewTargetDetected()

def isSearchEnabled(params):
	return proxy.isSearchEnabled()

def isTargetLost(params):
	return proxy.isTargetLost()

def lookAt(params):
	if len(params) < 4:
		print 'Error: function \'lookAt\' takes 2 params'
		return 'Error: function \'lookAt\' takes 2 params'
	Position = parse(params[0])
	Frame = parse(params[1])
	FractionMaxSpeed = parse(params[2])
	UseWholeBody = parse(params[3])
	return proxy.lookAt(Position,Frame,FractionMaxSpeed,UseWholeBody)

def lookAt(params):
	if len(params) < 3:
		print 'Error: function \'lookAt\' takes 2 params'
		return 'Error: function \'lookAt\' takes 2 params'
	Position = parse(params[0])
	FractionMaxSpeed = parse(params[1])
	UseWholeBody = parse(params[2])
	return proxy.lookAt(Position,FractionMaxSpeed,UseWholeBody)

def pointAt(params):
	if len(params) < 4:
		print 'Error: function \'pointAt\' takes 2 params'
		return 'Error: function \'pointAt\' takes 2 params'
	Effector = parse(params[0])
	Position = parse(params[1])
	Frame = parse(params[2])
	FractionMaxSpeed = parse(params[3])
	return proxy.pointAt(Effector,Position,Frame,FractionMaxSpeed)

def pointAt(params):
	if len(params) < 3:
		print 'Error: function \'pointAt\' takes 2 params'
		return 'Error: function \'pointAt\' takes 2 params'
	Effector = parse(params[0])
	Position = parse(params[1])
	FractionMaxSpeed = parse(params[2])
	return proxy.pointAt(Effector,Position,FractionMaxSpeed)

def registerTarget(params):
	if len(params) < 2:
		print 'Error: function \'registerTarget\' takes 2 params'
		return 'Error: function \'registerTarget\' takes 2 params'
	TargetName = parse(params[0])
	Param = parse(params[1])
	return proxy.registerTarget(TargetName,Param)

def removeAllTargets(params):
	return proxy.removeAllTargets()

def removeEffector(params):
	if len(params) < 1:
		print 'Error: function \'removeEffector\' takes 2 params'
		return 'Error: function \'removeEffector\' takes 2 params'
	Effector = parse(params[0])
	return proxy.removeEffector(Effector)

def removeTarget(params):
	if len(params) < 1:
		print 'Error: function \'removeTarget\' takes 2 params'
		return 'Error: function \'removeTarget\' takes 2 params'
	TargetName = parse(params[0])
	return proxy.removeTarget(TargetName)

def removeTargets(params):
	if len(params) < 1:
		print 'Error: function \'removeTargets\' takes 2 params'
		return 'Error: function \'removeTargets\' takes 2 params'
	TargetNames = parse(params[0])
	return proxy.removeTargets(TargetNames)

def setEffector(params):
	if len(params) < 1:
		print 'Error: function \'setEffector\' takes 2 params'
		return 'Error: function \'setEffector\' takes 2 params'
	Effector = parse(params[0])
	return proxy.setEffector(Effector)

def setExtractorPeriod(params):
	if len(params) < 2:
		print 'Error: function \'setExtractorPeriod\' takes 2 params'
		return 'Error: function \'setExtractorPeriod\' takes 2 params'
	TargetName = parse(params[0])
	Period = parse(params[1])
	return proxy.setExtractorPeriod(TargetName,Period)

def setMaximumDistanceDetection(params):
	if len(params) < 1:
		print 'Error: function \'setMaximumDistanceDetection\' takes 2 params'
		return 'Error: function \'setMaximumDistanceDetection\' takes 2 params'
	MaxDistance = parse(params[0])
	return proxy.setMaximumDistanceDetection(MaxDistance)

def setMode(params):
	if len(params) < 1:
		print 'Error: function \'setMode\' takes 2 params'
		return 'Error: function \'setMode\' takes 2 params'
	Mode = parse(params[0])
	return proxy.setMode(Mode)

def setMoveConfig(params):
	if len(params) < 1:
		print 'Error: function \'setMoveConfig\' takes 2 params'
		return 'Error: function \'setMoveConfig\' takes 2 params'
	Config = parse(params[0])
	return proxy.setMoveConfig(Config)

def setRelativePosition(params):
	if len(params) < 1:
		print 'Error: function \'setRelativePosition\' takes 2 params'
		return 'Error: function \'setRelativePosition\' takes 2 params'
	Target = parse(params[0])
	return proxy.setRelativePosition(Target)

def setTargetCoordinates(params):
	if len(params) < 1:
		print 'Error: function \'setTargetCoordinates\' takes 2 params'
		return 'Error: function \'setTargetCoordinates\' takes 2 params'
	Coord = parse(params[0])
	return proxy.setTargetCoordinates(Coord)

def setTimeOut(params):
	if len(params) < 1:
		print 'Error: function \'setTimeOut\' takes 2 params'
		return 'Error: function \'setTimeOut\' takes 2 params'
	TimeMs = parse(params[0])
	return proxy.setTimeOut(TimeMs)

def stopTracker(params):
	return proxy.stopTracker()

def track(params):
	if len(params) < 1:
		print 'Error: function \'track\' takes 2 params'
		return 'Error: function \'track\' takes 2 params'
	TargetName = parse(params[0])
	return proxy.track(TargetName)

def trackEvent(params):
	if len(params) < 1:
		print 'Error: function \'trackEvent\' takes 2 params'
		return 'Error: function \'trackEvent\' takes 2 params'
	EventName = parse(params[0])
	return proxy.trackEvent(EventName)

def toggleSearch(params):
	if len(params) < 1:
		print 'Error: function \'toggleSearch\' takes 2 params'
		return 'Error: function \'toggleSearch\' takes 2 params'
	SearchOn = parse(params[0])
	return proxy.toggleSearch(SearchOn)

def unregisterAllTargets(params):
	return proxy.unregisterAllTargets()

def unregisterTarget(params):
	if len(params) < 1:
		print 'Error: function \'unregisterTarget\' takes 2 params'
		return 'Error: function \'unregisterTarget\' takes 2 params'
	TargetName = parse(params[0])
	return proxy.unregisterTarget(TargetName)

def unregisterTargets(params):
	if len(params) < 1:
		print 'Error: function \'unregisterTargets\' takes 2 params'
		return 'Error: function \'unregisterTargets\' takes 2 params'
	TargetNames = parse(params[0])
	return proxy.unregisterTargets(TargetNames)

