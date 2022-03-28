#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np
import random


def gen_fasta(path: str):
    body = []
    stroka = str()
    with open(path, 'r') as file:
        body.append(file.readline().strip())
        for line in file:
            if line.startswith('>'):
                body.append(stroka)
                body.append(line.strip())
                stroka = str()
            else:
                stroka += line.strip()
    body.append(stroka)
    for value in body:
        yield value


class Generator_Rex:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.box = []
        self.stroka = str()
        with open(self.path_to_file, 'r') as file:
            file.readline()
            for line in file:
                if line.startswith('>'):
                    self.box.append(self.stroka)
                    self.stroka = str()
                else:
                    self.stroka += line.strip()
        self.box.append(self.stroka)
        self._coursor = -1

    def change(self, line):
        line_transform = np.array(list(line))
        num = int(len(line) * (random.randint(1, 3) * 0.1))
        line_transform[tuple(np.random.randint(len(line), size=num)),] = np.random.choice(line_transform, num)
        return ''.join(line_transform)

    def __next__(self):
        self._coursor += 1
        try:
            return self.change(self.box[self._coursor])
        except IndexError:
            self._coursor = 0
            return self.change(self.box[self._coursor])

    def __iter__(self):
        return self
