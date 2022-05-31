class person:
    def __init__(self,name,yob,mass,height):
        self.name = name
        self.yob = yob
        self.mass = mass
        self.height = height
        age = 2022 - yob
        bmi = mass/((height/100)*(height/100))
        print("my age is", age)
        print("BMI is", bmi)
    pass
    def details(self):
        print(f"my name is {self.name} i was born in {self.yob}")
        print(f"mass is {self.mass} height is {self.height}")
p1 = person("mike",2004,67,180)
p1.details()

        



class teacher:
    def __init__(self,name,yob,mass,height,subject,salary):
        self.name = name
        self.yob = yob
        self.mass = mass
        self.height = height
        self.subject = subject
        self.salary = salary
        age = 2022 - yob
        bmi = mass/((height/100)*(height/100))

        print("my age is", age)
        print("BMI is", bmi)
    pass
    def details(self):
         print(f"my name is {self.name} i was born in {self.yob}")
         print(f"i teach {self.subject} and i earn {self.salary}")
         print(f"mass is {self.mass} height is {self.height}")
p2 = teacher("beth",1984,71,167,"math",140000)
p2.details()


class student:
    def __init__(self,name,yob,mass,height,fav_subject,Class):
        self.name = name
        self.yob = yob
        self.mass = mass
        self.height = height
        self.fav_subject = fav_subject
        self.Class = Class
        age = 2022 - yob
        bmi = mass/((height/100)*(height/100))
        print("my age is", age)
        print("BMI is", bmi)
    pass 
    def details(self):
         print(f"my name is {self.name} i was born in {self.yob}")
         print(f"my favourite subject is {self.fav_subject} and my class is {self.Class}")
         print(f"mass is {self.mass} height is {self.height}")
p3 = student("francis",2006,68,174,"french","3A")
p3.details()         