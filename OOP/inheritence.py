class Vehicle:
    def general_usage(self):
        print("General usage is to provide Transportation")


class Car(Vehicle):
    def __init__(self):
        print("I'm Car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("Specific usage: Commute to work, vacation with family")


class MotorCycle(Vehicle):
    def __init__(self):
        self.wheels = 2
        self.roof = False

    def specific_usage(self):
        print("Specific usage: Road trip, Racing ")


c = Car()
c.general_usage()
c.specific_usage()
b = MotorCycle()
b.general_usage()
b.specific_usage()
