<<<<<<< HEAD
import utils



# check availability
def check(response,type):
    if(utils.resources[type]>=utils.MENU[response]['ingredients'][type]):
        return True
    else:
        return False

        
# insert_coin function
def insert_coin(cost):
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    q = int(input("How many Quarters?"))
    d = int(input("How many dimes?"))
    n = int(input("How many nickles?"))
    p = int(input("How many Pennies?"))
    total_cost = q*quarters+d*dimes+n*nickles+p*pennies
    print(total_cost,cost)
    return total_cost


def coffee(response):
    if(response=="report"):
        for item in utils.resources:
           print(f"{item}:{utils.resources[item]}")
        getchoice() 
    else:
        r1=check(response,"water")
        r2=check(response,"milk")
        r3=check(response,"coffee")
        print(r1,r2,r3)
        if(r1 and r2 and r3):
            cost=utils.MENU[response]["cost"]
            total_cost=insert_coin(cost)
            if(total_cost>cost):
                change=total_cost-cost
                print(f"Here is ${change} in change")
                utils.resources["money"] = utils.resources["money"]+change
                getchoice()
            else:
                print("Sorry that's not enough money, Money refunded!!!")

                
        else:
            print("Sorry there are not enough ingredients!!!")


def getchoice():
    response = input("What would you like?")
    coffee(response)

getchoice()





=======
import utils



# check availability
def check(response,type):
    if(utils.resources[type]>=utils.MENU[response]['ingredients'][type]):
        return True
    else:
        return False

        
# insert_coin function
def insert_coin(cost):
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    q = int(input("How many Quarters?"))
    d = int(input("How many dimes?"))
    n = int(input("How many nickles?"))
    p = int(input("How many Pennies?"))
    total_cost = q*quarters+d*dimes+n*nickles+p*pennies
    print(total_cost,cost)
    return total_cost


def coffee(response):
    if(response=="report"):
        for item in utils.resources:
           print(f"{item}:{utils.resources[item]}")
        getchoice() 
    else:
        r1=check(response,"water")
        r2=check(response,"milk")
        r3=check(response,"coffee")
        print(r1,r2,r3)
        if(r1 and r2 and r3):
            cost=utils.MENU[response]["cost"]
            total_cost=insert_coin(cost)
            if(total_cost>cost):
                change=total_cost-cost
                print(f"Here is ${change} in change")
                utils.resources["money"] = utils.resources["money"]+change
                getchoice()
            else:
                print("Sorry that's not enough money, Money refunded!!!")

                
        else:
            print("Sorry there are not enough ingredients!!!")


def getchoice():
    response = input("What would you like?")
    coffee(response)

getchoice()





>>>>>>> 15cd792293402f706cafa95b891709c8f33f1ed8
