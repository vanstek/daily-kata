#Sum of Numbers
#Level: 7 kyu
'''
Given two integers a and b, which can be positive or negative,
find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.
Note: a and b are not ordered!
'''

#my answer
def get_sum(a,b):
    return sum(x for x in range(min(a,b),max(a,b)+1))
    
#better answer
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
