#Slicing in Python

list = ["a","b","c","d","e","f"]

# slice list from 2nd position to 5th position
list.slice[2:5]

# slice list starting from 2nd position to end of list
list.slice[2:]

# slice list from start to 5th position
list.slice[:5]

# set slice counter
list.slice[2:5:2]
# here third part is slice increment counter
# output [c,e]

# prist every second element of  list from start 
list.slice[::2]

# print list from end
list.slice[::-1]