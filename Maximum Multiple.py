#Maximum Multiple
#Level: 7 kyu
'''
Given a Divisor and a Bound , Find the largest integer N , Such That ,

Conditions :
N is divisible by divisor

N is less than or equal to bound

N is greater than 0.
'''
def max_multiple(d, b):
    n = 0
    out = 0
    while n % d != 0:
        n += 1
    while n <= b:
        if n % d == 0:
            out = n
        n += d
    return out
    
    
#much smart way of doing it:
