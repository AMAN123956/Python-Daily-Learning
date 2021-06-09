
  #Number Guessing Game Objectives:

  # Include an ASCII art logo.
  # Allow the player to submit a guess for a number between 1 and 100.
  # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
  # If they got the answer correct, show the actual answer to the player.
  # Track the number of turns remaining.
  # If they run out of turns, provide feedback to the player. 
  # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random
print(art.logo)
# Easy Level
def easy_game():
  attempt_count=10
  print(f"You have {attempt_count} attempts remaining to guess the number")
  while(attempt_count>0):
    guess_number = int(input("Make a Guess:"))
    result=check_result(guess_number)
    if result==1:
      print(f"You got it!, the answer was {computer_choice}")
      attempt_count=0
    elif result==2:
      print('''Too High.\nGuess again.''')
      attempt_count = attempt_count-1
      print(f"You have {attempt_count} attempts remaining to guess the number.")
    else:
      print('''Too Low.\nGuess again.''')
      attempt_count = attempt_count-1
      print(f"You have {attempt_count} attempts remaining to guess the number.")

  # Difficult Level
def hard_game():
  attempt_count=5
  print(f"You have {attempt_count} attempts remaining to guess the number")
  while(attempt_count>0):
    guess_number = int(input("Make a Guess:"))
    result=check_result(guess_number)
    if result==1:
      print(f"You got it!, the answer was {computer_choice}")
      attempt_count=0
    elif result==2:
      print('''Too High.\nGuess again.''')
      attempt_count = attempt_count-1
      print(f"You have {attempt_count} attempts remaining to guess the number.")
    else:
      print('''Too Low.\nGuess again.''')
      attempt_count = attempt_count-1
      print(f"You have {attempt_count} attempts remaining to guess the number.")
# Check Result of Guess
def check_result(guess_number):
  if guess_number == computer_choice:
    return 1
  elif guess_number>computer_choice:
    return 2
  else:
    return 0

  # Computer Choice
computer_choice=random.randint(1,100)
print("I'm thinking of a number between 1 to 100")
print(f"Psst,the correct answer is {computer_choice}")
# Taking difficulty level from user
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if(difficulty_level == "easy"):
  easy_game()
else:
  hard_game()

=======
  #Number Guessing Game Objectives:

  # Include an ASCII art logo.
  # Allow the player to submit a guess for a number between 1 and 100.
  # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
  # If they got the answer correct, show the actual answer to the player.
  # Track the number of turns remaining.
  # If they run out of turns, provide feedback to the player. 
  # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random
print(art.logo)
# Easy Level
def easy_game():
  attempt_count=10
  print(f"You have {attempt_count} attempts remaining to guess the number")
  while(attempt_count>0):
    guess_number = int(input("Make a Guess:"))
    result=check_result(guess_number)
    if result==1:
      print(f"You got it!, the answer was {computer_choice}")
      attempt_count=0
    elif result==2:
      print('''Too High.\nGuess again.''')
      attempt_count = attempt_count-1
      print(f"You have {attempt_count} attempts remaining to guess the number.")
    else:
      print('''Too Low.\nGuess again.''')
      attempt_count = attempt_count-1
      print(f"You have {attempt_count} attempts remaining to guess the number.")

  # Difficult Level
def hard_game():
  attempt_count=5
  print(f"You have {attempt_count} attempts remaining to guess the number")
  while(attempt_count>0):
    guess_number = int(input("Make a Guess:"))
    result=check_result(guess_number)
    if result==1:
      print(f"You got it!, the answer was {computer_choice}")
      attempt_count=0
    elif result==2:
      print('''Too High.\nGuess again.''')
      attempt_count = attempt_count-1
      print(f"You have {attempt_count} attempts remaining to guess the number.")
    else:
      print('''Too Low.\nGuess again.''')
      attempt_count = attempt_count-1
      print(f"You have {attempt_count} attempts remaining to guess the number.")
# Check Result of Guess
def check_result(guess_number):
  if guess_number == computer_choice:
    return 1
  elif guess_number>computer_choice:
    return 2
  else:
    return 0

  # Computer Choice
computer_choice=random.randint(1,100)
print("I'm thinking of a number between 1 to 100")
print(f"Psst,the correct answer is {computer_choice}")
# Taking difficulty level from user
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if(difficulty_level == "easy"):
  easy_game()
else:
  hard_game()
