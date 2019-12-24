#Counting Duplicates
#Level: 6 kyu
'''
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic 
characters and numeric digits that occur more than once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
'''

def duplicate_count(text):
    text = text.upper()
    out = 0
    checked = []
    for l in text:
        if text.count(l) > 1 and l not in checked:
            checked.append(l)
            out += 1
    return out
