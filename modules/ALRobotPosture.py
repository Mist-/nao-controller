#coding=utf-8
from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALRobotPosture', '127.0.0.1', PORT)

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

def getPostureList(params):
    return proxy.getPostureList()

def getPosture(params):
    return proxy.getPostureList()

def goToPosture(params):
    if len(params) < 2:
        print 'Error: function \'goToPosture()\' takes 2 params'
        return 'Error: function \'goToPosture()\' takes 2 params'
    postureName = parse(params[0])
    speed = parse(params[1])
    return proxy.goToPosture(postureName, speed)

def applyPosture(params):
    if len(params) < 2:
        print 'Error: function \'applyPosture()\' takes 2 params'
        return 'Error: function \'applyPosture()\' takes 2 params'
    postureName = parse(params[0])
    speed = parse(params[1])
    return proxy.applyPosture(postureName, speed)

def stopMove(params):
    proxy.stopMove()
    return ''

def getPostureFamily(params):
    return proxy.getPostureFamily()

def getPostureFamilyList(params):
    return proxy.getPostureFamilyList()

def setMaxTryNumber(params):
    if len(params) < 2:
        print 'Error: function \'applyPosture()\' takes 2 params'
        return 'Error: function \'applyPosture()\' takes 2 params'
    