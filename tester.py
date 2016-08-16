#coding=utf-8
import socket

url = '127.0.0.1'
port = 9998

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((url, port))
    string = raw_input('>')
    if string == 'exit':
        break
    print string
    s.send(str(string) + ';')
    s.send('#')
    s.close
