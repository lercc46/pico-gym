#!/usr/bin/python3

with open("message.txt", "r") as file:
    msg = file.readline().strip()

# put numbers in list
msg = msg.split(" ")
print([int(num) % 41 for num in msg])
print([pow(int(num) % 41, -1, 41) for num in msg])

for num in msg:
    modded = int(num) % 41
    inverse = pow(modded, -1, 41) # mod inverse, built in!
    if inverse in range(1,27):
        print(chr(inverse+64), end="") # print letter
    elif inverse in range(27, 37):
        print(inverse-27, end="") # print number
    else:
        print("_", end="")
print()
