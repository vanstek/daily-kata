#Duplicate Encoder
#Level: 6 kyu
'''
The goal of this exercise is to convert a string to a new string where each character 
in the new string is "(" if that character appears only once in the original string, or ")" 
if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.
'''
def duplicate_encode(word):
    word = word.upper()
    out = ''
    for l in word:
        if word.count(l) == 1:
            out += '('
        else: 
            out += ')'
    return out
