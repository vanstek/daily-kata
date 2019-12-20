#Tail Swap
#Level: 7 kyu
'''
You'll be given a list of two strings, and each will contain exactly one colon (":") in the middle (but not at beginning or end). 
The length of the strings, before and after the colon, are random.
Your job is to return a list of two strings (in the same order as the original list), but with the characters after each colon swapped.
'''
def tail_swap(strings):
    out = []
    
    out.append(strings[0].split(':')[0] + ':' + strings[1].split(':')[1])
    out.append(strings[1].split(':')[0] + ':' + strings[0].split(':')[1])
            
    return out
