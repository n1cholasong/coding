#Pokemon - alpha 0.3.0
import time
from random import randint

print('Welcome to Pokemon - Alpha')
input('( Press enter to continue... )')

print('Loading', end = '')
for dot in range(3):
    time.sleep(0.55)
    print('.', end = '')

print('\n')

p1 = input('Player 1, what is your name? ')
p2 = input('Player 2, what is your name? ')
print('')
print('Welcome to Pokemon %s and %s!' %(p1, p2))
print('')

print('%s, choose your Pokemon!' %(p1))
s1 = input('z - Charmander\nx - Pikachu\n').lower()
print('')

if s1 == 'z':
    print('Player 1: Charmander!')
    poke1 = 'Charmander'
      
elif s1 == 'x':
    print('Player 1: Pikachu!')
    poke1 = 'Pikachu'

print('')
print('%s, choose your Pokemon!' %(p2))
s2 = input('z - Charmander\nx - Pikachu\n').lower()
print('')

if s2 == 'z':
    print('Player 2: Charmander!')
    poke2 = 'Charmander'
      
elif s2 == 'x':
    print('Player 2: Pikachu!')
    poke2 = 'Pikachu'

print('')

print('%s v/s %s' %(poke1, poke2))

print('Battle starting in', end = ' ')
for num in range(3 , 0, -1):
    time.sleep(1)
    print(num, end = ' ')
print('FIGHT!\n')

game = True
poke1_health = 100
poke2_health = 100

while game:
    print("%s's turn\nWhat will %s do?" %(p1, poke1))
    b1 = input('q - FIGHT\nw - RUN\n')
    player1 = True
    print('')
    while player1:
        if b1 == 'q':
            f1 = input('What will %s do next?\nq - TACKLE\nw - BITE\ne - HEADBUTT\nr - SCRATCH\n' %(poke1))
            if f1 == 'q':
                poke2_health = poke2_health - randint(5,10)
                input('%s used TACKLE' %(poke1))
                time.sleep(0.55)
                input('%s: %s/100' %(poke2, poke2_health))
                player1 = False
                player2 = True
                print('')
            elif f1 == 'w':
                poke2_health = poke2_health - randint(5,15)
                input('%s used BITE' %(poke1))
                time.sleep(0.55)
                input('%s: %s/100' %(poke2, poke2_health))
                player1 = False
                player2 = True
                print('')
            elif f1 == 'e':
                poke2_health = poke2_health - randint(10,20)
                input('%s used HEADBUTT' %(poke1))
                time.sleep(0.55)
                input('%s: %s/100' %(poke2, poke2_health))
                player1 = False
                player2 = True
                print('')
            elif f1 == 'r':
                poke2_health = poke2_health - randint(15,20)
                input('%s used SCRATCH' %(poke1))
                time.sleep(0.55)
                input('%s: %s/100' %(poke2, poke2_health))
                player1 = False
                player2 = True
                print('')
        elif b1 == 'w':
            print('%s has fled, %s won the battle!' %(p1, p2))
            player1 = False
            player2 = False
            game = False
        
    while player2:
        print("%s's turn\nWhat will %s do?" %(p2, poke2))
        b2 = input('q - FIGHT\nw - RUN\n')
        print('')
        if b2 == 'q':
            f2 = input('What will %s do next?\nq - TACKLE\nw - BITE\ne - HEADBUTT\nr - SCRATCH\n' %(poke2))
            if f2 == 'q':
                poke1_health = poke1_health - randint(5,10)
                input('%s used TACKLE' %(poke2))
                time.sleep(0.55)
                input('%s: %s/100' %(poke1, poke1_health))
                player2 = False
                player1 = True
                print('')
            elif f2 == 'w':
                poke1_health = poke1_health - randint(5,15)
                input('%s used BITE' %(poke2))
                time.sleep(0.55)
                input('%s: %s/100' %(poke1, poke1_health))
                player2 = False
                player1 = True
                print('')
            elif f2 == 'e':
                poke1_health = poke1_health - randint(10,20)
                input('%s used HEADBUTT' %(poke2))
                time.sleep(0.55)
                input('%s: %s/100' %(poke1, poke1_health))
                player2 = False
                player1 = True
                print('')
            elif f2 == 'r':
                poke1_health = poke1_health - randint(15,20)
                input('%s used SCRATCH' %(poke2))
                time.sleep(0.55)
                input('%s: %s/100' %(poke1, poke1_health))
                player2 = False
                player1 = True
                print('')
        if b2 == 'w':
            print('%s has fled, %s won the battle!' %(p2, p1))
            player2 = False
            player1 = False
            game = False

    if poke1_health <= 0:
        input('%s has fainted, %s won!' %(poke1, poke2))
        input('%s grew to LV. 100!' %(poke2))
        player1 = False
        player2 = False
        game = False
              
    if poke2_health <= 0:
        input('%s has fainted, %s won!' %(poke2, poke1))
        input('%s grew to LV. 100!' %(poke1))
        player1 = False
        player2 = False
        game = False
        
print('Game Over!')

            
           
        
        
    


       

                   
    
