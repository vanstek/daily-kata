#Two to One
#Level: 7 kyu
'''
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,
each taken only once - coming from s1 or s2.
'''

import re
def longest(s1, s2):
    return ''.join(sorted(set(re.match('[a-z]+', s1).group() + re.match('[a-z]+', s2).group())))
