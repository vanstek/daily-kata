#Two Sum
#Level: 6 kyu
'''
Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple like so: (index1, index2).
'''

def two_sum(numbers, target):
    for i, val1 in enumerate(numbers):
        for x, val2 in enumerate(numbers):
            if val1 + val2 == target and x != i:
                return (i, x)
    
    
