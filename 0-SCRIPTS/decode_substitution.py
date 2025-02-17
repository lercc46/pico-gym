#!/usr/bin/python3

# shady prof solution

key = {
    # "picoCTF"
    'v': 'p',
    'q': 'i',
    'k': 'c',
    'm': 'o',
    'f': 't',
    'l': 'f',
    
    # "4N41Y515"
    'g': 'n',
    't': 'y',

    # freq analysis --> E, T, A, O, I, N, S, ...
    'j': 'e',
    'f': 't',
    'q': 'i', # not a, i
    'm': 'o',
    'g': 'n', # not a, n
    's': 's', # not a, s
    'x': 'a', # trying a here

    # "there exists"
    'n': 'h',
    'd': 'r',
    'z': 'x',
        }

with open("message.txt", "r") as msg:
    ct = msg.read()

pt = ""
for a_char in ct:
    if a_char.lower() in key:
        pt += key[a_char.lower()].upper()
    else:
        pt += a_char.lower()

print(pt)
