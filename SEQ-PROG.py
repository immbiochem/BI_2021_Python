#!/usr/bin/env python
# coding: utf-8

# In[9]:


peremen = True #для бесконечного цикла
while peremen == True:
    interact1 = input("Enter your comand:") #для общения с пользователем
    if interact1 == "exit":
        peremen = False
        print("OK, that's all") #тут завершаем цикл
        break
    else:
        interact2 = input("Enter your seq:") #исходная строка 
        lis = [] #рабочая лошадь для анализа последовательности, перепечатываем строку в лист
        for line in interact2:
            lis+=[line]
        #print(lis) - напечатать код если нужно
        if "u" in interact2.lower() and "t" in interact2.lower(): #проверяем исходную строку на наличие реципроктных символов
            print("You have a Francenshtain-molecule, please, write normal seq") # t и u не могут быть вместе
        else:
            if "t" in interact2.lower() and interact1 == "transcribe": #транскрипция может быть только для ДНК, поэтому проверяем наличие t
                lis1 = [] #тут будет транскрипт как лист1
                for i in lis: #цикл используем для переработки транскрипта
                    if i == 'a':
                        lis1+='t'
                    if i == 't':
                        lis1+='a'
                    if i == 'g':
                        lis1+='c'
                    if i == 'c':
                        lis1+='g'
                print(lis1) #печатаем транскрипт
            else:
                if interact1 == "reverse": #действия для команды reverse
                    print("This is reversive seq: ")
                    for i in lis[::-1]:
                        print(i, end="") #в цикле выводим перевернутую последовательность
                else:
                    if interact1 == "complement" and "t" in interact2.lower(): #проверка для команды complement на ДНК-овость
                        lis2 = [] #тут будет комплементарная последовательность для ДНК
                        for i in lis: #цикл 
                            if i == 'a':
                                lis2+='t'
                            if i == 't':
                                lis2+='a'
                            if i == 'g':
                                lis2+='c'
                            if i == 'c':
                                lis2+='g'
                        print("This is the complement seq: ")
                        for i in lis2:
                            print(i, end="") #в цикле выводим комплементарную последовательность ДНК
                    else:
                        if interact1 == "complement" and "u" in interact2.lower(): #проверка для команды complement на РНК-овость
                            lis3 = [] #тут будет комплементарная последовательность для РНК
                            for i in lis: #цикл 
                                if i == 'a':
                                    lis3+='u'
                                if i == 'u':
                                    lis3+='a'
                                if i == 'g':
                                    lis3+='c'
                                if i == 'c':
                                    lis3+='g'
                            print("This is the complement seq: ")
                            for i in lis3:
                                print(i, end="") #в цикле выводим комплементарную последовательность РНК
                            
                        
                
                        
                
                    
                        
        
        
        


# In[ ]:




