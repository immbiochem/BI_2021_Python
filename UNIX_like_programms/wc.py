#!/usr/bin/env python3
import sys
import os
args = sys.argv[1:]
line = True if '-l' in args else False
words = True if '-w' in args else False
cbite = True if '-c' in args else False
if line:
    args.remove('-l')
if words:
    args.remove('-w')
if cbite:
    args.remove('-c')
if not (line or words or cbite):
    line, words, cbite = True, True, True
if len(args) == 0:
    text = list(sys.stdin)
    print()
    if line:
        print(len(text), end='    ')
    if words:
        counter = 0
        for i in text:
            counter += len(i.split())
        print(counter, end='    ')
    if cbite:
        print(sys.getsizeof(text), end='    ')
    print()
else:
    if len(args) == 1:
        if os.path.isdir(args[0]):
            print('This is a directory')
            print('0  '*3, args[0])
        else:
            with open(args[0], 'r') as file:
                text = list()
                for lines in file:
                    text.append(lines)
                print(args[0] + ':', end='\n')
                if line:
                    print(len(text), end='    ')
                if words:
                    counter = 0
                    for i in text:
                        counter += len(i.split())
                    print(counter, end='    ')
                if cbite:
                    print(sys.getsizeof(text), end='    ')
                print()
    else:
        line_counter = 0
        cbite_counter = 0
        words_counter = 0
        for some in args:
            print(some + ':')
            if os.path.isdir(some):
                print('0  ' * 3, some, end='\n')
            else:
                with open(some, 'r') as file:
                    text = list()
                    for lines in file:
                        text.append(lines)
                    if line:
                        print(len(text), end='    ')
                        line_counter += len(text)
                    if words:
                        counter = 0
                        for i in text:
                            counter += len(i.split())
                        print(counter, end='    ')
                        words_counter += counter
                    if cbite:
                        print(sys.getsizeof(text), end='    ')
                        cbite_counter += sys.getsizeof(text)
                    print()
        print("Total:")
        print(line_counter, words_counter, cbite_counter, sep='     ')
