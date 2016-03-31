from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALMotion', '127.0.0.1', PORT)

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

def wakeUp(params):
	return proxy.wakeUp()

def rest(params):
	return proxy.rest()

def robotIsWakeUp(params):
	return proxy.robotIsWakeUp()

def stiffnessInterpolation(params):
	if len(params) < 3:
		print 'Error: function \'stiffnessInterpolation\' takes 2 params'
		return 'Error: function \'stiffnessInterpolation\' takes 2 params'
	names = parse(params[0])
	stiffnessLists = parse(params[1])
	timeLists = parse(params[2])
	return proxy.stiffnessInterpolation(names,stiffnessLists,timeLists)

def setStiffnesses(params):
	if len(params) < 2:
		print 'Error: function \'setStiffnesses\' takes 2 params'
		return 'Error: function \'setStiffnesses\' takes 2 params'
	names = parse(params[0])
	stiffnesses = parse(params[1])
	return proxy.setStiffnesses(names,stiffnesses)

def getStiffnesses(params):
	if len(params) < 1:
		print 'Error: function \'getStiffnesses\' takes 2 params'
		return 'Error: function \'getStiffnesses\' takes 2 params'
	jointName = parse(params[0])
	return proxy.getStiffnesses(jointName)

def angleInterpolation(params):
	if len(params) < 4:
		print 'Error: function \'angleInterpolation\' takes 2 params'
		return 'Error: function \'angleInterpolation\' takes 2 params'
	names = parse(params[0])
	angleLists = parse(params[1])
	timeLists = parse(params[2])
	isAbsolute = parse(params[3])
	return proxy.angleInterpolation(names,angleLists,timeLists,isAbsolute)

def angleInterpolationWithSpeed(params):
	if len(params) < 3:
		print 'Error: function \'angleInterpolationWithSpeed\' takes 2 params'
		return 'Error: function \'angleInterpolationWithSpeed\' takes 2 params'
	names = parse(params[0])
	targetAngles = parse(params[1])
	maxSpeedFraction = parse(params[2])
	return proxy.angleInterpolationWithSpeed(names,targetAngles,maxSpeedFraction)

def angleInterpolationBezier(params):
	if len(params) < 3:
		print 'Error: function \'angleInterpolationBezier\' takes 2 params'
		return 'Error: function \'angleInterpolationBezier\' takes 2 params'
	jointNames = parse(params[0])
	times = parse(params[1])
	controlPoints = parse(params[2])
	return proxy.angleInterpolationBezier(jointNames,times,controlPoints)

def setAngles(params):
	if len(params) < 3:
		print 'Error: function \'setAngles\' takes 2 params'
		return 'Error: function \'setAngles\' takes 2 params'
	names = parse(params[0])
	angles = parse(params[1])
	fractionMaxSpeed = parse(params[2])
	return proxy.setAngles(names,angles,fractionMaxSpeed)

def changeAngles(params):
	if len(params) < 3:
		print 'Error: function \'changeAngles\' takes 2 params'
		return 'Error: function \'changeAngles\' takes 2 params'
	names = parse(params[0])
	changes = parse(params[1])
	fractionMaxSpeed = parse(params[2])
	return proxy.changeAngles(names,changes,fractionMaxSpeed)

def getAngles(params):
	if len(params) < 2:
		print 'Error: function \'getAngles\' takes 2 params'
		return 'Error: function \'getAngles\' takes 2 params'
	names = parse(params[0])
	useSensors = parse(params[1])
	return proxy.getAngles(names,useSensors)

def closeHand(params):
	if len(params) < 1:
		print 'Error: function \'closeHand\' takes 2 params'
		return 'Error: function \'closeHand\' takes 2 params'
	handName = parse(params[0])
	return proxy.closeHand(handName)

def openHand(params):
	if len(params) < 1:
		print 'Error: function \'openHand\' takes 2 params'
		return 'Error: function \'openHand\' takes 2 params'
	handName = parse(params[0])
	return proxy.openHand(handName)

def move(params):
	if len(params) < 3:
		print 'Error: function \'move\' takes 2 params'
		return 'Error: function \'move\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	return proxy.move(x,y,theta)

def move(params):
	if len(params) < 4:
		print 'Error: function \'move\' takes 2 params'
		return 'Error: function \'move\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	moveConfig = parse(params[3])
	return proxy.move(x,y,theta,moveConfig)

def moveToward(params):
	if len(params) < 3:
		print 'Error: function \'moveToward\' takes 2 params'
		return 'Error: function \'moveToward\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	return proxy.moveToward(x,y,theta)

def moveToward(params):
	if len(params) < 4:
		print 'Error: function \'moveToward\' takes 2 params'
		return 'Error: function \'moveToward\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	moveConfig = parse(params[3])
	return proxy.moveToward(x,y,theta,moveConfig)

def setWalkTargetVelocity(params):
	if len(params) < 4:
		print 'Error: function \'setWalkTargetVelocity\' takes 2 params'
		return 'Error: function \'setWalkTargetVelocity\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	frequency = parse(params[3])
	return proxy.setWalkTargetVelocity(x,y,theta,frequency)

def setWalkTargetVelocity(params):
	if len(params) < 5:
		print 'Error: function \'setWalkTargetVelocity\' takes 2 params'
		return 'Error: function \'setWalkTargetVelocity\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	frequency = parse(params[3])
	feetGaitConfig = parse(params[4])
	return proxy.setWalkTargetVelocity(x,y,theta,frequency,feetGaitConfig)

def setWalkTargetVelocity(params):
	if len(params) < 6:
		print 'Error: function \'setWalkTargetVelocity\' takes 2 params'
		return 'Error: function \'setWalkTargetVelocity\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	frequency = parse(params[3])
	leftFootGaitConfig = parse(params[4])
	rightFootGaitConfig = parse(params[5])
	return proxy.setWalkTargetVelocity(x,y,theta,frequency,leftFootGaitConfig,rightFootGaitConfig)

def moveTo(params):
	if len(params) < 3:
		print 'Error: function \'moveTo\' takes 2 params'
		return 'Error: function \'moveTo\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	return proxy.moveTo(x,y,theta)

def moveTo(params):
	if len(params) < 4:
		print 'Error: function \'moveTo\' takes 2 params'
		return 'Error: function \'moveTo\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	moveConfig = parse(params[3])
	return proxy.moveTo(x,y,theta,moveConfig)

def moveTo(params):
	if len(params) < 1:
		print 'Error: function \'moveTo\' takes 2 params'
		return 'Error: function \'moveTo\' takes 2 params'
	controlPoints = parse(params[0])
	return proxy.moveTo(controlPoints)

def moveTo(params):
	if len(params) < 2:
		print 'Error: function \'moveTo\' takes 2 params'
		return 'Error: function \'moveTo\' takes 2 params'
	controlPoints = parse(params[0])
	moveConfig = parse(params[1])
	return proxy.moveTo(controlPoints,moveConfig)

def moveTo(params):
	if len(params) < 4:
		print 'Error: function \'moveTo\' takes 2 params'
		return 'Error: function \'moveTo\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	pTime = parse(params[3])
	return proxy.moveTo(x,y,theta,pTime)

def walkTo(params):
	if len(params) < 3:
		print 'Error: function \'walkTo\' takes 2 params'
		return 'Error: function \'walkTo\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	return proxy.walkTo(x,y,theta)

def walkTo(params):
	if len(params) < 4:
		print 'Error: function \'walkTo\' takes 2 params'
		return 'Error: function \'walkTo\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	theta = parse(params[2])
	feetGaitConfig = parse(params[3])
	return proxy.walkTo(x,y,theta,feetGaitConfig)

def walkTo(params):
	if len(params) < 1:
		print 'Error: function \'walkTo\' takes 2 params'
		return 'Error: function \'walkTo\' takes 2 params'
	controlPoints = parse(params[0])
	return proxy.walkTo(controlPoints)

def walkTo(params):
	if len(params) < 2:
		print 'Error: function \'walkTo\' takes 2 params'
		return 'Error: function \'walkTo\' takes 2 params'
	controlPoints = parse(params[0])
	feetGaitConfig = parse(params[1])
	return proxy.walkTo(controlPoints,feetGaitConfig)

def setFootSteps(params):
	if len(params) < 4:
		print 'Error: function \'setFootSteps\' takes 2 params'
		return 'Error: function \'setFootSteps\' takes 2 params'
	legName = parse(params[0])
	footSteps = parse(params[1])
	timeList = parse(params[2])
	clearExisting = parse(params[3])
	return proxy.setFootSteps(legName,footSteps,timeList,clearExisting)

def setFootStepsWithSpeed(params):
	if len(params) < 4:
		print 'Error: function \'setFootStepsWithSpeed\' takes 2 params'
		return 'Error: function \'setFootStepsWithSpeed\' takes 2 params'
	legName = parse(params[0])
	footSteps = parse(params[1])
	fractionMaxSpeed = parse(params[2])
	clearExisting = parse(params[3])
	return proxy.setFootStepsWithSpeed(legName,footSteps,fractionMaxSpeed,clearExisting)

def getFootSteps(params):
	return proxy.getFootSteps()

def walkInit(params):
	return proxy.walkInit()

def moveInit(params):
	return proxy.moveInit()

def waitUntilWalkIsFinished(params):
	return proxy.waitUntilWalkIsFinished()

def waitUntilMoveIsFinished(params):
	return proxy.waitUntilMoveIsFinished()

def walkIsActive(params):
	return proxy.walkIsActive()

def moveIsActive(params):
	return proxy.moveIsActive()

def stopWalk(params):
	return proxy.stopWalk()

def stopMove(params):
	return proxy.stopMove()

def getFootGaitConfig(params):
	if len(params) < 1:
		print 'Error: function \'getFootGaitConfig\' takes 2 params'
		return 'Error: function \'getFootGaitConfig\' takes 2 params'
	config = parse(params[0])
	return proxy.getFootGaitConfig(config)

def getMoveConfig(params):
	if len(params) < 1:
		print 'Error: function \'getMoveConfig\' takes 2 params'
		return 'Error: function \'getMoveConfig\' takes 2 params'
	config = parse(params[0])
	return proxy.getMoveConfig(config)

def getRobotPosition(params):
	if len(params) < 1:
		print 'Error: function \'getRobotPosition\' takes 2 params'
		return 'Error: function \'getRobotPosition\' takes 2 params'
	useSensors = parse(params[0])
	return proxy.getRobotPosition(useSensors)

def getNextRobotPosition(params):
	return proxy.getNextRobotPosition()

def getRobotVelocity(params):
	return proxy.getRobotVelocity()

def getWalkArmsEnabled(params):
	return proxy.getWalkArmsEnabled()

def setWalkArmsEnabled(params):
	if len(params) < 2:
		print 'Error: function \'setWalkArmsEnabled\' takes 2 params'
		return 'Error: function \'setWalkArmsEnabled\' takes 2 params'
	leftArmEnable = parse(params[0])
	rightArmEnable = parse(params[1])
	return proxy.setWalkArmsEnabled(leftArmEnable,rightArmEnable)

def getMoveArmsEnabled(params):
	if len(params) < 1:
		print 'Error: function \'getMoveArmsEnabled\' takes 2 params'
		return 'Error: function \'getMoveArmsEnabled\' takes 2 params'
	chainName = parse(params[0])
	return proxy.getMoveArmsEnabled(chainName)

def setMoveArmsEnabled(params):
	if len(params) < 2:
		print 'Error: function \'setMoveArmsEnabled\' takes 2 params'
		return 'Error: function \'setMoveArmsEnabled\' takes 2 params'
	leftArmEnable = parse(params[0])
	rightArmEnable = parse(params[1])
	return proxy.setMoveArmsEnabled(leftArmEnable,rightArmEnable)

def positionInterpolation(params):
	if len(params) < 6:
		print 'Error: function \'positionInterpolation\' takes 2 params'
		return 'Error: function \'positionInterpolation\' takes 2 params'
	effectorName = parse(params[0])
	frame = parse(params[1])
	path = parse(params[2])
	axisMask = parse(params[3])
	durations = parse(params[4])
	isAbsolute = parse(params[5])
	return proxy.positionInterpolation(effectorName,frame,path,axisMask,durations,isAbsolute)

def positionInterpolations(params):
	if len(params) < 5:
		print 'Error: function \'positionInterpolations\' takes 2 params'
		return 'Error: function \'positionInterpolations\' takes 2 params'
	effectorNames = parse(params[0])
	frames = parse(params[1])
	paths = parse(params[2])
	axisMasks = parse(params[3])
	relativeTimes = parse(params[4])
	return proxy.positionInterpolations(effectorNames,frames,paths,axisMasks,relativeTimes)

def positionInterpolations(params):
	if len(params) < 6:
		print 'Error: function \'positionInterpolations\' takes 2 params'
		return 'Error: function \'positionInterpolations\' takes 2 params'
	effectorNames = parse(params[0])
	frame = parse(params[1])
	paths = parse(params[2])
	axisMasks = parse(params[3])
	relativeTimes = parse(params[4])
	isAbsolute = parse(params[5])
	return proxy.positionInterpolations(effectorNames,frame,paths,axisMasks,relativeTimes,isAbsolute)

def setPositions(params):
	if len(params) < 5:
		print 'Error: function \'setPositions\' takes 2 params'
		return 'Error: function \'setPositions\' takes 2 params'
	effectorNames = parse(params[0])
	frame = parse(params[1])
	position = parse(params[2])
	fractionMaxSpeed = parse(params[3])
	axisMask = parse(params[4])
	return proxy.setPositions(effectorNames,frame,position,fractionMaxSpeed,axisMask)

def setPosition(params):
	if len(params) < 5:
		print 'Error: function \'setPosition\' takes 2 params'
		return 'Error: function \'setPosition\' takes 2 params'
	effectorName = parse(params[0])
	frame = parse(params[1])
	position = parse(params[2])
	fractionMaxSpeed = parse(params[3])
	axisMask = parse(params[4])
	return proxy.setPosition(effectorName,frame,position,fractionMaxSpeed,axisMask)

def changePosition(params):
	if len(params) < 5:
		print 'Error: function \'changePosition\' takes 2 params'
		return 'Error: function \'changePosition\' takes 2 params'
	effectorName = parse(params[0])
	frame = parse(params[1])
	positionChange = parse(params[2])
	fractionMaxSpeed = parse(params[3])
	axisMask = parse(params[4])
	return proxy.changePosition(effectorName,frame,positionChange,fractionMaxSpeed,axisMask)

def getPosition(params):
	if len(params) < 3:
		print 'Error: function \'getPosition\' takes 2 params'
		return 'Error: function \'getPosition\' takes 2 params'
	name = parse(params[0])
	frame = parse(params[1])
	useSensorValues = parse(params[2])
	return proxy.getPosition(name,frame,useSensorValues)

def transformInterpolation(params):
	if len(params) < 6:
		print 'Error: function \'transformInterpolation\' takes 2 params'
		return 'Error: function \'transformInterpolation\' takes 2 params'
	effectorName = parse(params[0])
	frame = parse(params[1])
	path = parse(params[2])
	axisMask = parse(params[3])
	duration = parse(params[4])
	isAbsolute = parse(params[5])
	return proxy.transformInterpolation(effectorName,frame,path,axisMask,duration,isAbsolute)

def transformInterpolations(params):
	if len(params) < 5:
		print 'Error: function \'transformInterpolations\' takes 2 params'
		return 'Error: function \'transformInterpolations\' takes 2 params'
	effectorNames = parse(params[0])
	frames = parse(params[1])
	paths = parse(params[2])
	axisMasks = parse(params[3])
	relativeTimes = parse(params[4])
	return proxy.transformInterpolations(effectorNames,frames,paths,axisMasks,relativeTimes)

def transformInterpolations(params):
	if len(params) < 6:
		print 'Error: function \'transformInterpolations\' takes 2 params'
		return 'Error: function \'transformInterpolations\' takes 2 params'
	effectorNames = parse(params[0])
	frame = parse(params[1])
	paths = parse(params[2])
	axisMasks = parse(params[3])
	relativeTimes = parse(params[4])
	isAbsolute = parse(params[5])
	return proxy.transformInterpolations(effectorNames,frame,paths,axisMasks,relativeTimes,isAbsolute)

def setTransforms(params):
	if len(params) < 5:
		print 'Error: function \'setTransforms\' takes 2 params'
		return 'Error: function \'setTransforms\' takes 2 params'
	effectorName = parse(params[0])
	frame = parse(params[1])
	transform = parse(params[2])
	fractionMaxSpeed = parse(params[3])
	axisMask = parse(params[4])
	return proxy.setTransforms(effectorName,frame,transform,fractionMaxSpeed,axisMask)

def setTransform(params):
	if len(params) < 5:
		print 'Error: function \'setTransform\' takes 2 params'
		return 'Error: function \'setTransform\' takes 2 params'
	effectorName = parse(params[0])
	frame = parse(params[1])
	transform = parse(params[2])
	fractionMaxSpeed = parse(params[3])
	axisMask = parse(params[4])
	return proxy.setTransform(effectorName,frame,transform,fractionMaxSpeed,axisMask)

def changeTransform(params):
	if len(params) < 5:
		print 'Error: function \'changeTransform\' takes 2 params'
		return 'Error: function \'changeTransform\' takes 2 params'
	effectorName = parse(params[0])
	frame = parse(params[1])
	transform = parse(params[2])
	fractionMaxSpeed = parse(params[3])
	axisMask = parse(params[4])
	return proxy.changeTransform(effectorName,frame,transform,fractionMaxSpeed,axisMask)

def getTransform(params):
	if len(params) < 3:
		print 'Error: function \'getTransform\' takes 2 params'
		return 'Error: function \'getTransform\' takes 2 params'
	name = parse(params[0])
	frame = parse(params[1])
	useSensorValues = parse(params[2])
	return proxy.getTransform(name,frame,useSensorValues)

def wbEnable(params):
	if len(params) < 1:
		print 'Error: function \'wbEnable\' takes 2 params'
		return 'Error: function \'wbEnable\' takes 2 params'
	isEnabled = parse(params[0])
	return proxy.wbEnable(isEnabled)

def wbFootState(params):
	if len(params) < 2:
		print 'Error: function \'wbFootState\' takes 2 params'
		return 'Error: function \'wbFootState\' takes 2 params'
	stateName = parse(params[0])
	supportLeg = parse(params[1])
	return proxy.wbFootState(stateName,supportLeg)

def wbEnableBalanceConstraint(params):
	if len(params) < 2:
		print 'Error: function \'wbEnableBalanceConstraint\' takes 2 params'
		return 'Error: function \'wbEnableBalanceConstraint\' takes 2 params'
	isEnable = parse(params[0])
	supportLeg = parse(params[1])
	return proxy.wbEnableBalanceConstraint(isEnable,supportLeg)

def wbGoToBalance(params):
	if len(params) < 2:
		print 'Error: function \'wbGoToBalance\' takes 2 params'
		return 'Error: function \'wbGoToBalance\' takes 2 params'
	supportLeg = parse(params[0])
	duration = parse(params[1])
	return proxy.wbGoToBalance(supportLeg,duration)

def wbEnableEffectorControl(params):
	if len(params) < 2:
		print 'Error: function \'wbEnableEffectorControl\' takes 2 params'
		return 'Error: function \'wbEnableEffectorControl\' takes 2 params'
	effectorName = parse(params[0])
	isEnabled = parse(params[1])
	return proxy.wbEnableEffectorControl(effectorName,isEnabled)

def wbSetEffectorControl(params):
	if len(params) < 2:
		print 'Error: function \'wbSetEffectorControl\' takes 2 params'
		return 'Error: function \'wbSetEffectorControl\' takes 2 params'
	effectorName = parse(params[0])
	targetCoordinate = parse(params[1])
	return proxy.wbSetEffectorControl(effectorName,targetCoordinate)

def wbEnableEffectorOptimization(params):
	if len(params) < 2:
		print 'Error: function \'wbEnableEffectorOptimization\' takes 2 params'
		return 'Error: function \'wbEnableEffectorOptimization\' takes 2 params'
	effectorName = parse(params[0])
	isEnabled = parse(params[1])
	return proxy.wbEnableEffectorOptimization(effectorName,isEnabled)

