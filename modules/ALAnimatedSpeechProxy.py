#coding=utf-8
from naoqi import ALProxy
from network.const import PORT
from lib.cmd_parser import Cmd
from lib.elementParser import parse

proxy = ALProxy('ALAnimatedSpeech', '127.0.0.1', PORT)

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

def say(params):
    if len(params) < 1:
        print 'Error: function \'say()\' takes 1 params'
        return 'Error: function \'say()\' takes 1 params'
    text = params[0]
    if len(params) == 2:
        configuration = parse(params[1])
        proxy.say(text, configuration)
        return ''
    proxy.say(text)
    return ''

def setBodyLanguageMode(params):
    if len(params) < 1:
        print 'Error: function \'setBodyLanguageMode()\' takes 1 params'
        return 'Error: function \'setBodyLanguageMode()\' takes 1 params'
    bodyLanguageMode = parse(params[0])
    proxy.setBodyLanguageMode(bodyLanguageMode)
    return ''

def setBodyLanguageModeFromStr(params):
    if len(params) < 1:
        print 'Error: function \'setBodyLanguageModeFromStr()\' takes 1 params'
        return 'Error: function \'setBodyLanguageModeFromStr()\' takes 1 params'
    stringBodyLanguageMode = params[0]
    proxy.setBodyLanguageModeFromStr(stringBodyLanguageMode)
    return ''

def getBodyLanguageMode(params):
    return proxy.getBodyLanguageMode()

def getBodyLanguageModeToStr(params):
    return proxy.getBodyLanguageModeToStr()

def addTagsToWords(params):
    if len(params) < 1:
        print 'Error: function \'addTagsToWords()\' takes 1 params'
        return 'Error: function \'addTagsToWords()\' takes 1 params'
    tagsToWords = parse(params[0])
    proxy.addTagsToWords(tagsToWords)
    return ''

def declareAnimationsPackage(params):
    if len(params) < 1:
        print 'Error: function \'declareAnimationsPackage()\' takes 1 params'
        return 'Error: function \'declareAnimationsPackage()\' takes 1 params'
    animationsPackage = parse(params)
    proxy.declareAnimationsPackage(animationsPackage)
    return ''

def declareTagForAnimations(params):
    if len(params) < 1:
        print 'Error: function \'declareTagForAnimations()\' takes 1 params'
        return 'Error: function \'declareTagForAnimations()\' takes 1 params'
    tagsToAnimations = parse(params)
    proxy.declareTagForAnimations(animationsPackage)
    return ''

def setBodyLanguageEnabled(params):
    if len(params) < 1:
        print 'Error: function \'setBodyLanguageEnabled()\' takes 1 params'
        return 'Error: function \'setBodyLanguageEnabled()\' takes 1 params'
    enable = parse(params)
    proxy.setBodyLanguageEnabled(enable)
    return ''

def setBodyTalkEnabled(params):
    if len(params) < 1:
        print 'Error: function \'setBodyTalkEnabled()\' takes 1 params'
        return 'Error: function \'setBodyTalkEnabled()\' takes 1 params'
    enable = parse(params)
    proxy.setBodyTalkEnabled(enable)
    return ''

def isBodyTalkEnabled(params):
    return proxy.isBodyTalkEnabled()
