#!/usr/bin/env python
# coding: utf-8

# In[5]:


def cell_count_converter(cell_count):
    print("Your cell count in 1 ml:", cell_count * 10000)


while True:
    command = input("Enter your command (cell_count or exit):")
    if command == "exit":
        print("That's all")
        break
    elif command == "cell_count":
        cell_in_chamber = int(input("Enter the number of cells in 25 large squares of Goryaev's chamber:"))
        if cell_in_chamber >= 0:
            cell_count_converter(cell_in_chamber)
            print("Next step")
            continue
        else:
            print("The number of cells cannot be less than zero")
            continue
    else:
        print("This command is incorrect, please, enter correct command")
        continue
    # для счетной камеры Горяева 

# In[ ]:
