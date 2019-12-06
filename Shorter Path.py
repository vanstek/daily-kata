#Shorter Path
#Level: 6 kyu
'''
You are given a list of directions in the form of a list:
goal = ["N", "S", "E", "W"]
Pretend that each direction counts for 1 step in that particular direction.
Your task is to create a function called directions, that will return a reduced list that will get you to the same point.The order of directions must be returned as N then S then E then W.
If you get back to beginning, return an empty array.
'''

#couldve put it all in one for loop
def directions(goal):
    N = goal.count("N") - goal.count("S")
    E = goal.count("E") - goal.count("W")
    dir = []
    
    if N > 0: 
        for x in range(abs(N)):   
              dir.append('N')
    elif N < 0:
        for x in range(abs(N)):   
            dir.append('S')        
    if E > 0:
        for x in range(abs(E)):    
            dir.append('E')
    elif E < 0:
        for x in range(abs(E)):    
            dir.append('W') 
    return dir 
    
    
