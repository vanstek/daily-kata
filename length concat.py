#shorter concat [reverse longer]
#Level: 7 kyu
'''
Given 2 strings, a and b, return a string of the form: shorter+reverse(longer)+shorter.
'''
def shorter_reverse_longer(a,b):
    if len(a) > len(b):
        return b + a[len(a)::-1] + b 
    if len(b) > len(a):
        return a + b[len(b)::-1] + a 
    else:
        return b + a[len(a)::-1] + b 
