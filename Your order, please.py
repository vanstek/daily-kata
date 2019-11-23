#Your order, please
#
'''Your task is to sort a given string. Each word in the string will contain a single number. 
This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
'''

import re
def order(sentence):
    if sentence == '': return sentence
    split = sentence.split(' ')
    list = [None] * len(split)
    for i in split:        
        result = int(re.search('\d',i).group(0))
        del list[result-1]
        list.insert(result-1, i + " ")
    out = '' 
    for val in list:  
        out += val   
    return(out.rstrip())
