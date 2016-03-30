#coding=utf-8

import re

class Cmd:
    def __init__(self, cmdstr):
        self.cmdstr = cmdstr.strip()
        pass

    # 去掉第一个字符串
    def removeHead(self):
        self.cmdstr = self.cmdstr[self.cmdstr.index(' ') + 1:]
        pass

    # 返回指令的主体
    def getCommand(self):
        cmds = re.split('[ ]+', self.cmdstr)
        if len(cmds) > 0:
            return cmds[0]
        return ''

    # 返回指令的参数键，形如 -i, --install
    def getKeys(self):
        cmds = re.split('[ ]+', self.cmdstr)
        keys = []
        for cmd in cmds:
            mo = re.match('[-][-][a-zA-Z]+', cmd)
            if mo and mo.group() == cmd:
                keys.append(mo.group().replace('-', ''))
                pass
            mo1 = re.match('[-][a-zA-Z]', cmd)
            if mo1 and mo1.group() == cmd:
                keys.append(mo1.group().replace('-', ''))
                pass
            pass
        return keys

    # 返回某个参数键对应的参数列表
    def getValues(self, key):
        cmds = re.split('[ ]+', self.cmdstr)
        values = []
        if len(key) == 1:
            key = '-' + key
        else:
            key = '--' + key
        for i in range(0, len(cmds)):
            if cmds[i] == key:
                for j in range(i, len(cmds)):
                    mo = re.match('[-][-][a-zA-Z]+', cmds[j])
                    mo1 = re.match('[-][a-zA-Z]', cmds[j])
                    if not (mo and mo.group() == cmds[j] or mo1 and mo1.group() == cmds[j]):
                        values.append(cmds[j])
            pass
        return values
