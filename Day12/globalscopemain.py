
#Global and Local Scope
# =======================================================================

enemies=1
def increase_enemies():
    enemies=2
    print(f"enemies inside function {enemies}")

increase_enemies()
print(f"Enemies outside the function {enemies}")

#output 21 
#expected output 22
#Reason because enemies variable inside function is separate new variable with name same as global 
# enemy variable so when we are incrementing inside the function we are incrementing local variable not global enemies variable

#Modifyiong Global Variable
score=10
def increase_score():
    global score
    score +=1
    print(f"score variable inside function {score}")

increase_score()
print(f"score variable outside function {score}")

#Output 22
#Expected Output 22

#Note Global Constant Variables are declared in capital letters
PI=3.14
=======
#Global and Local Scope
# =======================================================================

enemies=1
def increase_enemies():
    enemies=2
    print(f"enemies inside function {enemies}")

increase_enemies()
print(f"Enemies outside the function {enemies}")

#output 21 
#expected output 22
#Reason because enemies variable inside function is separate new variable with name same as global 
# enemy variable so when we are incrementing inside the function we are incrementing local variable not global enemies variable

#Modifyiong Global Variable
score=10
def increase_score():
    global score
    score +=1
    print(f"score variable inside function {score}")

increase_score()
print(f"score variable outside function {score}")

#Output 22
#Expected Output 22

#Note Global Constant Variables are declared in capital letters
PI=3.14
