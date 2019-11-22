#Integer Depth
#Level: 6 kyu
'''
The depth of an integer n is defined to be how many multiples of n it is necessary to 
compute before all 10 digits have appeared at least once in some multiple.
'''

def compute_depth(n):
    digits = [1,2,3,4,5,6,7,8,9,0]
    i = 0
    while digits:
        i += 1
        multiple = i * n
        for x in str(multiple):
            if int(x) in digits:                 
                digits.remove(int(x)) 
    return i


#this solution is better. is 0(n) through set usage
def compute_depth(n):
    i = 0
    digits = set()
    while len(digits) < 10:
        i += 1
        digits.update(str(n * i))
    return i
