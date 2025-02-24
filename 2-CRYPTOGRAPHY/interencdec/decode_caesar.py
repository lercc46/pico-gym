# to crack the caesar cipher in the double base64'd flag

flag_2 = ""

with open('flag_2', 'r') as file:
    for line in file:
        flag_2 += line.strip()

rot = 0
while rot <= 26:
    for char in flag_2.lower():
        if ord(char) in range(97,123): 
            print(chr((ord(char) + rot - 97) % 26 + 97), end="")
        else:
            print(char, end="")
    print()
    rot += 1

