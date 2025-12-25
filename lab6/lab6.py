class UserAccount:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password: str) -> None:
        self.__password = new_password

    def check_password(self, password: str) -> bool:
        return self.__password == password

class Vehicle:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def get_info(self) -> str:
        return f"brand: {self.make}, model: {self.model}"

class Car(Vehicle):
    def __init__(self, make: str, model: str, fuel_type: str):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self) -> str:
        return f"brand: {self.make}, model: {self.model}, fuel type: {self.fuel_type}"

# Задание 1
user = UserAccount("Damn", "gmuserbetch@gmail.com", "12345678")
print(user.check_password("12345678"))
user.set_password("abcd")
print(user.check_password("12345678"))
print(user.check_password("abcd"))

# Задание 2
vehicle = Vehicle("kia", "rio")
print(vehicle.get_info())

car = Car("BMW", "MP3", "diesel")
print(car.get_info())
