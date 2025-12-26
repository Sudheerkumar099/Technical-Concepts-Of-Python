from parent import Parent
class Student(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
       

S = Student("Sudheer",22)
print(S.species)
print(S.name)