#!/usr/bin/env python3
import sys
args = sys.argv[1:]
if len(args) > 0:
    for i in args:
        with open(i, 'r') as file:
            for line in file:
                print(line, end='')
else:
    for i in sys.stdin:
        print(i, end='')
