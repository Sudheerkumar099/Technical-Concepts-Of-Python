from parent import Parent
class Child(Parent):
    def fun(self):
        print("This is from child")
        
    def __init__(self,name,age):
        self.name = name
        self.age = age
               
c = Child("sudheer",22)
print(c.name)
del c.name
# print(c.name)
c.fun()
c.pfun()
print(c.species)
