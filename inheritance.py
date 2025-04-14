class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
            print(self.firstname, self.lastname)
class student(person):
     def __init__(self, fname, lname, year):
           super().__init__(fname, lname)
           self.graduationyear = year

     def welcome(self):
          print("welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = student("Yuva", "Teja",2018)
x.welcome()

