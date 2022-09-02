from use_cases.cars_use_case.car_dto import CarDto
from typing import List


def get_car_by_id(id:int, cars: List[CarDto])-> CarDto:
    for car in cars:
        if car.id == id:
            return car
    return CarDto(None, None)


def delete_car_by_id(id:int, cars: List[CarDto])-> CarDto:
    for car in cars:
        if car.id == id:
            cars.remove(car)
    return cars

