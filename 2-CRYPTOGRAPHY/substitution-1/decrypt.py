# shady prof solution

key = {
    # picoCTF
    'b': 'p',
    'z': 'i',
    's': 'c',
    'k': 'o',
    's': 'c',
    'y': 't',
    't': 'f',

    # one-letter words
    'j': 'a',
    
    # CTF(s)
    'e': 's',

    # "capture the flag"
    'n': 'u',
    'd': 'r',
    'r': 'e',
    'a': 'h',
    'h': 'l',
    'm': 'g',

    # "security"
    'o': 'y',
    
    # "skills"
    'v': 'k',

    # "technical"
    'c': 'n',

    # "problem-solving"
    'l': 'b',
    'w': 'v',
    'x': 'm',

    # 'which'
    'g': 'w',

    # 'hosted'
    'q': 'd',

    # 'FR3(Q)U3NCY'
    'u': 'q'
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
