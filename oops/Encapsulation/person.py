class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age
  def getage(self):
      return self.__age
  def setage(self,age):
      self.__age=age

p1 = Person("Emil", 25)
print(p1.name)
p1.setage(30)
print(p1.getage())
