from data_access.entity.base_entity import BaseEntity


class UserEntity(BaseEntity):

    def __init__(self, id: int, username: str, password: bytes, country: str, cars: list) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.country = country
        self.cars = cars

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_country(self):
        return self.country

    def get_cars(self):
        return self.cars
                
    def to_json(self):
        cars_obj = self.__dict__.get("cars")
        if cars_obj:
            cars_json = [car.to_json() for car in cars_obj]
            self.__dict__["cars"]= cars_json
        return self.__dict__
    

            