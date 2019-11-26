#+1 array
#Level: 6 kyu
'''
Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.
'''

def up_array(arr):
    if not arr: return None
    for i in arr:
        if i < 0 or i > 9: return None
    num = int(''.join(map(str,arr)))
    num += 1
    arr = [int(x) for x in str(num)]
    return arr
    
        
