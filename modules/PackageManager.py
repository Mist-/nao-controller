from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('PackageManager', '127.0.0.1', PORT)

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

def install(params):
	if len(params) < 1:
		print 'Error: function \'install\' takes 2 params'
		return 'Error: function \'install\' takes 2 params'
	path = parse(params[0])
	return proxy.install(path)

def installCheckMd5(params):
	if len(params) < 2:
		print 'Error: function \'installCheckMd5\' takes 2 params'
		return 'Error: function \'installCheckMd5\' takes 2 params'
	path = parse(params[0])
	md5 = parse(params[1])
	return proxy.installCheckMd5(path,md5)

def hasPackage(params):
	if len(params) < 1:
		print 'Error: function \'hasPackage\' takes 2 params'
		return 'Error: function \'hasPackage\' takes 2 params'
	uuid = parse(params[0])
	return proxy.hasPackage(uuid)

def removePkg(params):
	if len(params) < 1:
		print 'Error: function \'removePkg\' takes 2 params'
		return 'Error: function \'removePkg\' takes 2 params'
	uuid = parse(params[0])
	return proxy.removePkg(uuid)

def packages2(params):
	return proxy.packages2()

def package2(params):
	if len(params) < 1:
		print 'Error: function \'package2\' takes 2 params'
		return 'Error: function \'package2\' takes 2 params'
	uuid = parse(params[0])
	return proxy.package2(uuid)

def packages(params):
	return proxy.packages()

def package(params):
	if len(params) < 1:
		print 'Error: function \'package\' takes 2 params'
		return 'Error: function \'package\' takes 2 params'
	uuid = parse(params[0])
	return proxy.package(uuid)

def packageIcon(params):
	if len(params) < 1:
		print 'Error: function \'packageIcon\' takes 2 params'
		return 'Error: function \'packageIcon\' takes 2 params'
	uuid = parse(params[0])
	return proxy.packageIcon(uuid)

