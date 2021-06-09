import  art
print(art.logo)

import game_data
from replit import clear
print(game_data.data[0]["name"])
list=game_data.data
count=0
def getPerson(count,type):
  
  name = list[count]["name"]
  description = list[count]["description"]
  country = list[count]["country"]
  if type==1:
    print(f"Compare A: {name} , {description}, from {country}")
    count+=0
    return list[count]["follower_count"]
  else:
    print(f"Compare B: {name}, {description}, from {country}")
    return list[count]["follower_count"]
   
current_score=0   
play_more=True
while(play_more != False):
  
  person1=getPerson(count,1)
  #Person2 
  count+=1
  person2=getPerson(count,2)
  user_choice = input("Who has more followers? Type 'A' or 'B'")
  # Check Winner
  def checkWinner(person1,person2,user_choice):
    global current_score
    global play_more
    if person1>person2 and user_choice=='A':
      current_score+=1
      print(f"You're right! Currrent Score:{current_score} ")
      play_more=True
    elif person2>person1 and user_choice=="B":
      current_score+=1
      print(f"You're right! Currrent Score:{current_score} ")
      play_more=True
    else:
      print(f"OOPs!, You lost the Game, Current Score:{current_score}")
      play_more=False
  clear()
  checkWinner(person1,person2,user_choice)
    
    




