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

def vigenere(key, string):
    keyy = []
    for char in key:
        keyy.append(ord(char)-97)
    key_length = len(keyy)
    output = ''
    index = 0
    for char in string:
        if char.isalpha():
            output += ceasar(keyy[index], char)
            index += 1
            if index == key_length:
                index = 0
        else:
            output += char
    return output

def beaufort(key, string):
    keyy = []
    for char in key:
        keyy.append(-(ord(char)-97))
    key_length = len(keyy)
    output = ''
    index = 0
    for char in string:
        if char.isalpha():
            output += ceasar(keyy[index], char)
            index += 1
            if index == key_length:
                index = 0
        else:
            output += char
    return output

    