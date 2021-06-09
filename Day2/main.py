# Primitive Data Types

# String
print("Hello[0]")  # Print 'H'

print("123"+"345") # It world Print "123345"

# Integer
print(123+345) # It would print 468
#123_456_789 # It would print 123,456,789

# Float
# 3.1459 

# Type Error and Type Conversion
#1. We cannot concatenate string with integer
variable_name=2
type(variable_name) # Gives the data type of the variable
num_char=len(input("what is your name?")) # num_char is an integer
#2.String to integer
variable_name="aman"
integer_number = int(variable_name)
#3.Integer to String
variable_name=2
string_num = str(variable_name)

# Mathematical Opeations in Python
#1.Addition '+'
#2.Subtraction '-'
#3.Multiplication '*'
#4.Division '/' Note:Always results in floating point number
#5.Exponent '**' 2 raised to 3 written as (2**3)
#Order of Priority PEMDAS

# Round Function
print(8/3) #Float
print(8//3) #Integer
number = round(8/3,2) # It rounds to 2 digits after decimal

# f-string: used to concatenate string with integers
# example:
score=0
height=1.9
isWinning=True
print(f"Your score is {score},your height is {height},you arr winning is {isWinning}")

# Day2 Done

