# Клас продукту
class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.color = None

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color})"


# Клас Будівника
class CarBuilder:
    def __init__(self):
        self.car = Car()

    def build_make(self):
        pass

    def build_model(self):
        pass

    def build_year(self):
        pass

    def build_color(self):
        pass

    def get_car(self):
        return self.car


# Клас Керівника (Director)
class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        self.builder.build_make()
        self.builder.build_model()
        self.builder.build_year()
        self.builder.build_color()


# Клас конкретного будівника
class SportsCarBuilder(CarBuilder):
    def build_make(self):
        self.car.make = "Ferrari"

    def build_model(self):
        self.car.model = "458 Italia"

    def build_year(self):
        self.car.year = 2023

    def build_color(self):
        self.car.color = "Red"


# Клас іншого конкретного будівника
class SUVBuilder(CarBuilder):
    def build_make(self):
        self.car.make = "Jeep"

    def build_model(self):
        self.car.model = "Grand Cherokee"

    def build_year(self):
        self.car.year = 2023

    def build_color(self):
        self.car.color = "Blue"


# Використання патерну Будівника
if __name__ == "__main__":
    # Використання будівника для спортивного автомобіля
    sports_car_builder = SportsCarBuilder()
    director = CarDirector(sports_car_builder)
    director.construct_car()
    sports_car = sports_car_builder.get_car()
    print("Sports Car:", sports_car)

    # Використання будівника для SUV
    suv_builder = SUVBuilder()
    director = CarDirector(suv_builder)
    director.construct_car()
    suv = suv_builder.get_car()
    print("SUV:", suv)
    