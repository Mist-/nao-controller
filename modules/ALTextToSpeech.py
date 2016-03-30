#coding=utf-8
from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALTextToSpeech', '127.0.0.1', PORT)

def proceed(cmd):
    cmd = Cmd(cmd)
    cmd.removeHead()
    print 'going to function:', cmd.getCommand()
    func = globals().get(cmd.getCommand())
    if func:
        return func(cmd.getValues('p'))
    else:
        print 'Error: Cannot find command:' + cmd.getCommand()
        return 'Error: Cannot find command:' + cmd.getCommand()

def getAvailableLanguages(params):
    return proxy.getAvailableLanguages()

def getAvailableVoices(params):
    return proxy.getAvailableVoices()

def getLanguage(params):
    return proxy.getLanguage()

def getParameter(params):
    if len(params) < 1:
        print 'Error: function \'getParameter()\' takes 2 params'
        return 'Error: function \'getParameter()\' takes 2 params'
    parameter = parse(params[0])
    return proxy.getParameter(parameter)

def getSupportedLanguages(params):
    return proxy.getSupportedLanguages()

def getVoice(params):
    return proxy.getVoice()

def getVolume(params):
    return proxy.getVolume()

def loadVoicePreference(params):
    if len(params) < 1:
        print 'Error: function \'loadVoicePreference()\' takes 1 params'
        return 'Error: function \'loadVoicePreference()\' takes 1 params'
    preferencesFileSuffix = parse(params[0])
    proxy.loadVoicePreference(preferencesFileSuffix)
    return ''

def locale(params):
    return proxy.locale()

def say(params):
    if len(params) < 1:
        print 'Error: function \'say()\' takes 1 or 2 params'
        return 'Error: function \'say()\' takes 1 or 2 params'
    stringToSay = params[0]
    if len(params) > 1:
        language = params[1]
        proxy.say(stringToSay, language)
        return ''
    proxy.say(stringToSay)
    return ''

def sayToFile(params):
    if len(params) < 2:
        print 'Error: function \'sayToFile()\' takes 2 params'
        return 'Error: function \'sayToFile()\' takes 2 params'
    stringToSay = params[0]
    fileName = params[1]
    proxy.sayToFile(stringToSay, fileName)
    return ''

def sayToFileAndPlay(params):
    if len(params) < 1:
        print 'Error: function \'sayToFileAndPlay()\' takes 1 params'
        return 'Error: function \'sayToFileAndPlay()\' takes 1 params'
    stringToSay = params[0]
    proxy.sayToFileAndPlay(stringToSay)
    return ''

def setLanguage(params):
    if len(params) < 1:
        print 'Error: function \'setLanguage()\' takes 1 params'
        return 'Error: function \'setLanguage()\' takes 1 params'
    language = params[0]
    proxy.setLanguage(stringToSay)
    return ''

def setLanguageDefaultVoice(params):
    if len(params) < 2:
        print 'Error: function \'setLanguageDefaultVoice()\' takes 2 params'
        return 'Error: function \'setLanguageDefaultVoice()\' takes 2 params'
    language = params[0]
    voice = params[1]
    proxy.setLanguageDefaultVoice(language, voice)
    return ''

def setParameter(params):
    if len(params) < 2:
        print 'Error: function \'setParameter()\' takes 2 params'
        return 'Error: function \'setParameter()\' takes 2 params'
    parameter = params[0]
    value = params[1]
    proxy.setLanguageDefaultVoice(parameter, value)
    return ''

def setVoice(params):
    if len(params) < 1:
        print 'Error: function \'setVoice()\' takes 1 params'
        return 'Error: function \'setVoice()\' takes 1 params'
    voiceID = params[0]
    proxy.setVoice(voiceID)
    return ''

def setVolume(params):
    if len(params) < 1:
        print 'Error: function \'setVolume()\' takes 1 params'
        return 'Error: function \'setVolume()\' takes 1 params'
    volume = params[0]
    proxy.setVolume(volume)
    return ''

def stopAll(params):
    proxy.stopAll()
    return ''

def getLanguageEncoding(params):
    if len(params) < 1:
        print 'Error: function \'getLanguageEncoding()\' takes 1 params'
        return 'Error: function \'getLanguageEncoding()\' takes 1 params'
    languageName = params[0]
    proxy.getLanguageEncoding(languageName)
    return ''
