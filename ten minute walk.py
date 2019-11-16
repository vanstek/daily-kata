#Take a Ten Minute Walk
#Level: 6 kyu
'''
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, 
so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their 
phones -- everytime you press the button it sends you an array of one-letter strings representing directions 
to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block in a direction and you know it takes you one minute to 
traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly 
ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.
'''
def isValidWalk(walk):
    x = 0
    y = 0
    
    for dir in walk:
        
        if dir == "n":
            y += 1
        if dir == "s":
            y -= 1
        if dir == "e":
            x += 1
        if dir == "w":
            x -= 1

    return True if ((x == 0) and (y == 0) and (len(walk) == 10)) else False
        
