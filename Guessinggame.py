import random

print("Guess a number from 1 to 10!\n To exit the programm type 'Exit'")
Lives = 3
randnum = random.randint(0,10)
while True:
  print(f'You have {Lives} lives left...\n\n')
  Uinput = input('Type here your number: ')
  try:
    Guess = int(Uinput)
    if Guess == randnum:
      print(f"{randnum} was the right number! You won!")
      break
    else:
      if Guess >= randnum:
        print('That number is to big!')
      else:
        print('That number is to small')
      Lives -= 1
    if Lives == 0:
      print('You lost D:')
      break
  except:
    if Uinput == 'Exit':
      break
    else:
      print('Please enter a valid value')
print('\n\nprogram has finished')
