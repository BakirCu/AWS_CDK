from data_access.base_reposotory.my_sql_reposiroty import MySqlRepository
from data_access.user_repositiry import UserDynamoDbReposytory, UserMySqlReposytory
import os


# db_type = os.environ["db_provider"] 
db_type = "mysql" 
db_provider= None
user_repository = None

if db_type == "dynamodb":
    user_repository = UserDynamoDbReposytory()
elif db_type == "mysql":
    user_repository = MySqlRepository("aws-users.ciotugvfgxcu.us-east-1.rds.amazonaws.com",
                                        "admin",
                                        "test12345",
                                        "UserCars")

elif db_type == "mocked":
    pass
    
