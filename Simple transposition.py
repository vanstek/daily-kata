#Simple transposition
#Level: 6 kyu
'''
Simple transposition is a basic and simple cryptography technique. We make 2 rows and put first a letter in the Row 1, 
the second in the Row 2, third in Row 1 and so on until the end. Then we put the text from Row 2 next to the Row 1 text and thats it.
Complete the function that recieves a string and encrypt it with this simple transposition.
'''

def simple_transposition(text):
    first = []
    second = []
    for i,val in enumerate(text):
        if i%2 == 0:
            first.append(val)
        else:
            second.append(val)
    first.extend(second)
    out = ''.join(first)
    return out
