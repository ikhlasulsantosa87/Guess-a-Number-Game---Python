import random

def guessMyNumber(highestNumber):
  secretNumber = random.randint(1, highestNumber)
  ourGuess = 0
  lives = 10
  while ourGuess != secretNumber and lives > 0:
    try:
      ourGuess = int(input('Please enter a number : '))
    except ValueError:
      print('Please, enter a number not a character!')

    if ourGuess < secretNumber:
      print('Sorry, too low!')
      lives = lives - 1
    elif ourGuess > secretNumber:
      print('Sorry, too high!')
      lives = lives - 1

  if ourGuess == secretNumber:
    print(f'Congratulations, you just guessed my number {secretNumber}!')
  elif lives == 0:
    print(f'You lost. The number is {secretNumber}!')

guessMyNumber(100)
