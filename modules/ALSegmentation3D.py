from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALSegmentation3D', '127.0.0.1', PORT)

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

def getDeltaDepthThreshold(params):
	return proxy.getDeltaDepthThreshold()

def getBlobTrackingDistance(params):
	return proxy.getBlobTrackingDistance()

def getTopOfBlob(params):
	if len(params) < 3:
		print 'Error: function \'getTopOfBlob\' takes 2 params'
		return 'Error: function \'getTopOfBlob\' takes 2 params'
	dist = parse(params[0])
	frame = parse(params[1])
	applyVerticalOffset = parse(params[2])
	return proxy.getTopOfBlob(dist,frame,applyVerticalOffset)

def getVerticalOffset(params):
	return proxy.getVerticalOffset()

def isBlobTrackingEnabled(params):
	return proxy.isBlobTrackingEnabled()

def setBlobTrackingDistance(params):
	if len(params) < 1:
		print 'Error: function \'setBlobTrackingDistance\' takes 2 params'
		return 'Error: function \'setBlobTrackingDistance\' takes 2 params'
	distance = parse(params[0])
	return proxy.setBlobTrackingDistance(distance)

def setBlobTrackingEnabled(params):
	if len(params) < 1:
		print 'Error: function \'setBlobTrackingEnabled\' takes 2 params'
		return 'Error: function \'setBlobTrackingEnabled\' takes 2 params'
	status = parse(params[0])
	return proxy.setBlobTrackingEnabled(status)

def setDeltaDepthThreshold(params):
	if len(params) < 1:
		print 'Error: function \'setDeltaDepthThreshold\' takes 2 params'
		return 'Error: function \'setDeltaDepthThreshold\' takes 2 params'
	threshold = parse(params[0])
	return proxy.setDeltaDepthThreshold(threshold)

def setVerticalOffset(params):
	if len(params) < 1:
		print 'Error: function \'setVerticalOffset\' takes 2 params'
		return 'Error: function \'setVerticalOffset\' takes 2 params'
	offset = parse(params[0])
	return proxy.setVerticalOffset(offset)

