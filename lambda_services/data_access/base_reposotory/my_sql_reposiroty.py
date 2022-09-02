from data_access.base_reposotory.base_repository import BaseRepository
from data_access.entity.user_entity import UserEntity
from data_access.entity.car_entity import CarEntity
import pymysql

class MySqlRepository(BaseRepository):

    

    def __init__(self, endpoint, username, password, database_name) -> None:
        self.connection =  pymysql.connect(endpoint, username, password, database_name)
        self.cursor = self.connection.cursor()

    #this is not good, this is for UserMySqlRepository, just to show logic
    def get_all(self)-> List[UserEntity]:
        cursor = self.cursor
        query = '''
                SELECT User.id, User.username, 
                        User.password, User.country, 
                        group_concat(Car.id) as car_ids, 
                        group_concat(Car.type) as car_types 
                FROM UserCars.User
                INNER JOIN UserCar
                ON User.id = UserCar.user_id
                INNER JOIN  Car
                ON Car.id = UserCar.car_id
                GROUP BY User.id'''
        cursor.execute(query)
        rows = cursor.fetchall()

        users = []
        for row in rows:
            user_id = row[0]
            username = row[1]
            pasword = row[2]
            country = row[3]
            car_ids = row[4].split(',')
            car_types = row[5].split(',')

            if len(car_ids) != len(car_types):
                raise Exception

            cars_enteties = []
            for i in range(len(car_ids)):
                cars_enteties.append(CarEntity(car_ids[i], car_types[i]))
            users.append(UserEntity(user_id, username, pasword, country, cars_enteties))
        return users


    def get_by_id(self):
        pass


    def create(self):
        pass

    def delete_by_id(self):
        pass

    def update(self):
        pass