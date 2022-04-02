'''
  Starter Code for number guessing game
  
  Please enter your team members names here:
brenda m.
'''

import random
answer = random.randint(1, 100)

# Begin your code here

x = input('What is your name: ')
print('Hi, ' + x + '!' + '\n' + '\t' + 'Please guess a number from 1 to 100.')

y = int(input('Your ' + 'guess: '))

while answer != 'y':
  print
  if y > answer:
    print('Too High') 
    y = int(input('Guess again, ' + x + ':'))
  elif y < answer:
    print('Too Low') 
    y = int(input('Guess again, ' + x + ':'))
  else:
    print('Win')
    break
    print
