#coding=utf-8
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

def moveToward(params):
    print 'moving'
    proxy.moveToward(float(params[0]), float(params[1]), float(params[2]))

def stopMove(params):
    proxy.stopMove()
    pass

def robotIsWakeUp(params):
    return str(autonomousLifeProxy.robotIsWakeUp())

def wakeUp(params):
    proxy.wakeUp()
    pass

def rest(params):
    proxy.rest()
    pass

def stiffnessInterpolation(params):
    if len(params) < 3:
        print 'Error: function \'stiffnessInterpolation()\' takes 3 params'
        return 'Error: function \'stiffnessInterpolation()\' takes 3 params'
    names = parse(params[0])
    stiffnessLists = parse(params[1])
    timeLists = parse(params[2])
    proxy.stiffnessInterpolation(names, stiffnessLists, timeLists)
    pass

def setStiffness(params):
    if len(params) < 2:
        print 'Error: function \'setStiffness()\' takes 2 params'
        return 'Error: function \'setStiffness()\' takes 2 params'
    names = parse(params[0])
    stiffnessLists = parse(params[1])
    proxy.setStiffnesses(names, stiffnessLists)

def getStiffnesses(params):
    if len(params) < 1:
        print 'Error: function \'getStiffness()\' takes 1 param'
        return 'Error: function \'getStiffness()\' takes 1 param'
    jointName = parse(params[0])
    return proxy.getStiffnesses(jointName)
