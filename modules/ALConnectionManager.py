from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALConnectionManager', '127.0.0.1', PORT)

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

def state(params):
	return proxy.state()

def scan(params):
	return proxy.scan()

def services(params):
	return proxy.services()

def technologies(params):
	return proxy.technologies()

def service(params):
	if len(params) < 1:
		print 'Error: function \'service\' takes 2 params'
		return 'Error: function \'service\' takes 2 params'
	serviceId = parse(params[0])
	return proxy.service(serviceId)

def connect(params):
	if len(params) < 1:
		print 'Error: function \'connect\' takes 2 params'
		return 'Error: function \'connect\' takes 2 params'
	serviceId = parse(params[0])
	return proxy.connect(serviceId)

def disconnect(params):
	if len(params) < 1:
		print 'Error: function \'disconnect\' takes 2 params'
		return 'Error: function \'disconnect\' takes 2 params'
	serviceId = parse(params[0])
	return proxy.disconnect(serviceId)

def forget(params):
	if len(params) < 1:
		print 'Error: function \'forget\' takes 2 params'
		return 'Error: function \'forget\' takes 2 params'
	serviceId = parse(params[0])
	return proxy.forget(serviceId)

def setServiceConfiguration(params):
	if len(params) < 1:
		print 'Error: function \'setServiceConfiguration\' takes 2 params'
		return 'Error: function \'setServiceConfiguration\' takes 2 params'
	configuration = parse(params[0])
	return proxy.setServiceConfiguration(configuration)

def setServiceInput(params):
	if len(params) < 1:
		print 'Error: function \'setServiceInput\' takes 2 params'
		return 'Error: function \'setServiceInput\' takes 2 params'
	input = parse(params[0])
	return proxy.setServiceInput(input)

def scan(params):
	if len(params) < 1:
		print 'Error: function \'scan\' takes 2 params'
		return 'Error: function \'scan\' takes 2 params'
	technology = parse(params[0])
	return proxy.scan(technology)

def enableTethering(params):
	if len(params) < 1:
		print 'Error: function \'enableTethering\' takes 2 params'
		return 'Error: function \'enableTethering\' takes 2 params'
	technology = parse(params[0])
	return proxy.enableTethering(technology)

def enableTethering(params):
	if len(params) < 3:
		print 'Error: function \'enableTethering\' takes 2 params'
		return 'Error: function \'enableTethering\' takes 2 params'
	technology = parse(params[0])
	name = parse(params[1])
	passphrase = parse(params[2])
	return proxy.enableTethering(technology,name,passphrase)

def disableTethering(params):
	if len(params) < 1:
		print 'Error: function \'disableTethering\' takes 2 params'
		return 'Error: function \'disableTethering\' takes 2 params'
	technology = parse(params[0])
	return proxy.disableTethering(technology)

def getTetheringEnable(params):
	if len(params) < 1:
		print 'Error: function \'getTetheringEnable\' takes 2 params'
		return 'Error: function \'getTetheringEnable\' takes 2 params'
	technology = parse(params[0])
	return proxy.getTetheringEnable(technology)

def tetheringName(params):
	if len(params) < 1:
		print 'Error: function \'tetheringName\' takes 2 params'
		return 'Error: function \'tetheringName\' takes 2 params'
	technology = parse(params[0])
	return proxy.tetheringName(technology)

def tetheringPassphrase(params):
	if len(params) < 1:
		print 'Error: function \'tetheringPassphrase\' takes 2 params'
		return 'Error: function \'tetheringPassphrase\' takes 2 params'
	technology = parse(params[0])
	return proxy.tetheringPassphrase(technology)

def countries(params):
	return proxy.countries()

def country(params):
	return proxy.country()

def setCountry(params):
	if len(params) < 1:
		print 'Error: function \'setCountry\' takes 2 params'
		return 'Error: function \'setCountry\' takes 2 params'
	country = parse(params[0])
	return proxy.setCountry(country)

def interfaces(params):
	return proxy.interfaces()

