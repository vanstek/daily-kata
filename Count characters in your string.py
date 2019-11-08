# Count characters in your string
# Level: 6kyu
'''
The main idea is to count all the occuring characters(UTF-8) in string. If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

What if the string is empty ? Then the result should be empty object literal { }
'''
def count(string):
    count = {}
    for i in string:
        count[i] = string.count(i)
    return count

# Test Case
print(friend(["Ryan", "Kieran", "Mark", ]))
© 2019 GitHub, Inc.
