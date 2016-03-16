from lib.cmd_parser import Cmd

def proceed(cmd):
    cmd = Cmd(cmd)
    cmd.removeHead()
    print 'going to function:', cmd.getCommand()
    func = globals().get(cmd.getCommand())
    print '111111,', func
    if func:
        return func(cmd.getValues('p'))
    else:
        print 'Cannot find command:' + cmd.getCommand()
        return 'Cannot find command:' + cmd.getCommand()
