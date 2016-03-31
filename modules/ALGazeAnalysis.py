from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALGazeAnalysis', '127.0.0.1', PORT)

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

def getTolerance(params):
	return proxy.getTolerance()

def setTolerance(params):
	if len(params) < 1:
		print 'Error: function \'setTolerance\' takes 2 params'
		return 'Error: function \'setTolerance\' takes 2 params'
	tolerance = parse(params[0])
	return proxy.setTolerance(tolerance)

def isFaceAnalysisEnabled(params):
	return proxy.isFaceAnalysisEnabled()

def setFaceAnalysisEnabled(params):
	if len(params) < 1:
		print 'Error: function \'setFaceAnalysisEnabled\' takes 2 params'
		return 'Error: function \'setFaceAnalysisEnabled\' takes 2 params'
	status = parse(params[0])
	return proxy.setFaceAnalysisEnabled(status)

