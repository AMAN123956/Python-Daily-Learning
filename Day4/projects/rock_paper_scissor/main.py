rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
list=[rock,paper,scissors]
# Random Number to help select computer
random_integer = random.randint(0,2)
# User Choice
user_choice = int(input("Enter Your Choice: 0-Rock,1-Paper,2-Scissors.What is your choice?"))
# Checking Result
if(user_choice==0):
  print(list[0])
  print("Computer Choice:")
  print(list[random_integer])
  if(random_integer==2):
    print("Congrats,You Won!!!")
  elif(random_integer==0):
    print("OOPs!,Game is Tied")
  else:
    print("Bad Luck!,Computer Won!!!")
elif(user_choice==1):
  print(list[1])
  print("Computer Choice:")
  print(list[random_integer])
  if(random_integer==0):
    print("Congrats,You Won!!!")
  elif(random_integer==1):
    print("OOPs!,Game is Tied")
  else:
    print("Bad Luck!,Computer Won!!!")
else:
  print(list[2])
  print("Computer Choice:")
  print(list[random_integer])
  if(random_integer==1):
    print("Congrats,You Won!!!")
  elif(random_integer==2):
    print("OOPs!,Game is Tied")
  else:
    print("Bad Luck!,Computer Won!!!")