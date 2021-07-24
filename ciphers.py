#ciphers

def rot13(string):
    ROT13 = str.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
                          'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    return string.translate(ROT13)

def atbash(string):
    ATBASH = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                           'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba')
    return string.translate(ATBASH)
    
def ceasar(key, string):
    output = ''
    for char in string:       
        if char.isupper():
            output += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            output += chr((ord(char) + key - 97) % 26 + 97)
        else:
            output += char
    return output


    