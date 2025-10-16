class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is starting")

    def drive(self, distance):
        print(f"The {self.make} {self.model}'s drive is {distance} km.")

    def stop_engine(self):
        print(f"The {self.make} {self.model}'s engine is stopping")


car1 = Car("Mercedes", "SL500", 2022)
car2 = Car("Toyota", "Corolla", 2021)
car3 = Car("BMW", "330", 2021)

car1.start_engine()
car2.start_engine()
car3.start_engine()
car1.drive(100)
car2.drive(100)
car3.drive(100)
car1.stop_engine()
car2.stop_engine()
car3.stop_engine()

# dunder method