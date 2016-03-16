#coding=utf-8

import re

def parse(str):
    if not str: return None
    str = str.strip()
    if fullyMatch('[0-9]+', str):
        return int(str)
    elif fullyMatch('[0-9]*[.][0-9]+|[0-9]+[.][0-9]*', str):
        return float(str)
    elif fullyMatch('[\[].*[\]]', str):
        return getArray(str)
    elif fullyMatch('[\'].*[\']|[\"].*[\"]', str):
        return str[1:len(str) - 1]
    elif str == 'False':
        return False
    elif str == 'True':
        return True
    elif str == '':
        return None
    print '未识别的元素类型：', str

# 接受形如'[1,2,3,'123',True]'的字符串（中间不允许出现空格）。
def getArray(str):
    str = str.strip()
    str = str[1:len(str) - 1]
    result = []
    elems = re.split('[,][ ]*|([\[].*[\]])', str)
    for element in elems:
        ele = parse(element)
        if ele != '' and ele != () and ele != [] and not ele:
            continue
        result.append(ele)
    return result

def fullyMatch(reg, str):
    if re.match(reg, str) and re.match(reg, str).group() == str:
        return True
    return False

print parse('[1, 2, [2, 3, [4, 5, [6, 7]]]]')
