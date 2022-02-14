#!/usr/bin/env python3
import sys
args = sys.argv[1:]
n = True if '-n' in args else False
numeric = 10
if n:
    for some in args:
        if some.isdigit():
            numeric = int(some)
            args.remove(some)
            break
    args.remove('-n')
if len(args) == 0:
    text = list()
    for line in sys.stdin:
        text.append(line)
    print()
    if len(text) >= numeric:
        print(*text[len(text)-numeric:], sep='', end='')
    else:
        print(*text, sep='', end='')
else:
    label = True if len(args) > 1 else False
    for some in args:
        print()
        text = list()
        with open(some, 'r') as file:
            for line in file:
                text.append(line)
        if label:
            print('===>' + some + '<===')
        # print()
        if len(text) >= numeric:
            print(*text[len(text) - numeric:], sep='', end='')
        else:
            print(*text, sep='', end='')
