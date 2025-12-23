from parent import Parent
class Student(Parent):
    def __init__(self,name,age):
        #super().__init__(name)
        self.name=name
        self.age = age
        print("sdfghjkl")
       
p = Parent("abc")

