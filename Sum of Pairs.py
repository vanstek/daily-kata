#Sum of Pairs
#Level: 5 kyu
'''
Given a list of integers and a single sum value, 
return the first two values (parse from the left please) in order of appearance that add up to form the sum.
'''


#incorrect because O(n^2)
def sum_pairs(ints, s):
    out = [None] * 2
    diff = len(ints)
    for i, val in enumerate(ints):
        for x, val2 in enumerate(ints):    
            if x > i and val + val2 == s and diff > (abs(x - i)):
                diff = abs(x - i)
                out[0] = val
                out[1] = val2
    
    return None if None in out else out
    
    
    
#solution code

def sum_pairs(ints, s):
    d = set()
    for n in ints:
      if n in d: return [s - n, n]
      d.add(s - n)
