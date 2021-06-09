# Dictionary
{key: value}
#example:
programming_dictionary = {
    "France":"Paris",
    "India":"New Delhi",
}

#Access Particular Properties in a list
programming_dictionary["France"]   #syntax:dictionary_name[key]

#Adding New Items to the Dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])