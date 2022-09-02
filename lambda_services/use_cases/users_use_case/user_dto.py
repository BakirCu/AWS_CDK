import json
from exeption_handling.lambda_exceptions import BadRequestException
from use_cases.cars_use_case.car_dto import CarDto
from lambda_helpers.base_dto import BaseDto
from base64 import b64encode
import hashlib
import logging


LOG = logging.getLogger() 
LOG.setLevel(logging.INFO)


class UserDto(BaseDto):
    def __init__(self, id: int, username: str, password: bytes, country: str, cars: json) -> None:
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

    def get_cars(self):
        return self.cars

    def add_car(self, id, type):
        self.cars.append(CarDto(id, type))
        
    @staticmethod
    def hash_password(password: str, key: str) -> str:
        hash_password = hashlib.pbkdf2_hmac("sha256",
                                            password=password.encode("utf-8"),
                                            salt=key.encode("utf-8"),
                                            iterations=100000
                                            )
        return b64encode(hash_password).decode('ascii')

    @staticmethod
    def from_dict(data: dict) -> object:
        LOG.info(data)
        id = data.get("id")
        username = data.get("username")
        password = data.get("password")
        if not (id or username or password):
            raise BadRequestException("Please provide valid data")
        country = data.get("country")
        password_hash = UserDto.hash_password(password, 
                                            "opo42p590sadiyuf9SASK_dsa)(*",
                                            )
        cars = data.get("cars")
        cars_dto = []
        if cars:
            for car in cars:
                cars_dto.append(CarDto.from_dict(car))
        return UserDto(id=id, username=username, password=password_hash, country=country, cars=cars_dto)
