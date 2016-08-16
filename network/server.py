#coding=utf-8
import socket
from lib.cmd_proceeder import give
from lib.cmd_parser import Cmd

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def initServer():
    sock.bind(('0.0.0.0', 9998))
    sock.listen(1)

# 通过socket获取一条语句
def getCommandList():
    conn, addr = sock.accept()
    cmdList = []
    while True:
        string = conn.recv(1024)
        cmds = string.split(';')
        cmds.append('#')
        for cmd in cmds:
            if cmd == '#':
                return (cmdList, conn)
            if cmd:
                cmdList.append(cmd)
                print 'receiving command:', cmd
    pass
