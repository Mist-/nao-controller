#coding=utf-8
from modules.ALMotion import proceed as motionProc
from modules.ALAutonomousLife import proceed as autoLifeProc
from lib.cmd_parser import Cmd

procs = {}
procs['ALMotion'] = motionProc
procs['ALAutonomousLife'] = autoLifeProc


# 将指令分配给相应的子程序处理
def give(cmd):
    module = Cmd(cmd).getCommand()
    print 'going to module:', module
    proc = procs[module]
    return proc(cmd)
    pass
