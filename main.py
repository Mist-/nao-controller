from network.server import initServer, getCommandList, give
import thread

initServer()

def giveCommand(cmd, conn):
    feedback = ''

    for cmd in cmdList:
        feedback += str(give(cmd)) + '\n'

    conn.send(feedback)

while True:
    cmdList, conn = getCommandList()
    thread.start_new_thread(giveCommand, (cmdList, conn))

conn.close()
