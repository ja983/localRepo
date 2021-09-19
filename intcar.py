#Create a Car class with three class members and two fields and one method

class Car:
    def __init__(self,year,make,model):
        self.year=year
        self.make=make
        self.model=model

    def startEngine(self,str="Vvvrrroooommm!!!"):
        print(str)

    def showYear(self):
        return self.year

maserati=Car(2019,'Maserati','Levante')
maserati

maserati.model

maserati.startEngine()
maserati.startEngine('sputter sputter misfire')

maserati.showYear()
