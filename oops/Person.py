class Human:
    def eat(self):
        print(f"{self.name} is eating")

class Person(Human):
    def __init__(self,name,age=18):
        super().__init__()
        self.name=name
        self.age=age
              
    def print_name(self):
        print(self.name)
        
    def print_age(myobject):
        print(myobject.age)
        
    def __add__(self,other):
        return self.age + other.age
    
    def __str__(self):
        return f"name is  {self.name} age is {self.age}"
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
    def __eq__(self,other):
        return self.name == other.name
    
    def __len__(self):
        return len(self.name)
    
    def __getitem__(self,index):
        return self.name[index]
    
    def __call__(self):
        return self.age*2
    


'''p1 = Person("Emil")
p2 = Person("Tobias", 25)
print(p1.name, p1.age)
print(p2.name, p2.age)'''

sudheer = Person("Sudheerr")
willy = Person("Willy")
john = Person("John")

'''abc.print_name()
abc.print_age()
sudheer.print_name()
sudheer.print_age()'''

#__str__ funtions
print(sudheer)

#__add__ function
print(sudheer + willy)

#__repr__ function
print(repr(sudheer))
text =  repr(sudheer)
sudheer2 = eval(text)
print(repr(sudheer2))
print(sudheer is sudheer2)

#Del
del john
#print(john)

#super()
sudheer.eat()

#__eq__ funtion
print(sudheer == sudheer2)
print(sudheer == willy)

#__len__
name = (Person([sudheer.name,willy.name,"John",23]))
print(type(name))
print(len(name))

#__getItem__ function
print(name[3])

#call function
person3 = Person(name="ajay")
print(sudheer())
print(repr(sudheer))
