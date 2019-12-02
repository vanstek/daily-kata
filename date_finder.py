#Scraping: Get the Year a CodeWarrior Joined
#Level: 5 kyu
'''
Task: Write a function get_member_since which accepts a username from someone at Codewars and returns an string containing the month and year separated by a space that they joined CodeWars.

If you want/don't want your username to be in the tests, ask me in the discourse area. There can't be too many though because the server may time out.
'''

from urllib.request import urlopen
import re

def get_member_since(username):
    url = 'https://www.codewars.com/users/{}'.format(username)
    html = str(urlopen(url).read())
    date = re.search('Member Since:</b>(.*?)</div>', html)
    return date.group(1) if date else None
