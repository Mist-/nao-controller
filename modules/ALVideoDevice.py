from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALVideoDevice', '127.0.0.1', PORT)

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

def subscribeCamera(params):
	if len(params) < 5:
		print 'Error: function \'subscribeCamera\' takes 2 params'
		return 'Error: function \'subscribeCamera\' takes 2 params'
	Name = parse(params[0])
	CameraIndex = parse(params[1])
	Resolution = parse(params[2])
	ColorSpace = parse(params[3])
	Fps = parse(params[4])
	return proxy.subscribeCamera(Name,CameraIndex,Resolution,ColorSpace,Fps)

def subscribeCameras(params):
	if len(params) < 5:
		print 'Error: function \'subscribeCameras\' takes 2 params'
		return 'Error: function \'subscribeCameras\' takes 2 params'
	Name = parse(params[0])
	CameraIndexes = parse(params[1])
	Resolutions = parse(params[2])
	ColorSpaces = parse(params[3])
	Fps = parse(params[4])
	return proxy.subscribeCameras(Name,CameraIndexes,Resolutions,ColorSpaces,Fps)

def unsubscribe(params):
	if len(params) < 1:
		print 'Error: function \'unsubscribe\' takes 2 params'
		return 'Error: function \'unsubscribe\' takes 2 params'
	Handle = parse(params[0])
	return proxy.unsubscribe(Handle)

def getSubscribers(params):
	return proxy.getSubscribers()

def getCameraIndexes(params):
	return proxy.getCameraIndexes()

def hasDepthCamera(params):
	return proxy.hasDepthCamera()

def getCameraModel(params):
	if len(params) < 1:
		print 'Error: function \'getCameraModel\' takes 2 params'
		return 'Error: function \'getCameraModel\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.getCameraModel(CameraIndex)

def getCameraName(params):
	if len(params) < 1:
		print 'Error: function \'getCameraName\' takes 2 params'
		return 'Error: function \'getCameraName\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.getCameraName(CameraIndex)

def getActiveCamera(params):
	return proxy.getActiveCamera()

def setActiveCamera(params):
	if len(params) < 1:
		print 'Error: function \'setActiveCamera\' takes 2 params'
		return 'Error: function \'setActiveCamera\' takes 2 params'
	ActiveCamera = parse(params[0])
	return proxy.setActiveCamera(ActiveCamera)

def getFrameRate(params):
	if len(params) < 1:
		print 'Error: function \'getFrameRate\' takes 2 params'
		return 'Error: function \'getFrameRate\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.getFrameRate(CameraIndex)

def getResolution(params):
	if len(params) < 1:
		print 'Error: function \'getResolution\' takes 2 params'
		return 'Error: function \'getResolution\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.getResolution(CameraIndex)

def getColorSpace(params):
	if len(params) < 1:
		print 'Error: function \'getColorSpace\' takes 2 params'
		return 'Error: function \'getColorSpace\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.getColorSpace(CameraIndex)

def getHorizontalFOV(params):
	if len(params) < 1:
		print 'Error: function \'getHorizontalFOV\' takes 2 params'
		return 'Error: function \'getHorizontalFOV\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.getHorizontalFOV(CameraIndex)

def getVerticalFOV(params):
	if len(params) < 1:
		print 'Error: function \'getVerticalFOV\' takes 2 params'
		return 'Error: function \'getVerticalFOV\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.getVerticalFOV(CameraIndex)

def getParameter(params):
	if len(params) < 2:
		print 'Error: function \'getParameter\' takes 2 params'
		return 'Error: function \'getParameter\' takes 2 params'
	CameraIndex = parse(params[0])
	parameter = parse(params[1])
	return proxy.getParameter(CameraIndex,parameter)

def getParameterRange(params):
	if len(params) < 2:
		print 'Error: function \'getParameterRange\' takes 2 params'
		return 'Error: function \'getParameterRange\' takes 2 params'
	CameraIndex = parse(params[0])
	Id = parse(params[1])
	return proxy.getParameterRange(CameraIndex,Id)

def setParameter(params):
	if len(params) < 3:
		print 'Error: function \'setParameter\' takes 2 params'
		return 'Error: function \'setParameter\' takes 2 params'
	CameraIndex = parse(params[0])
	parameter = parse(params[1])
	newValue = parse(params[2])
	return proxy.setParameter(CameraIndex,parameter,newValue)

def setParameterToDefault(params):
	if len(params) < 2:
		print 'Error: function \'setParameterToDefault\' takes 2 params'
		return 'Error: function \'setParameterToDefault\' takes 2 params'
	CameraIndex = parse(params[0])
	parameter = parse(params[1])
	return proxy.setParameterToDefault(CameraIndex,parameter)

def setAllParametersToDefault(params):
	if len(params) < 1:
		print 'Error: function \'setAllParametersToDefault\' takes 2 params'
		return 'Error: function \'setAllParametersToDefault\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.setAllParametersToDefault(CameraIndex)

def openCamera(params):
	if len(params) < 1:
		print 'Error: function \'openCamera\' takes 2 params'
		return 'Error: function \'openCamera\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.openCamera(CameraIndex)

def closeCamera(params):
	if len(params) < 1:
		print 'Error: function \'closeCamera\' takes 2 params'
		return 'Error: function \'closeCamera\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.closeCamera(CameraIndex)

def isCameraOpen(params):
	if len(params) < 1:
		print 'Error: function \'isCameraOpen\' takes 2 params'
		return 'Error: function \'isCameraOpen\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.isCameraOpen(CameraIndex)

def startCamera(params):
	if len(params) < 1:
		print 'Error: function \'startCamera\' takes 2 params'
		return 'Error: function \'startCamera\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.startCamera(CameraIndex)

def stopCamera(params):
	if len(params) < 1:
		print 'Error: function \'stopCamera\' takes 2 params'
		return 'Error: function \'stopCamera\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.stopCamera(CameraIndex)

def isCameraStarted(params):
	if len(params) < 1:
		print 'Error: function \'isCameraStarted\' takes 2 params'
		return 'Error: function \'isCameraStarted\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.isCameraStarted(CameraIndex)

def getActiveCamera(params):
	if len(params) < 1:
		print 'Error: function \'getActiveCamera\' takes 2 params'
		return 'Error: function \'getActiveCamera\' takes 2 params'
	Handle = parse(params[0])
	return proxy.getActiveCamera(Handle)

def setActiveCamera(params):
	if len(params) < 2:
		print 'Error: function \'setActiveCamera\' takes 2 params'
		return 'Error: function \'setActiveCamera\' takes 2 params'
	Handle = parse(params[0])
	ActiveCamera = parse(params[1])
	return proxy.setActiveCamera(Handle,ActiveCamera)

def getFrameRate(params):
	if len(params) < 1:
		print 'Error: function \'getFrameRate\' takes 2 params'
		return 'Error: function \'getFrameRate\' takes 2 params'
	Handle = parse(params[0])
	return proxy.getFrameRate(Handle)

def setFrameRate(params):
	if len(params) < 2:
		print 'Error: function \'setFrameRate\' takes 2 params'
		return 'Error: function \'setFrameRate\' takes 2 params'
	Handle = parse(params[0])
	Fps = parse(params[1])
	return proxy.setFrameRate(Handle,Fps)

def getResolution(params):
	if len(params) < 1:
		print 'Error: function \'getResolution\' takes 2 params'
		return 'Error: function \'getResolution\' takes 2 params'
	Handle = parse(params[0])
	return proxy.getResolution(Handle)

def setResolution(params):
	if len(params) < 2:
		print 'Error: function \'setResolution\' takes 2 params'
		return 'Error: function \'setResolution\' takes 2 params'
	Handle = parse(params[0])
	Resolution = parse(params[1])
	return proxy.setResolution(Handle,Resolution)

def getColorSpace(params):
	if len(params) < 1:
		print 'Error: function \'getColorSpace\' takes 2 params'
		return 'Error: function \'getColorSpace\' takes 2 params'
	Handle = parse(params[0])
	return proxy.getColorSpace(Handle)

def setColorSpace(params):
	if len(params) < 2:
		print 'Error: function \'setColorSpace\' takes 2 params'
		return 'Error: function \'setColorSpace\' takes 2 params'
	Handle = parse(params[0])
	ColorSpace = parse(params[1])
	return proxy.setColorSpace(Handle,ColorSpace)

def getCameraParameter(params):
	if len(params) < 2:
		print 'Error: function \'getCameraParameter\' takes 2 params'
		return 'Error: function \'getCameraParameter\' takes 2 params'
	Handle = parse(params[0])
	Id = parse(params[1])
	return proxy.getCameraParameter(Handle,Id)

def getCameraParameterRange(params):
	if len(params) < 2:
		print 'Error: function \'getCameraParameterRange\' takes 2 params'
		return 'Error: function \'getCameraParameterRange\' takes 2 params'
	Handle = parse(params[0])
	Id = parse(params[1])
	return proxy.getCameraParameterRange(Handle,Id)

def setCameraParameter(params):
	if len(params) < 3:
		print 'Error: function \'setCameraParameter\' takes 2 params'
		return 'Error: function \'setCameraParameter\' takes 2 params'
	Handle = parse(params[0])
	Id = parse(params[1])
	NewValue = parse(params[2])
	return proxy.setCameraParameter(Handle,Id,NewValue)

def setCameraParameterToDefault(params):
	if len(params) < 2:
		print 'Error: function \'setCameraParameterToDefault\' takes 2 params'
		return 'Error: function \'setCameraParameterToDefault\' takes 2 params'
	Handle = parse(params[0])
	Id = parse(params[1])
	return proxy.setCameraParameterToDefault(Handle,Id)

def setAllCameraParametersToDefault(params):
	if len(params) < 1:
		print 'Error: function \'setAllCameraParametersToDefault\' takes 2 params'
		return 'Error: function \'setAllCameraParametersToDefault\' takes 2 params'
	Handle = parse(params[0])
	return proxy.setAllCameraParametersToDefault(Handle)

def getDirectRawImageLocal(params):
	if len(params) < 1:
		print 'Error: function \'getDirectRawImageLocal\' takes 2 params'
		return 'Error: function \'getDirectRawImageLocal\' takes 2 params'
	Handle = parse(params[0])
	return proxy.getDirectRawImageLocal(Handle)

def getDirectRawImageRemote(params):
	if len(params) < 1:
		print 'Error: function \'getDirectRawImageRemote\' takes 2 params'
		return 'Error: function \'getDirectRawImageRemote\' takes 2 params'
	Handle = parse(params[0])
	return proxy.getDirectRawImageRemote(Handle)

def releaseDirectRawImage(params):
	if len(params) < 1:
		print 'Error: function \'releaseDirectRawImage\' takes 2 params'
		return 'Error: function \'releaseDirectRawImage\' takes 2 params'
	Handle = parse(params[0])
	return proxy.releaseDirectRawImage(Handle)

def getImageLocal(params):
	if len(params) < 1:
		print 'Error: function \'getImageLocal\' takes 2 params'
		return 'Error: function \'getImageLocal\' takes 2 params'
	Handle = parse(params[0])
	return proxy.getImageLocal(Handle)

def getImageRemote(params):
	if len(params) < 1:
		print 'Error: function \'getImageRemote\' takes 2 params'
		return 'Error: function \'getImageRemote\' takes 2 params'
	Handle = parse(params[0])
	return proxy.getImageRemote(Handle)

def releaseImage(params):
	if len(params) < 1:
		print 'Error: function \'releaseImage\' takes 2 params'
		return 'Error: function \'releaseImage\' takes 2 params'
	Handle = parse(params[0])
	return proxy.releaseImage(Handle)

def getActiveCameras(params):
	if len(params) < 1:
		print 'Error: function \'getActiveCameras\' takes 2 params'
		return 'Error: function \'getActiveCameras\' takes 2 params'
	Handle = parse(params[0])
	return proxy.getActiveCameras(Handle)

def setActiveCameras(params):
	if len(params) < 2:
		print 'Error: function \'setActiveCameras\' takes 2 params'
		return 'Error: function \'setActiveCameras\' takes 2 params'
	Handle = parse(params[0])
	ActiveCameras = parse(params[1])
	return proxy.setActiveCameras(Handle,ActiveCameras)

def getResolutions(params):
	if len(params) < 1:
		print 'Error: function \'getResolutions\' takes 2 params'
		return 'Error: function \'getResolutions\' takes 2 params'
	Handle = parse(params[0])
	return proxy.getResolutions(Handle)

def setResolutions(params):
	if len(params) < 2:
		print 'Error: function \'setResolutions\' takes 2 params'
		return 'Error: function \'setResolutions\' takes 2 params'
	Handle = parse(params[0])
	Resolutions = parse(params[1])
	return proxy.setResolutions(Handle,Resolutions)

def getColorSpaces(params):
	if len(params) < 1:
		print 'Error: function \'getColorSpaces\' takes 2 params'
		return 'Error: function \'getColorSpaces\' takes 2 params'
	Handle = parse(params[0])
	return proxy.getColorSpaces(Handle)

def setColorSpaces(params):
	if len(params) < 2:
		print 'Error: function \'setColorSpaces\' takes 2 params'
		return 'Error: function \'setColorSpaces\' takes 2 params'
	Handle = parse(params[0])
	ColorSpaces = parse(params[1])
	return proxy.setColorSpaces(Handle,ColorSpaces)

def getCamerasParameter(params):
	if len(params) < 2:
		print 'Error: function \'getCamerasParameter\' takes 2 params'
		return 'Error: function \'getCamerasParameter\' takes 2 params'
	Handle = parse(params[0])
	Id = parse(params[1])
	return proxy.getCamerasParameter(Handle,Id)

def setCamerasParameter(params):
	if len(params) < 3:
		print 'Error: function \'setCamerasParameter\' takes 2 params'
		return 'Error: function \'setCamerasParameter\' takes 2 params'
	Handle = parse(params[0])
	Id = parse(params[1])
	NewValue = parse(params[2])
	return proxy.setCamerasParameter(Handle,Id,NewValue)

def setCamerasParameterToDefault(params):
	if len(params) < 2:
		print 'Error: function \'setCamerasParameterToDefault\' takes 2 params'
		return 'Error: function \'setCamerasParameterToDefault\' takes 2 params'
	Handle = parse(params[0])
	Id = parse(params[1])
	return proxy.setCamerasParameterToDefault(Handle,Id)

def getDirectRawImagesLocal(params):
	if len(params) < 1:
		print 'Error: function \'getDirectRawImagesLocal\' takes 2 params'
		return 'Error: function \'getDirectRawImagesLocal\' takes 2 params'
	Handle = parse(params[0])
	return proxy.getDirectRawImagesLocal(Handle)

def getDirectRawImagesRemote(params):
	if len(params) < 1:
		print 'Error: function \'getDirectRawImagesRemote\' takes 2 params'
		return 'Error: function \'getDirectRawImagesRemote\' takes 2 params'
	Handle = parse(params[0])
	return proxy.getDirectRawImagesRemote(Handle)

def releaseDirectRawImages(params):
	if len(params) < 1:
		print 'Error: function \'releaseDirectRawImages\' takes 2 params'
		return 'Error: function \'releaseDirectRawImages\' takes 2 params'
	Handle = parse(params[0])
	return proxy.releaseDirectRawImages(Handle)

def getImagesLocal(params):
	if len(params) < 1:
		print 'Error: function \'getImagesLocal\' takes 2 params'
		return 'Error: function \'getImagesLocal\' takes 2 params'
	Handle = parse(params[0])
	return proxy.getImagesLocal(Handle)

def getImagesRemote(params):
	if len(params) < 1:
		print 'Error: function \'getImagesRemote\' takes 2 params'
		return 'Error: function \'getImagesRemote\' takes 2 params'
	Handle = parse(params[0])
	return proxy.getImagesRemote(Handle)

def releaseImages(params):
	if len(params) < 1:
		print 'Error: function \'releaseImages\' takes 2 params'
		return 'Error: function \'releaseImages\' takes 2 params'
	Handle = parse(params[0])
	return proxy.releaseImages(Handle)

def putImage(params):
	if len(params) < 4:
		print 'Error: function \'putImage\' takes 2 params'
		return 'Error: function \'putImage\' takes 2 params'
	CameraIndex = parse(params[0])
	Width = parse(params[1])
	Height = parse(params[2])
	ImageBuffer = parse(params[3])
	return proxy.putImage(CameraIndex,Width,Height,ImageBuffer)

def getExpectedImageParameters(params):
	if len(params) < 1:
		print 'Error: function \'getExpectedImageParameters\' takes 2 params'
		return 'Error: function \'getExpectedImageParameters\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.getExpectedImageParameters(CameraIndex)

def getAngularPositionFromImagePosition(params):
	if len(params) < 2:
		print 'Error: function \'getAngularPositionFromImagePosition\' takes 2 params'
		return 'Error: function \'getAngularPositionFromImagePosition\' takes 2 params'
	CameraIndex = parse(params[0])
	ImagePosition = parse(params[1])
	return proxy.getAngularPositionFromImagePosition(CameraIndex,ImagePosition)

def getImagePositionFromAngularPosition(params):
	if len(params) < 2:
		print 'Error: function \'getImagePositionFromAngularPosition\' takes 2 params'
		return 'Error: function \'getImagePositionFromAngularPosition\' takes 2 params'
	CameraIndex = parse(params[0])
	AngularPosition = parse(params[1])
	return proxy.getImagePositionFromAngularPosition(CameraIndex,AngularPosition)

def getAngularSizeFromImageSize(params):
	if len(params) < 2:
		print 'Error: function \'getAngularSizeFromImageSize\' takes 2 params'
		return 'Error: function \'getAngularSizeFromImageSize\' takes 2 params'
	CameraIndex = parse(params[0])
	ImageSize = parse(params[1])
	return proxy.getAngularSizeFromImageSize(CameraIndex,ImageSize)

def getImageSizeFromAngularSize(params):
	if len(params) < 2:
		print 'Error: function \'getImageSizeFromAngularSize\' takes 2 params'
		return 'Error: function \'getImageSizeFromAngularSize\' takes 2 params'
	CameraIndex = parse(params[0])
	AngularSize = parse(params[1])
	return proxy.getImageSizeFromAngularSize(CameraIndex,AngularSize)

def getImageInfoFromAngularInfo(params):
	if len(params) < 2:
		print 'Error: function \'getImageInfoFromAngularInfo\' takes 2 params'
		return 'Error: function \'getImageInfoFromAngularInfo\' takes 2 params'
	CameraIndex = parse(params[0])
	AngularInfo = parse(params[1])
	return proxy.getImageInfoFromAngularInfo(CameraIndex,AngularInfo)

def getImageInfoFromAngularInfoWithResolution(params):
	if len(params) < 3:
		print 'Error: function \'getImageInfoFromAngularInfoWithResolution\' takes 2 params'
		return 'Error: function \'getImageInfoFromAngularInfoWithResolution\' takes 2 params'
	CameraIndex = parse(params[0])
	AngularInfo = parse(params[1])
	ResolutionIndex = parse(params[2])
	return proxy.getImageInfoFromAngularInfoWithResolution(CameraIndex,AngularInfo,ResolutionIndex)

def onClientDisconnected(params):
	if len(params) < 3:
		print 'Error: function \'onClientDisconnected\' takes 2 params'
		return 'Error: function \'onClientDisconnected\' takes 2 params'
	eventName = parse(params[0])
	eventContents = parse(params[1])
	message = parse(params[2])
	return proxy.onClientDisconnected(eventName,eventContents,message)

def subscribe(params):
	if len(params) < 4:
		print 'Error: function \'subscribe\' takes 2 params'
		return 'Error: function \'subscribe\' takes 2 params'
	Name = parse(params[0])
	resolution = parse(params[1])
	colorSpace = parse(params[2])
	fps = parse(params[3])
	return proxy.subscribe(Name,resolution,colorSpace,fps)

def unsubscribeAllInstances(params):
	if len(params) < 1:
		print 'Error: function \'unsubscribeAllInstances\' takes 2 params'
		return 'Error: function \'unsubscribeAllInstances\' takes 2 params'
	Name = parse(params[0])
	return proxy.unsubscribeAllInstances(Name)

def getVIMResolution(params):
	return proxy.getVIMResolution()

def getVIMColorSpace(params):
	return proxy.getVIMColorSpace()

def getVIMFrameRate(params):
	return proxy.getVIMFrameRate()

def getGVMResolution(params):
	if len(params) < 1:
		print 'Error: function \'getGVMResolution\' takes 2 params'
		return 'Error: function \'getGVMResolution\' takes 2 params'
	id = parse(params[0])
	return proxy.getGVMResolution(id)

def getGVMColorSpace(params):
	if len(params) < 1:
		print 'Error: function \'getGVMColorSpace\' takes 2 params'
		return 'Error: function \'getGVMColorSpace\' takes 2 params'
	id = parse(params[0])
	return proxy.getGVMColorSpace(id)

def getGVMFrameRate(params):
	if len(params) < 1:
		print 'Error: function \'getGVMFrameRate\' takes 2 params'
		return 'Error: function \'getGVMFrameRate\' takes 2 params'
	id = parse(params[0])
	return proxy.getGVMFrameRate(id)

def startFrameGrabber(params):
	if len(params) < 1:
		print 'Error: function \'startFrameGrabber\' takes 2 params'
		return 'Error: function \'startFrameGrabber\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.startFrameGrabber(CameraIndex)

def stopFrameGrabber(params):
	if len(params) < 1:
		print 'Error: function \'stopFrameGrabber\' takes 2 params'
		return 'Error: function \'stopFrameGrabber\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.stopFrameGrabber(CameraIndex)

def isFrameGrabberOff(params):
	if len(params) < 1:
		print 'Error: function \'isFrameGrabberOff\' takes 2 params'
		return 'Error: function \'isFrameGrabberOff\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.isFrameGrabberOff(CameraIndex)

def getCameraModelID(params):
	return proxy.getCameraModelID()

def getParam(params):
	if len(params) < 1:
		print 'Error: function \'getParam\' takes 2 params'
		return 'Error: function \'getParam\' takes 2 params'
	Param = parse(params[0])
	return proxy.getParam(Param)

def setParam(params):
	if len(params) < 2:
		print 'Error: function \'setParam\' takes 2 params'
		return 'Error: function \'setParam\' takes 2 params'
	Param = parse(params[0])
	NewValue = parse(params[1])
	return proxy.setParam(Param,NewValue)

def setParamDefault(params):
	if len(params) < 1:
		print 'Error: function \'setParamDefault\' takes 2 params'
		return 'Error: function \'setParamDefault\' takes 2 params'
	Param = parse(params[0])
	return proxy.setParamDefault(Param)

def getAngPosFromImgPos(params):
	if len(params) < 1:
		print 'Error: function \'getAngPosFromImgPos\' takes 2 params'
		return 'Error: function \'getAngPosFromImgPos\' takes 2 params'
	imgPos = parse(params[0])
	return proxy.getAngPosFromImgPos(imgPos)

def getAngSizeFromImgSize(params):
	if len(params) < 1:
		print 'Error: function \'getAngSizeFromImgSize\' takes 2 params'
		return 'Error: function \'getAngSizeFromImgSize\' takes 2 params'
	imgSize = parse(params[0])
	return proxy.getAngSizeFromImgSize(imgSize)

def getImgInfoFromAngInfo(params):
	if len(params) < 1:
		print 'Error: function \'getImgInfoFromAngInfo\' takes 2 params'
		return 'Error: function \'getImgInfoFromAngInfo\' takes 2 params'
	angles = parse(params[0])
	return proxy.getImgInfoFromAngInfo(angles)

def getImgInfoFromAngInfoWithRes(params):
	if len(params) < 2:
		print 'Error: function \'getImgInfoFromAngInfoWithRes\' takes 2 params'
		return 'Error: function \'getImgInfoFromAngInfoWithRes\' takes 2 params'
	angInfo = parse(params[0])
	resIndex = parse(params[1])
	return proxy.getImgInfoFromAngInfoWithRes(angInfo,resIndex)

def getImgPosFromAngPos(params):
	if len(params) < 1:
		print 'Error: function \'getImgPosFromAngPos\' takes 2 params'
		return 'Error: function \'getImgPosFromAngPos\' takes 2 params'
	angPos = parse(params[0])
	return proxy.getImgPosFromAngPos(angPos)

def getImgSizeFromAngSize(params):
	if len(params) < 1:
		print 'Error: function \'getImgSizeFromAngSize\' takes 2 params'
		return 'Error: function \'getImgSizeFromAngSize\' takes 2 params'
	angSize = parse(params[0])
	return proxy.getImgSizeFromAngSize(angSize)

def getExpectedImageParameters(params):
	return proxy.getExpectedImageParameters()

def setSimCamInputSize(params):
	if len(params) < 2:
		print 'Error: function \'setSimCamInputSize\' takes 2 params'
		return 'Error: function \'setSimCamInputSize\' takes 2 params'
	Width = parse(params[0])
	Height = parse(params[1])
	return proxy.setSimCamInputSize(Width,Height)

def putImage(params):
	if len(params) < 1:
		print 'Error: function \'putImage\' takes 2 params'
		return 'Error: function \'putImage\' takes 2 params'
	ImageBuffer = parse(params[0])
	return proxy.putImage(ImageBuffer)

def resolutionToSizes(params):
	if len(params) < 1:
		print 'Error: function \'resolutionToSizes\' takes 2 params'
		return 'Error: function \'resolutionToSizes\' takes 2 params'
	Resolution = parse(params[0])
	return proxy.resolutionToSizes(Resolution)

def sizesToResolution(params):
	if len(params) < 2:
		print 'Error: function \'sizesToResolution\' takes 2 params'
		return 'Error: function \'sizesToResolution\' takes 2 params'
	Width = parse(params[0])
	Height = parse(params[1])
	return proxy.sizesToResolution(Width,Height)

def startFrameGrabber(params):
	return proxy.startFrameGrabber()

def stopFrameGrabber(params):
	return proxy.stopFrameGrabber()

def isFrameGrabberOff(params):
	return proxy.isFrameGrabberOff()

def getHorizontalAperture(params):
	if len(params) < 1:
		print 'Error: function \'getHorizontalAperture\' takes 2 params'
		return 'Error: function \'getHorizontalAperture\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.getHorizontalAperture(CameraIndex)

def getVerticalAperture(params):
	if len(params) < 1:
		print 'Error: function \'getVerticalAperture\' takes 2 params'
		return 'Error: function \'getVerticalAperture\' takes 2 params'
	CameraIndex = parse(params[0])
	return proxy.getVerticalAperture(CameraIndex)

def recordVideo(params):
	if len(params) < 4:
		print 'Error: function \'recordVideo\' takes 2 params'
		return 'Error: function \'recordVideo\' takes 2 params'
	Name = parse(params[0])
	Path = parse(params[1])
	TotalNumber = parse(params[2])
	Period = parse(params[3])
	return proxy.recordVideo(Name,Path,TotalNumber,Period)

def stopVideo(params):
	if len(params) < 1:
		print 'Error: function \'stopVideo\' takes 2 params'
		return 'Error: function \'stopVideo\' takes 2 params'
	Name = parse(params[0])
	return proxy.stopVideo(Name)

