# a class in a compositoin of properties and methods
# an object is an instance of a class

class Human:
    def __init__(self, Name, Occupation):
        self.name = Name
        self.occupation = Occupation

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "playes Tennis")
        elif self.occupation == "actor":
            print(self.name, "shoort film")

    def speaks(self):
        print(self.name, "says how are you ?")


tom = Human("Tom cruse", "actor")
tom.do_work()
tom.speaks()
