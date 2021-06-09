# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(names)
num_items = len(names)
print(f"length {num_items}")
import random
#1.a Random Number Module Function
random_integer = random.randint(1,num_items-1)
print(random_integer)
person=names[random_integer]
#print(person)
print(f"{person} is going to pay the bill")




