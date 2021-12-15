class Car():
    def __init__(self, make, model, color, year, is_clean=False):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.is_clean = is_clean

    def wash(self):
        if not self.is_clean:
            self.is_clean=True

car = Car(
    make="Subaru",
    model="Legacy",
    color="Graphite Gray",
    year=2013
)

print(car.make, car.model, car.color, car.year, car.is_clean, sep="\n")
print()

truck = Car(
    make="RAM",
    model="Big One",
    color="Red",
    year=2015,
    is_clean=True
)

print(truck.make, truck.model, truck.color, truck.year, truck.is_clean, sep="\n")
print(car.is_clean)
car.wash()
print(car.is_clean)
truck.wash()
