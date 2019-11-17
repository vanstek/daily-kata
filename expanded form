#Write Number in Expanded Form
#Level: 6 kyu
'''You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
'''

def expanded_form(num):
    i = 1
    num = str(num)
    out = ''

    for n in num:
        if i == 1:
            out +=(n + '0'*(len(num)-i))
        elif n != '0':
            out +=(' + ' + n + '0'*(len(num)-i))
        i += 1
        
    return out
