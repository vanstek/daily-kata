#Sort the odd
#Level: 6 kyu
'''You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.
Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.
'''

def sort_array(source_array):
    if source_array == []:
        return source_array   
    odds = []   
    
    for i,n in enumerate(source_array):       
        if n%2 != 0:
            odds.append(n)
            
    odds.sort()   
     s = 0 
    for i,n in enumerate(source_array):
        if n%2 != 0:
            source_array[i] = odds[s]
            s +=1           
    return source_array
