class Car:
    def __init__(self, make: str, model: str, year: int, odometer_reading: int = 0) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def drive(self) -> None:
        print(f"Driving {self.make} is driving.")

    def get_info(self) -> None:
        print(f"{self.year} {self.make} {self.model} with {self.odometer_reading} miles on the odometer.")

volvo: Car = Car("Volvo", "XC90", 2022)

volvo.drive()
volvo.get_info()