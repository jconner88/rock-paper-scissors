import random

choices = ['rock', 'paper', 'scissors']

while True:
  player_choice = input('Choose rock, paper or scissors: ').casefold()
  computer_choice = random.choice(choices)
  print(f'You chose {player_choice} and your opponent chose {computer_choice}')
  if player_choice == 'rock' and computer_choice == 'scissors':
    print('Congratulations you win!')
    break
  elif player_choice == 'rock' and computer_choice == 'paper':
    print('You lost.')
    break
  elif player_choice == 'paper' and computer_choice == 'rock':
    print('Congratulations you win!')
    break
  elif player_choice == 'paper' and computer_choice == 'scissors':
    print('You lost.')
    break
  elif player_choice == 'scissors' and computer_choice == 'paper':
    print('Congratulations you win!')
    break
  elif player_choice == 'scissors' and computer_choice == 'rock':
    print('You lost.')
    break
  else:
    print('It was a draw.')