# Child class 1
class Thar:
    def black(self):
        model="Thar"
        print("Model of Car is :", model)
# Child class 2
class Scorpio:
    def white(self):
        model2= "Scorpio"
        print("Model of Car is :",model2)
# Prent class 
class TS(Thar, Scorpio):
    car="Models"
    print(car,"of the Cars: ")

d = TS()
d.black()
d.white()
