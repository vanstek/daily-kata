#Disarium Number (Special Numbers Series #3)
#Level: 7 kyu
'''
Definition
Disarium number is the number that The sum of its digits powered with their respective positions is equal to the number itself.

Task
Given a number, Find if it is Disarium or not .
'''

#human unreadable one liner
def disarium_number(number):
    return "Disarium !!" if sum(int(str(number)[n])**(n+1) for n in range(len(str(number)))) == number else "Not !!"
