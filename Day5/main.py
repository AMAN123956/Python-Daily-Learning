# Day5
# ===========================================================================

# For Loops
# example
fruits=["Apple","Peach","Pear"]

for fruit in fruits:
    print(fruit)

#Note: Indentation matters most in case of loops

# Second Kind of For Loop
#When we want to use loops in anything else of list

# range() function:
# syntax: for number in range(a,b) :  creates a range between a to b where b is not include
#example
for number in range(1,5):
    print(number)                      ## Output: 1,2,3,4

# We need to pass a third parameter to the range function when we want to increase by more than one
#example
for number in range(1,5,2):
    print(number)                      ## Output: 1,3


#Example Programs
#1.Sum of even numbers in between 1 to 100
sum_even = 0
for number in range(2,101,2):
    sum_even+=number
print(sum_even)

#2 Fizz Buzz Interview Question
#Write your code below this row 👇

for number in range(1,101):
  if(number%15==0):
    print("fizzBuzz")
  elif(number%3==0):
    print("fizz")
  elif(number%5==0):
    print("Buzz")
  else:
    print(number)
  

# Standard Functions
#1. sum(list_name) > It finds the sum of all elements of list
#2. len(llist_name) > It finds the length of a list
#3. How to print all items of list in single line
 for item in list_name:
     print(item,end=" ")

#4 . How to print items of list in random order
import random
words=["Aman","Abhishek","Arushi","Virat"]
random.shuffle(words)     ## Note:It modifies original list

# If we don't want original list to be modified then we should use random.sample()


