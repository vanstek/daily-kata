#Multiples of 3 or 5
#Level: 6 kyu
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
'''
def solution(number):
    return sum(i for i in range(number) if i % 5 == 0 or i % 3 == 0)
