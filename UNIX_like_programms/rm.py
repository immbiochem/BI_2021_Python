#!/usr/bin/env python3
import os
import sys
import shutil
args = sys.argv[1:]
if '-r' in args:
    args.remove('-r')
    for i in args:
        shutil.rmtree(i)
else:
    for i in args:
        if os.path.isfile(i):
            os.remove(i)
        else:
            print('This is not a file')
