# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import os, sys
import socket, struct
from collections import namedtuple
import re
 
#''' 获取Linux系统的版本信息 ''' 
def getOsVersion():
    with open('/etc/issue') as fd:
        for line in fd:
            osver = line.strip()
            break
    return {'osver': osver}
 
#''' 获取CPU的型号和CPU的核心数 '''
def getCpu():
    num = 0
    with open('/proc/cpuinfo') as fd:
        for line in fd:
            if line.startswith('processor'):
                num += 1
            if line.startswith('model name'):
                cpu_model = line.split(':')[1].strip().split()
                cpu_model = cpu_model[0] + ' ' + cpu_model[2] + ' ' + cpu_model[-1]
    return {'cpu_num': num, 'cpu_model': cpu_model}
 
#''' 获取Linux系统的总物理内存 '''
def getMemory():
    with open('/proc/meminfo') as fd:
        for line in fd:
            if line.startswith('MemTotal'):
                mem = int(line.split()[1].strip())
                break
    mem = '%.f' % (mem / 1024000.0) + ' GB'
    return {'Memory': mem}
 
def main():
    dic = {}
    osver = getOsVersion()
    cpu = getCpu()
    mem = getMemory()
    dic.update(osver)
    dic.update(cpu)
    dic.update(mem)
    print (dic)
    return 0


