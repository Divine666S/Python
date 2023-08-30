

class Car:
    def name(self):
        print("It's a Car")

class Thar(Car):
    def black(self):
        print("It is a Black Thar")

class Scorpio(Car):
    def white(self):
        print("It is a White Scorpio")

 
def display(self):
    self.black()
    self.white()

print("Cars:")
d=Scorpio()
d.name()   
d.display()   