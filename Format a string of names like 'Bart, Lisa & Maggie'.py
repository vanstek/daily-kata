#Format a string of names like 'Bart, Lisa & Maggie'.
#Level: 6 kyu
'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
'''

def namelist(names):
    out = ''
    print(names)
    if names == []:
        return out
        
    for i, val in enumerate(names): 
        print(val['name'])
        if i == (len(names) - 1):
            out += (val['name'])
            return out
        elif i == (len(names) - 2):
            out += (val['name'] + ' & ') 
        else: 
            out += (val['name'] + ', ')
