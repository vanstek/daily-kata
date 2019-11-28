#Loose Change
#Level: 6 kyu
'''
Welcome young Jedi! In this Kata you must create a function that takes an amount of US currency in cents, 
and returns a dictionary/hash which shows the least amount of coins used to make up that amount. 
The only coin denominations considered in this exercise are: Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢). 
Therefore the dictionary returned should contain exactly 4 key/value pairs.
'''
def loose_change(cents):
    if cents <= 0:
        return {"Nickels": 0, "Pennies": 0, "Dimes": 0, "Quarters": 0}
    q = cents // 25
    cents -= q * 25
    d = cents // 10
    cents -= d * 10
    n = cents // 5
    cents -= n * 5
    p = cents // 1
    return {"Nickels": n, "Pennies": p, "Dimes": d, "Quarters": q}
        
