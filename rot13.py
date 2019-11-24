#Rot13
#Level: 6 kyu
'''
Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters 
included in the string, they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
''' 

import string
def rot13(message):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    s = list(message)
    for i, letter in enumerate(s):
        if letter in lower:
            s[i] = lower[lower.index(letter)-13]        
        elif letter in upper:
            s[i] = upper[upper.index(letter)-13]
    return(''.join(s))
