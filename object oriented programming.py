class dog:
    def __init__(self,no_of_eyes,color,no_of_legs):
        self.no_of_eyes =no_of_eyes
        self.color = color
        self.no_of_legs = no_of_legs
        pass
    def barking(self):
        print("woof woof!")
    def walking(self):
        print("running")    
german_shephard = dog(no_of_eyes=2,color='grey',no_of_legs=4)
dodger = dog(no_of_eyes=1,color='white',no_of_legs=4)
dobberman = dog(2,'brown',3)
print(dodger.no_of_eyes)
print(german_shephard.color,dobberman.no_of_eyes)
dobberman.color = ('black')
print(dobberman.color)    
dobberman.barking()        
dodger.walking()
print(dodger.no_of_legs)