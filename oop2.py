class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    pass
    def details(self):
        print(f"my name is {self.name} and my age is {self.age}")
p1 = person("mike",18)
p1.details()        



class employee(person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
    pass
    def details(self):
        print(f"my name is {self.name}  my age is {self.age} and my salary is {self.salary}")
p2 = employee("mike",18,15000)
p2.details()