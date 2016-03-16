from network.server import initServer, getCommandList, give

initServer()
cmdList, conn = getCommandList()

feedback = ''

for cmd in cmdList:
    feedback += str(give(cmd)) + '\n'

conn.send(feedback)

conn.close()
