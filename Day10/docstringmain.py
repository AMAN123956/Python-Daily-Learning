#Docstring 
# =================================================================
# Uses:
# 1.Can Also be used as multiline-comment
# 2.Are a way to create a little bit of documentation for our function
# 3.Comes after function definition

#example
def format_name(f_name,l_name):
    '''Take a first and last name and format it to return a title
        case version of the name.'''
    
    name=f_name.title()+l_name.title()
    return name

print(format_name("aman","Dixit"))
