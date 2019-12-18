#Persistent Bugger.
#Level: 6 kyu
'''
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.
'''

def persistence(newnum):
    count = 0
    while newnum >= 10:
        res = 1
        for i in str(newnum): 
            res *= int(i)
        newnum = res
        count += 1
    return count
