#Count the divisors of a number
#Level: 7 kyu
'''
Count the number of divisors of a positive integer n.
'''

def divisors(n):
    out = 0
    for x in range(1,n+1):
        if n%x == 0:
            out += 1
    return out
