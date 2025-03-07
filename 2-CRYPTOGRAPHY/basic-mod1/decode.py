#!/usr/bin/python3

with open("message.txt", "r") as file:
    msg = file.readline().strip()

# put numbers in list
msg = msg.split(" ")

for num in msg:
    modded = int(num) % 37
    if modded in range(0,26):
        print(chr(modded+65), end="") # print letter
    elif modded in range(26, 36):
        print(modded-26, end="") # print number
    else:
        print("_", end="")
print()
