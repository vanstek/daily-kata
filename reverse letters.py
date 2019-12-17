#Numbers to Letters
#Level: 7 kyu
'''
Given an array of numbers, you must return a string. 
The numbers correspond to the letters of the alphabet in reverse order: a=26, z=1 etc. Y
ou should also account for '!', '?' and ' ' that are represented by '27', '28' and '29' respectively.
'''

import string
def switcher(arr):
    str = []
    alpha = string.ascii_lowercase[::-1] + ('!? ')       
    for i in arr:
        str.append(alpha[int(i)-1])
    return ''.join(str)
