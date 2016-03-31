from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALTabletService', '127.0.0.1', PORT)

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

def cleanWebview(params):
	return proxy.cleanWebview()

def hideWebview(params):
	return proxy.hideWebview()

def loadApplication(params):
	if len(params) < 1:
		print 'Error: function \'loadApplication\' takes 2 params'
		return 'Error: function \'loadApplication\' takes 2 params'
	name = parse(params[0])
	return proxy.loadApplication(name)

def loadUrl(params):
	if len(params) < 1:
		print 'Error: function \'loadUrl\' takes 2 params'
		return 'Error: function \'loadUrl\' takes 2 params'
	url = parse(params[0])
	return proxy.loadUrl(url)

def showWebview(params):
	return proxy.showWebview()

def getVideoLength(params):
	return proxy.getVideoLength()

def getVideoPosition(params):
	return proxy.getVideoPosition()

def pauseVideo(params):
	return proxy.pauseVideo()

def playVideo(params):
	if len(params) < 1:
		print 'Error: function \'playVideo\' takes 2 params'
		return 'Error: function \'playVideo\' takes 2 params'
	url = parse(params[0])
	return proxy.playVideo(url)

def resumeVideo(params):
	return proxy.resumeVideo()

def stopVideo(params):
	return proxy.stopVideo()

def hideImage(params):
	return proxy.hideImage()

def pauseGif(params):
	return proxy.pauseGif()

def preLoadImage(params):
	if len(params) < 1:
		print 'Error: function \'preLoadImage\' takes 2 params'
		return 'Error: function \'preLoadImage\' takes 2 params'
	url = parse(params[0])
	return proxy.preLoadImage(url)

def resumeGif(params):
	return proxy.resumeGif()

def setBackgroundColor(params):
	if len(params) < 1:
		print 'Error: function \'setBackgroundColor\' takes 2 params'
		return 'Error: function \'setBackgroundColor\' takes 2 params'
	color = parse(params[0])
	return proxy.setBackgroundColor(color)

def showImage(params):
	if len(params) < 1:
		print 'Error: function \'showImage\' takes 2 params'
		return 'Error: function \'showImage\' takes 2 params'
	url = parse(params[0])
	return proxy.showImage(url)

def showAlertView(params):
	if len(params) < 3:
		print 'Error: function \'showAlertView\' takes 2 params'
		return 'Error: function \'showAlertView\' takes 2 params'
	radius = parse(params[0])
	color = parse(params[1])
	delay = parse(params[2])
	return proxy.showAlertView(radius,color,delay)

def showInputDialog(params):
	if len(params) < 4:
		print 'Error: function \'showInputDialog\' takes 2 params'
		return 'Error: function \'showInputDialog\' takes 2 params'
	type = parse(params[0])
	title = parse(params[1])
	ok = parse(params[2])
	cancel = parse(params[3])
	return proxy.showInputDialog(type,title,ok,cancel)

def showInputTextDialog(params):
	if len(params) < 3:
		print 'Error: function \'showInputTextDialog\' takes 2 params'
		return 'Error: function \'showInputTextDialog\' takes 2 params'
	title = parse(params[0])
	ok = parse(params[1])
	cancel = parse(params[2])
	return proxy.showInputTextDialog(title,ok,cancel)

def configureWifi(params):
	if len(params) < 3:
		print 'Error: function \'configureWifi\' takes 2 params'
		return 'Error: function \'configureWifi\' takes 2 params'
	security = parse(params[0])
	ssid = parse(params[1])
	key = parse(params[2])
	return proxy.configureWifi(security,ssid,key)

def disableWifi(params):
	return proxy.disableWifi()

def enableWifi(params):
	return proxy.enableWifi()

def forgetWifi(params):
	if len(params) < 1:
		print 'Error: function \'forgetWifi\' takes 2 params'
		return 'Error: function \'forgetWifi\' takes 2 params'
	ssid = parse(params[0])
	return proxy.forgetWifi(ssid)

def getWifiStatus(params):
	return proxy.getWifiStatus()

def getBrightness(params):
	return proxy.getBrightness()

def getCurrentLifeActivity(params):
	return proxy.getCurrentLifeActivity()

def hide(params):
	return proxy.hide()

def resetToDefaultValue(params):
	return proxy.resetToDefaultValue()

def robotIp(params):
	return proxy.robotIp()

def setBrightness(params):
	if len(params) < 1:
		print 'Error: function \'setBrightness\' takes 2 params'
		return 'Error: function \'setBrightness\' takes 2 params'
	newBrightness = parse(params[0])
	return proxy.setBrightness(newBrightness)

def setTabletLanguage(params):
	if len(params) < 1:
		print 'Error: function \'setTabletLanguage\' takes 2 params'
		return 'Error: function \'setTabletLanguage\' takes 2 params'
	language = parse(params[0])
	return proxy.setTabletLanguage(language)

def setVolume(params):
	if len(params) < 1:
		print 'Error: function \'setVolume\' takes 2 params'
		return 'Error: function \'setVolume\' takes 2 params'
	volume = parse(params[0])
	return proxy.setVolume(volume)

def version(params):
	return proxy.version()

def postEventToApplication(params):
	return proxy.postEventToApplication()

def getLastVideoErrorLog(params):
	return proxy.getLastVideoErrorLog()

def onTouchDown(params):
	if len(params) < 2:
		print 'Error: function \'onTouchDown\' takes 2 params'
		return 'Error: function \'onTouchDown\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	return proxy.onTouchDown(x,y)

def onTouchMove(params):
	if len(params) < 2:
		print 'Error: function \'onTouchMove\' takes 2 params'
		return 'Error: function \'onTouchMove\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	return proxy.onTouchMove(x,y)

def onTouchUp(params):
	if len(params) < 2:
		print 'Error: function \'onTouchUp\' takes 2 params'
		return 'Error: function \'onTouchUp\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	return proxy.onTouchUp(x,y)

def onTouch(params):
	if len(params) < 2:
		print 'Error: function \'onTouch\' takes 2 params'
		return 'Error: function \'onTouch\' takes 2 params'
	x = parse(params[0])
	y = parse(params[1])
	return proxy.onTouch(x,y)

def onConsoleMessage(params):
	if len(params) < 1:
		print 'Error: function \'onConsoleMessage\' takes 2 params'
		return 'Error: function \'onConsoleMessage\' takes 2 params'
	message = parse(params[0])
	return proxy.onConsoleMessage(message)

def onImageLoaded(params):
	return proxy.onImageLoaded()

def onInputText(params):
	if len(params) < 2:
		print 'Error: function \'onInputText\' takes 2 params'
		return 'Error: function \'onInputText\' takes 2 params'
	validation = parse(params[0])
	input = parse(params[1])
	return proxy.onInputText(validation,input)

def onPageFinished(params):
	return proxy.onPageFinished()

def onPageStarted(params):
	return proxy.onPageStarted()

def videoFinished(params):
	return proxy.videoFinished()

def videoStarted(params):
	return proxy.videoStarted()

