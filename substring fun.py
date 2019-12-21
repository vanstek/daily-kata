#Substring fun
#Level: 7 kyu
'''
Complete the function that takes an array of words.
You must concatenate the nth letter from each word to construct a new word 
which should be returned as a string, where n is the position of the word in the list.
'''
def nth_char(words):
    new = []
    for i,val in enumerate(words):
        new.append(val[i])
    return ''.join(new)



#one liner:
def nth_char(words):
  return ''.join(w[i] for i,w in enumerate(words))
