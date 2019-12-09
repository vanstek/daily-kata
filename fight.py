#Two fighters, one winner.
#Level: 7 kyu
'''
Create a function that returns the name of the winner in a fight between two fighters.
Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.
Each fighter will be a Fighter object/instance.
'''
def declare_winner(fighter1, fighter2, first_attacker):  
    if first_attacker == fighter1.name:
        while(fighter1.health > 0 and fighter2.health > 0):
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name          
    else:
        while(fighter1.health > 0 and fighter2.health > 0):    
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name
         
