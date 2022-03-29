#!/usr/bin/env python
# coding: utf-8

# In[ ]:

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


class GeneratorRex:
    """
    input: path to .fasta file
    replacement - replace one or more letters in the given sequence
    delit - remove a letter or piece in the given sequence
    inser - insert one or more letters into the given sequence
    chance - apply replacement, delit or inser with some probability to the passed sequence
    """

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

    @staticmethod
    def replacement(line):
        lengh = len(line)
        line_list = list(line)
        amount_of_replace = range(int(lengh * round(random.choice([i*0.1 for i in range(5)]), 2)))
        indexes_for_replace = [random.randint(0, lengh - 1) for _ in amount_of_replace]
        for i in indexes_for_replace:
            line_list[i] = random.choice(list(set(line)))  # replace to letter from line alphabet
        return ''.join(line_list)

    @staticmethod
    def delit(line):
        lengh = len(line)
        rand_chance = random.randint(0, 3)  # rand_chance == 3 probability 1/4
        if rand_chance == 3:  # big del
            boundary_list = sorted([random.randint(0, lengh) for _ in range(2)])
            return line[:boundary_list[0]] + line[boundary_list[1]:]
        else:  # short del
            boundary_num = random.randint(0, lengh)
            return line[:boundary_num] + line[boundary_num + 1:]

    @staticmethod
    def inser(line):
        lengh = len(line)
        rand_chance = random.randint(0, 3)  # rand_chance == 3 probability 1/4
        boundary = random.randint(0, lengh)
        if rand_chance == 3:
            insert_part = "".join([random.choice(list(set(line))) for _ in range(random.randint(0, int(lengh * 0.5)))])
            return line[:boundary] + insert_part + line[boundary:]
        else:
            return line[:boundary] + random.choice(list(set(line))) + line[boundary:]

    def chance(self, line):
        coin = random.randint(0, 3)
        if coin >= 1:
            return self.replacement(line)
        else:
            coin = random.randint(0, 1)
            if coin:
                return self.inser(line)
            else:
                return self.delit(line)

    def __next__(self):
        self._coursor += 1
        try:
            return self.chance(self.box[self._coursor])
        except IndexError:
            self._coursor = 0
            return self.chance(self.box[self._coursor])

    def __iter__(self):
        return self
