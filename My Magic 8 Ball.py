#My Magic 8 Ball

import time

print('Welcome to Magic 8 Ball')
input('press ENTER to continue')
print('Loading', end = ' ')
for dot in range(3):
    time.sleep(0.55)
    print('.', end = ' ')

name = input('\nWhat is your name?\nName: ').title

q = input('\nAsk a question: ')

print('shaking', end = ' ')
for dot in range(3):
    time.sleep(0.55)
    print('.', end = ' ')

from random import randint

answer = (
    "\nGo for it!",
    "\nNo way, %s!" %(name),
    "\nI'm not sure. Ask me again.",
    "\nFear of the unknown is what imprisons us.",
    "\nIt would be madness to do that!",
    "\nOnly you can save mankind!",
    "\nMakes no ifference to me, do or dont't - whatever.",
    "\nYes, I think on balance that is the right choice."
    )

choice = randint(0,7)
print(answer[choice])

input('\n\nPress the RETURN key to finish.')

