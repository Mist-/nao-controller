from pyquery import PyQuery as pyq
import urllib2
s = urllib2.urlopen("file:///opt/Aldebaran%20Robotics/Choregraphe%20Suite%202.1/share/doc/naoqi/index.html").read()

codes = {}

def getFunctions(url):
    apihost = 'file:///opt/Aldebaran Robotics/Choregraphe Suite 2.1/share/doc/naoqi/'
    if url == '#':
        return
    url = apihost + url
    doc = pyq(urllib2.urlopen(url).read())
    for nodefunction in doc('.function'):
        func = pyq(pyq(nodefunction).children()[0])
        funcName = func('.descname').text()
        module = func('.descclassname').text().split('::')[0].split('Proxy')[0]
        params = []
        for param in func('em'):
            params.append(pyq(param).text())
        if not codes.has_key(module):
            codes[module] = ''
            codes[module] += 'from naoqi import ALProxy\n'
            codes[module] += 'from network.const import PORT\n'
            codes[module] += 'from lib.cmd_parser import Cmd\n'
            codes[module] += 'from lib.elementParser import parse\n\n'
            codes[module] += 'proxy = ALProxy(\'' + module + '\', \'127.0.0.1\', PORT)\n\n'
            codes[module] += 'def proceed(cmd):\n'
            codes[module] += '\tcmd = Cmd(cmd)\n'
            codes[module] += '\tcmd.removeHead()\n'
            codes[module] += '\tprint \'going to function:\', cmd.getCommand()\n'
            codes[module] += '\tfunc = globals().get(cmd.getCommand())\n'
            codes[module] += '\tif func:\n'
            codes[module] += '\t\treturn func(cmd.getValues(\'p\'))\n'
            codes[module] += '\telse:\n'
            codes[module] += '\t\tprint \'Error: Cannot find command:\' + cmd.getCommand()\n'
            codes[module] += '\t\treturn \'Error: Cannot find command:\' + cmd.getCommand()\n\n'
        codes[module] += 'def ' + funcName + '(params):\n'
        if params:
            codes[module] += '\tif len(params) < ' + str(len(params)) + ':\n'
            codes[module] += '\t\tprint \'Error: function \\\'' + funcName + '\\\' takes 2 params\'\n'
            codes[module] += '\t\treturn \'Error: function \\\'' + funcName + '\\\' takes 2 params\'\n'
        for i in range(len(params)):
            codes[module] += '\t' + params[i] + ' = parse(params[' + str(i) + '])\n'
        codes[module] += '\treturn proxy.' + funcName + '('
        if params:
            codes[module] += params[0]
            for i in range(1, len(params)):
                codes[module] += ',' + params[i]
        codes[module] += ')\n\n'

for apinode in pyq(s)('a[class=\'reference internal\']:contains(\'API\')'):
    apinode = pyq(apinode)
    apiurl = apinode.attr('href')
    getFunctions(apiurl)

for key in codes.keys():
    f = open(key[0:len(key)] + '.py', 'w')
    f.writelines(codes[key])
    f.close()
