#Factorial
#Level: 7 kyu
'''
https://en.wikipedia.org/wiki/Factorial
'''
def factorial(n):
    out = 1
    for x in range(n):
        out *= n
        n -= 1
    return out
