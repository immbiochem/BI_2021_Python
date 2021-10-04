#!/usr/bin/env python
# coding: utf-8

# In[9]:


varios = True  # для бесконечного цикла
while varios == True:
    interact1 = input("Enter your command:")  # для общения с пользователем
    if interact1 == "exit":
        varios = False
        print("OK, that's all")  # тут завершаем цикл при команде exit
        break
    elif interact1 != "transcribe" and interact1 != "reverse" and interact1 != "complement" and interact1 != "reverse complement":
        print("I don't know this command")
    else:
        interact2 = input("Enter your seq:")  # исходная строка
        lis = []  # рабочая лошадь для анализа последовательности, перепечатываем строку в лист
        for line in interact2:
            lis += [line]

        # проведем проверку, является ли последовательность нуклеиновой кислотой
        condition = 0
        for i in lis:
            # для малых букв
            if i == 'a':
                continue
            elif i == 't':
                continue
            elif i == 'g':
                continue
            elif i == 'c':
                continue
            elif i == 'u':
                continue

            # для больших букв
            elif i == 'T':
                continue
            elif i == 'G':
                continue
            elif i == 'C':
                continue
            elif i == 'U':
                continue
            elif i == 'A':
                continue

            else:
                condition = 1
                break
        if condition == 1:
            print("This isn't nucleic acid")
            continue
        elif 'u' in interact2.lower() and 't' in interact2.lower():  # проверка u и t в одной строке
            print("This isn't a normal RNA or DNA!")  # в норме их вместе быть не должно
            continue

        # определим тип молекулы

        if 'u' in interact2.lower():
            molecul = "RNA"
        else:
            molecul = "DNA"

        # команда для обратной последовательности

        if interact1 == "reverse":
            print("Your reverse seq: ")
            for i in lis[::-1]:
                print(i, end="")
            print()

        # команда для транскрипции

        elif interact1 == "transcribe":
            if molecul == "DNA":  # ДНК транскрибируется
                lis2 = []
                for i in lis:
                    # для малых букв
                    if i == 'a':
                        lis2 += 'u'
                    if i == 't':
                        lis2 += 'a'
                    if i == 'c':
                        lis2 += 'g'
                    if i == 'g':
                        lis2 += 'c'
                    # для больших букв
                    if i == 'A':
                        lis2 += 'U'
                    if i == 'T':
                        lis2 += 'A'
                    if i == 'C':
                        lis2 += 'G'
                    if i == 'G':
                        lis2 += 'C'

                print("Your transcript: ")  # Выводим результат
                for i in lis2:
                    print(i, end="")
                print()
            else:
                print("This isn't transcribed!")  # РНК транслируется, не транскрибируется

        # команда для complement seq

        elif interact1 == "complement":
            if molecul == "DNA":  # если ДНК, то циклом выводит комплементарную последовательность ДНК
                lis3 = []
                for i in lis:
                    # для малых букв
                    if i == 'a':
                        lis3 += 't'
                    if i == 't':
                        lis3 += 'a'
                    if i == 'c':
                        lis3 += 'g'
                    if i == 'g':
                        lis3 += 'c'
                    # для больших букв
                    if i == 'A':
                        lis3 += 'T'
                    if i == 'T':
                        lis3 += 'A'
                    if i == 'C':
                        lis3 += 'G'
                    if i == 'G':
                        lis3 += 'C'
                print("Your complement DNA-seq: ")
                for i in lis3:
                    print(i, end="")
                print()
            else:  # если РНК, то циклом выводит комплементарную последовательность РНК
                lis3 = []
                for i in lis:
                    # для малых букв
                    if i == 'a':
                        lis3 += 'u'
                    if i == 'u':
                        lis3 += 'a'
                    if i == 'c':
                        lis3 += 'g'
                    if i == 'g':
                        lis3 += 'c'
                    # для больших букв
                    if i == 'A':
                        lis3 += 'U'
                    if i == 'U':
                        lis3 += 'A'
                    if i == 'C':
                        lis3 += 'G'
                    if i == 'G':
                        lis3 += 'C'
                print("Your complement RNA-seq: ")
                for i in lis3:
                    print(i, end="")
                print()

        # команда для reverse complement seq

        elif interact1 == "reverse complement":
            if molecul == "DNA":  # если ДНК, то циклом выводит обратную комплементарную последовательность ДНК
                lis3 = []
                for i in lis:
                    # для малых букв
                    if i == 'a':
                        lis3 += 't'
                    if i == 't':
                        lis3 += 'a'
                    if i == 'c':
                        lis3 += 'g'
                    if i == 'g':
                        lis3 += 'c'
                    # для больших букв
                    if i == 'A':
                        lis3 += 'T'
                    if i == 'T':
                        lis3 += 'A'
                    if i == 'C':
                        lis3 += 'G'
                    if i == 'G':
                        lis3 += 'C'
                print("Your reverse complement DNA-seq: ")
                for i in lis3[::-1]:
                    print(i, end="")
                print()
            else:  # если РНК, то циклом выводит обратную комплементарную последовательность РНК
                lis3 = []
                for i in lis:
                    # для малых букв
                    if i == 'a':
                        lis3 += 'u'
                    if i == 'u':
                        lis3 += 'a'
                    if i == 'c':
                        lis3 += 'g'
                    if i == 'g':
                        lis3 += 'c'
                    # для больших букв
                    if i == 'A':
                        lis3 += 'U'
                    if i == 'U':
                        lis3 += 'A'
                    if i == 'C':
                        lis3 += 'G'
                    if i == 'G':
                        lis3 += 'C'
                print("Your reverse complement RNA-seq: ")
                for i in lis3[::-1]:
                    print(i, end="")
                print()

# In[ ]:
