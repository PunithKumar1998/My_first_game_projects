#import

import random

#variable 1
dice = 6

#variable 2
position = random.randint(1,6)

#variable 1 = variable 1 + variable 2
dice = dice + position

#print(invite)
print("wellcom, let's play a game of dice")

#output print
name = input('what is ur name:?').strip()
print('hello {}!, are u ready to play'.format(name))

#if the player is ready to play
S = input("press S to play ")
if  S == 's':
     print('the dice rolled , and u got the number {}'.format(position))
elif S != 's':
     print("press S to continue")
     
#loop
while True:
     import random
     position = random.randint(1,6) #for the number to change 
     
     input_ = input('do u want to continue(y/n)?') #if the user wants to continue
     if input_ == 'y':
          print('the dice rolled , and u got the number {}'.format(position))
          #print("let's play again ")

     else:
          print("see u later {}".format(name))
          break


