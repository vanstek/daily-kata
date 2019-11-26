#What's in a name?
#Level: 6 kyu
'''
Test whether or not the string contains all of the letters which spell a given name, in order.
'''
def name_in_str(str, name):
    str = str.lower()
    name = name.lower()
    hold = ''
    l = 0
    for i, c in enumerate(str):
        if c == name[l]:
            l += 1
            hold += c         
            print(c)
        if hold == name:
            return True
    return False
