#Draw stairs
#Level: 8 kyu
'''
Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.
'''
def draw_stairs(n):
    return '\n'.join(' '*x + 'I' for x in range(n))
