#coding=utf-8
from modules.ALMotion import proceed as motionProc
from modules.ALAutonomousLife import proceed as autoLifeProc
from modules.ALDialog import proceed as dialogProc
from modules.ALTextToSpeech import proceed as ttsProc
import modules

from lib.cmd_parser import Cmd

procs = {}
procs['ALMotion'] = motionProc
procs['ALAutonomousLife'] = autoLifeProc
procs['ALTextToSpeech'] = ttsProc
procs['ALDialog'] = dialogProc

print modules
# 将指令分配给相应的子程序处理
def give(cmd):
    module = Cmd(cmd).getCommand()
    print 'going to module:', module
    proc = procs.get(module, None)
    if not proc:
        print 'no module named \'' + module + '\''
        return 'no module named \'' + module + '\''
    return proc(cmd)
