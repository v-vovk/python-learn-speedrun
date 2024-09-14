class Car:
    def __init__(self, make: str, model: str, year: int, odometer_reading: int = 0) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading
    ...

volvo: Car = Car("Volvo", "XC90", 2022)
print(volvo.make)
print(volvo.model)
print(volvo.year)
print(volvo.odometer_reading)

bmw: Car = Car("BMW", "X5", 2023, 100000)