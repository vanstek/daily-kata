#Meeting
#Level: 6 kyu
'''
s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
Could you make a program that

makes this string uppercase
gives it sorted in alphabetical order by last name.
'''

def meeting(s):
    s = s.upper()
    s = s.split(";")
    out = ''
    names = []
    
    for n in s:
        n = n.split(':')
        n.reverse()
        names.append(n)    
        
    names = sorted(names)
    for name in names: out += '(' + name[0] +', ' + name[1] +  ')'
    
    return out
    
