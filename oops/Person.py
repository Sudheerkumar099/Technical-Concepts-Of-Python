class Person:
    def __init__(self,name,age=18):
        self.name=name
        self.age=age
        
    def print_name(self):
        print(self.name)
        
    def print_age(myobject):
        print(myobject.age)

# p1 = Person("Emil")
# p2 = Person("Tobias", 25)

# print(p1.name, p1.age)
# print(p2.name, p2.age)

sudheer = Person("sudheer")
abc = Person("abc",25)

abc.print_name()
abc.print_age()
sudheer.print_name()
sudheer.print_age()