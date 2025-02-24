#!/usr/bin/python3

# to crack caesar, ROT13, etc.

from sys import argv

flag = ""
filename = "encoded_flag"

with open(filename, 'r') as file:
    for line in file:
        flag += line.strip()

if argv[1] == "c":
    rot = 0
    while rot <= 26:
        for char in flag.lower():
            if ord(char) in range(97,123): 
                print(chr((ord(char) + rot - 97) % 26 + 97), end="")
            else:
                print(char, end="")
        print()
        rot += 1

elif argv[1] == "r":
    rot = int(input("rotate by how much? [1-25]: "))
    for char in flag.lower():
        if ord(char) in range(97,123): 
            print(chr((ord(char) + rot - 97) % 26 + 97), end="")
        else:
            print(char, end="")
    print()

else:
    print("invalid arg, \'c\' for caesar brute force and \'r\' to choose how far to rotate")
