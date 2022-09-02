from data_access.base_reposotory.dynamo_db_repozitory import DynamoDBRepository
from data_access.base_reposotory.my_sql_reposiroty import MySqlRepository
from data_access.entity.user_entity import UserEntity
from data_access.entity.car_entity import CarEntity
from typing import List
import logging
import os
from exeption_handling.lambda_exceptions import BadRequestException


TABLE_NAME = os.environ["table_name"]

LOG = logging.getLogger()
LOG.setLevel(logging.INFO)


class UserDynamoDbReposytory(DynamoDBRepository):

    def __init__(self) -> None:
        DynamoDBRepository.__init__(self, TABLE_NAME)

    def get_all(self) -> List[UserEntity]:
        data_db = self.table.scan()
        users_db = data_db.get("Items")
        users = []
        for user in users_db:
            id = user.get("id")
            username = user.get("username")
            password = user.get("password")
            country = user.get("country")
            cars = user.get("cars")
            cars = user.get("cars")
            cars_entites = []
            if cars:
                for car in cars:
                    car_id = car.get("id")
                    car_type = car.get("type")
                cars_entites.append(CarEntity(int(car_id), car_type))
            users.append(UserEntity(int(id), username,
                         password, country, cars_entites))
        return users

    def get_by_id(self, id: int) -> UserEntity:
        data_db = self.table.get_item(Key={"id": id})
        user = data_db.get("Item")
        if not user:
            raise BadRequestException("User does not exist in database")
        id = user.get("id")
        username = user.get("username")
        password = user.get("password")
        country = user.get("country")
        cars = user.get("cars")
        cars_entites = []
        if cars:
            for car in cars:
                car_id = car.get("id")
                car_type = car.get("type")
                cars_entites.append(CarEntity(int(car_id), car_type))
        return UserEntity(int(id), username, password, country, cars_entites)

    def create(self, record: UserEntity) -> None:
        self.table.put_item(Item=record.to_json())

    def delete_by_id(self, id: int) -> None:
        self.table.delete_item(Key={"id": id})

    def update(self, record: UserEntity) -> None:
        user= record.to_json()
        username = user.get("username"),
        password = user.get("password"),
        country = user.get("country")
        cars = user.get("cars")
        self.table.update_item(Key={'id': record.get_id()},
                                          UpdateExpression="set username=:u, password=:p, country=:co, cars=:ca",
                                          ExpressionAttributeValues={':u': username,
                                                                     ':p': password,
                                                                     ':co':country,
                                                                     ':ca':cars
                                                                     },
                                          ReturnValues="UPDATED_NEW"
                                          )



class UserMySqlReposytory(MySqlRepository):

    def get_all(self) -> List[UserEntity]:
        pass

    def get_by_id(self, id: int) -> UserEntity:
        pass

    def create(self, record: UserEntity) -> None:
        pass

    def delete_by_id(self, id: int) -> None:
        pass

    def update(self, record: UserEntity) -> None:
        pass