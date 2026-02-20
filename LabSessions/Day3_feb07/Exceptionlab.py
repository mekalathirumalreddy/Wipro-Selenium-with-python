#1.1.Handle FileNotFoundError Exception When Opening a File

try:
    import json

    with open("C://Users//thiru//PycharmProjects//PythonAdvanceProject//DataFormats//employe.json", 'r') as file:
        data = json.load(file)
    print(data)
except FileNotFoundError:
    print("There is no such file")
except Exception as e:
    print(e)


#2.write a program to handle invalid user input

try:
    a=int(input())
    print(a)
except Exception as e:
    print(e)


#3.Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()

import random
import string

ran_chr=random.choice(string.ascii_letters)
print("random_character:",ran_chr)

ran_str=""
length=random.randint(3,10)
for i in range(length):
    ran_chr = random.choice(string.ascii_letters)
    ran_str+=ran_chr
print("random_string:",ran_str)

ran_str_fixed_length=""
length=5
for i in range(length):
    ran_chr = random.choice(string.ascii_letters)
    ran_str_fixed_length+=ran_chr
print("fixed_length_string:",ran_str_fixed_length)

