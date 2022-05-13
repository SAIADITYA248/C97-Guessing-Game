run = True
import random
x=random.randint(1,9)
while run:
    user_input = int(input('Enter Number: '))
    if user_input == x:
        print('Congratulations You won!')
        run = False
    else:
        print('Oh You were close! Try Again')
        continue