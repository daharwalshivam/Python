#this is game based on rock, paper, scissor game

from random import randint
again = 'y'
while again == 'y':
    print('================ ROCK PAPER SCISSORS GAME ==============')
    print('Enter your choice? ')
    player = input('Rock(r),Paper(p) or Scissors(s): ')
    print(player,'vs ',end = '')
    chosen = randint(1,3)
    if chosen == 1:
        computer = 'r'
    elif chosen == 2:
        computer = 'p'
    elif chosen == 3:
        computer = 's'
    print(computer)
    if player == computer:
        print("wow It's a Draw!")
    elif player == 'r' and computer == 's':
        print("You Wins!")
    elif player == 'r' and computer == 'p':
        print("Computer Wins!")
    elif player == 'p' and computer == 's':
        print("Computer Wins!")
    elif player == 'p' and computer == 'r':
        print("You Wins!")
    elif player == 's' and computer == 'p':
        print("You Wins!")
    elif player == 's' and computer == 'r':
        print("Computer Wins!")
    again = input('Do you want to play again?(Y/N)')
