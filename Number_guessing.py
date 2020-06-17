from random import randint  #import random

guess_range = randint(0,100) #guessing range(random)

#print(guess_range) #to check the condition try this 

name = input('please enter ur name to start the game:')
print('hello {}! wellcome to GUESS THE NUMBER'.format(name))

s = input("press s to start the game :").lower()
if s == 's':
    guess_number = int(input('enter the number that u r guessing the range is from  0-100:'))
#uess_number = int(input('enter the number that u r guessing the range is from 0-100:'))
elif s != 's':
    print('wrong choice , press s to start the game :')

if guess_number == guess_range:
    print('the number u guessed is correct')
else:
    print('wong number')
    print('the random number that is generated is :{} '.format(guess_range))
    
    
while True:
    from random import randint
    guess_range = randint(0,100)
    #print(guess_range)

    input_ = input('do u want to continue(y/n)')

    if input_ == 'y':
        guess_number = int(input('enter the number that u are guessing :'))
        
        if guess_number == guess_range:
            print('the number u guessed is correct')
        else:
            print('wrong number')

    else:
        print('bye {} , better luck next time'.format(name))
        break