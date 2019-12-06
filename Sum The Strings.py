#Sum The Strings
#Level: 8 kyu
'''
Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):
'''
def sum_str(a, b):
    return str(int(a or 0)+int(b or 0))
