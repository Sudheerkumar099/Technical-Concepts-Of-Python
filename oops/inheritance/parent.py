class Parent:
    species = "Human" 
    def __init__(self,name):
        self.name = name
        print(self.__dict__)
    
    def pfun(self):
        print("Parent")
            
