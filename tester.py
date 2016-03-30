import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
s.send('ALMotion moveToward -p 1.0 1.0 1;')
s.send('#')
s.close()
