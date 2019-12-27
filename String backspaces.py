#Backspaces in string
#Level: 6 kyu
'''
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
Your task is to process a string with "#" symbols.
'''
def clean_string(string):
    out = ''
    for x in string:
        if x != '#': out += x
        else: out = out[:-1] 
    return out
