# Inheritance 
# Is alike a super class

class Animal:
    def __init__(self):
        self.num_eyes=2
    
    def breathe(self):
        print("Inhale,Exhale!")


#Sub Class

class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def swim(self):
        print("moving in water!")


nemo=Fish()
nemo.swim()
#Calling method of Super Class
nemo.breathe()
print(nemo.num_eyes)


# Modifying Super Class

class Fish(Animal):

    def breathe(self):
        super.breathe()  # Inherits all things that super class does
        print("doing this")