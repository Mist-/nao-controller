#coding=utf-8

from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd

proxy = ALProxy('ALAutonomousLife', '127.0.0.1', PORT)

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

def setState(params):
    if len(params) < 1:
        return 'Error: function \'ALAutonomousousLife::setState()\' takes 1 argument'
    proxy.setState(params[0])

def getState(params):
    return proxy.getState()
