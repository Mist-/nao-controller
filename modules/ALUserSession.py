from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALUserSession', '127.0.0.1', PORT)

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

def doUsersExist(params):
	if len(params) < 1:
		print 'Error: function \'doUsersExist\' takes 2 params'
		return 'Error: function \'doUsersExist\' takes 2 params'
	userIDs = parse(params[0])
	return proxy.doUsersExist(userIDs)

def getUserList(params):
	return proxy.getUserList()

def getNumUsers(params):
	return proxy.getNumUsers()

def getFocusedUser(params):
	return proxy.getFocusedUser()

def getOpenUserSessions(params):
	return proxy.getOpenUserSessions()

def areUserSessionsOpen(params):
	if len(params) < 1:
		print 'Error: function \'areUserSessionsOpen\' takes 2 params'
		return 'Error: function \'areUserSessionsOpen\' takes 2 params'
	userIDs = parse(params[0])
	return proxy.areUserSessionsOpen(userIDs)

def getBindingSources(params):
	return proxy.getBindingSources()

def doesBindingSourceExist(params):
	if len(params) < 1:
		print 'Error: function \'doesBindingSourceExist\' takes 2 params'
		return 'Error: function \'doesBindingSourceExist\' takes 2 params'
	bindingName = parse(params[0])
	return proxy.doesBindingSourceExist(bindingName)

def getUserBindings(params):
	if len(params) < 1:
		print 'Error: function \'getUserBindings\' takes 2 params'
		return 'Error: function \'getUserBindings\' takes 2 params'
	userID = parse(params[0])
	return proxy.getUserBindings(userID)

def getUserBinding(params):
	if len(params) < 2:
		print 'Error: function \'getUserBinding\' takes 2 params'
		return 'Error: function \'getUserBinding\' takes 2 params'
	userID = parse(params[0])
	bindingName = parse(params[1])
	return proxy.getUserBinding(userID,bindingName)

def findUsersWithBinding(params):
	if len(params) < 2:
		print 'Error: function \'findUsersWithBinding\' takes 2 params'
		return 'Error: function \'findUsersWithBinding\' takes 2 params'
	bindingName = parse(params[0])
	bindingValue = parse(params[1])
	return proxy.findUsersWithBinding(bindingName,bindingValue)

def doesUserDataSourceExist(params):
	if len(params) < 1:
		print 'Error: function \'doesUserDataSourceExist\' takes 2 params'
		return 'Error: function \'doesUserDataSourceExist\' takes 2 params'
	sourceName = parse(params[0])
	return proxy.doesUserDataSourceExist(sourceName)

def getUserDataSources(params):
	return proxy.getUserDataSources()

def getUserData(params):
	if len(params) < 3:
		print 'Error: function \'getUserData\' takes 2 params'
		return 'Error: function \'getUserData\' takes 2 params'
	userID = parse(params[0])
	dataName = parse(params[1])
	sourceName = parse(params[2])
	return proxy.getUserData(userID,dataName,sourceName)

def getUserData(params):
	if len(params) < 2:
		print 'Error: function \'getUserData\' takes 2 params'
		return 'Error: function \'getUserData\' takes 2 params'
	userID = parse(params[0])
	dataName = parse(params[1])
	return proxy.getUserData(userID,dataName)

