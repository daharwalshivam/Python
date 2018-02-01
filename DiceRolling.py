#This program can roll dies and give random output

from random import randint
def roll(min = 1 , max = 6):
    return randint(min,max)

again = 'y'
print('======== ROLLING THE DICE ========')
while again == 'y' or again == 'Y':
    var = input('press R to Roll the Dice: ')
    if var == 'r' or var == 'R':
        print(roll())
        again = input('Do u want to roll the dice again (Y/N)? ')
