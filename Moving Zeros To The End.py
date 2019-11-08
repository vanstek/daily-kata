# Moving Zeros To The End
# Level: 5kyu
'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
'''

def move_zeros(array):
    zeros = []
    new = []
    for i, val in enumerate(array):
            if  val == 0 and not (val is False):
                #adds val to zeros 'list'
                zeros.append(0)
            else:
                #adds vals to beginning of 'new' list
                new.append(val)
                
    return new + zeros
    
    
    
