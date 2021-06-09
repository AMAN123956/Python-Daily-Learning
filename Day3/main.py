# Conditional Statement
# ============================================================================

# 1. If/else
# if condition:
#    do this
# else:
#    do this
# example

height=int(input("Enter Your Height in CMs"))
if(height>170):
    print("You are eligible")
else:
    print("you are not eligible for ride")

#Note: Colon and indentation matters most in python conditional statements

# Comparison Operators:
# > : Greater Than
# < : Less Than
# >= : Gretaer than or equal to
# <= : Less than or equal to
# == : Equal to (Comparison)
# != : Not equal to

#Nested if statements
if condition:
    if another_condition:
        do this:
    else:
        do this:
else:
    do this

# Nested elif statements
if condition:
    do this
elif condition:
    do this
elif condition:
    do this
else:
    do this

# Leap Year Program
# Logic : On evry year that is evenly divisble by 4
#             except every year year that is evenly divisible by 100
#                unless the year is aklso evenly divisible by 400

# Program
year = int(input("Enter Year?"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("Leap Year")
        else:
            print("Not aLeap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")

#Logical Operators
#1.And 
#2.Or
#3.Not

#Standard Functions
#1.lower() = uppercase to lowercase
print("Aman".lower) #prints aman
#2.count() = Counts particular alphabet in a string
print("Aman".count("a")) # Returns 1 

# Day3 Done