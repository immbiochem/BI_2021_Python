#!/usr/bin/env python3
import sys
import os
args = sys.argv[1:]
if len(args) == 0:
    sorted_list = []
    for i in sys.stdin:
        sorted_list.append(i)
    print(*sorted(sorted_list), end='', sep='')
else:
    if os.path.isfile(args[0]):
        sorted_list = []
        for i in args:
            with open(i, 'r') as file:
                for line in file:
                    sorted_list.append(line)
        print(*sorted(sorted_list), sep='', end='')
    else:
        print(*sorted(args), sep='\n')
