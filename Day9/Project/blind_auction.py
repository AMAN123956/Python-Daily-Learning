from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
choice=True
bid_desc={}
while(choice==True):
  clear()
  name=input("Enter Name:")
  bid_amt = int(input("Enter Your Bid Amt:"))
  bid_desc[name] = bid_amt
  play=input("Are there any other users who want to bid?(y|n)")
  if play=='y':
    choice=True
  else:
    choice=False

for key in bid_desc:
  max_amt=0
  name=""
  if(bid_desc[key]>max_amt):
    max_amt=bid_desc[key]
    name=key

print(f"{name} wins the bid with a bid of ${max_amt}")