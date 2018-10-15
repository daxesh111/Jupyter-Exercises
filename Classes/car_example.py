class Vehicle:
    def __init__(self, VIN, Manufacturer, Weight):
        self.vin_n = VIN
        self.Manufact = Manufacturer
        self.wei = Weight
    def GetWeight(self):
        return self.wei
    def GetVIN(self):
        return self.vin_n
    def getManufact(self):
        return self.Manufact
class Car(Vehicle):
    def __init__(self, VIN, Manufacturer, Weight, Seats):
        self.vin_n = VIN
        self.Manufact = Manufacturer
        self.wei = Weight
        self.Seats = Seats
    def NumberofSeats(self):
        return self.Seats
    def VehicleType(self):
        return "This is Car"

class Truck(Vehicle):
    def __init__(self, VIN, Manufacturer, Weight, Capacity):
        self.vin_n = VIN
        self.Manufact = Manufacturer
        self.wei = Weight
        self.Capacity = Capacity
    def TransporationCapacity(self):
        return self.Capacity
    def VehicleType(self):
        return "This is Truck"

a = Car("ABC78910", "MERCE", 100, 5)
b = Truck("DAXESHTRUCKVIN", "ISUZU", 1000, 10000)
c = Car("DEFthird" , "BMW", 50, 2)

x = [i for i in [a,b,c]]

for i in x:
    print(i.getManufact(), i.VehicleType())
