#!/usr/bin/env python3
import os
import sys

arguments = sys.argv
flag = 0
for i in arguments[1:]:
    if os.path.isfile(i) and i in os.listdir():
        print(i, sep='', end=' ')
        arguments.remove(i)
        flag = 1
if flag == 1:
    print()
if '-a' in arguments:
    arguments.remove('-a')
    if len(arguments) == 1:
        print(*os.listdir(), sep=' ')
    elif len(arguments) == 2:
        if flag == 1:
            print(arguments[1], ":", *os.listdir(arguments[1]), sep=' ')
        else:
            print(*os.listdir(arguments[1]), sep=' ')
    else:
        for i in arguments[1:]:
            print(i, ':', *os.listdir(i), sep=' ')
else:
    if len(arguments) == 1:
        print(*[f for f in os.listdir() if not f.startswith('.')], sep=' ')
    elif len(arguments) == 2:
        if flag == 1:
            print(arguments[1], ":", *[f for f in os.listdir(arguments[1]) if not f.startswith('.')], sep=' ')
        else:
            print(*[f for f in os.listdir(arguments[1]) if not f.startswith('.')], sep=' ')
    else:
        for i in arguments[1:]:
            print(i, ':', *[f for f in os.listdir(i) if not f.startswith('.')], sep=' ')
