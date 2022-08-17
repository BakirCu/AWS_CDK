from dynamo_db_repozitory import DynamoDBRepository
from my_sql_reposiroty import MySqlRepository

db_type = "dynamodb" # that can be hardcoded for now

db_provider= None
if db_type == "dynamodb":
    db_provider = DynamoDBRepository("aws-movies-Users0A0EEA89-1ATR1DNGQLAXK")
elif db_type == "mysql":
    db_provider = MySqlRepository("some mysql credentials")
elif db_type == "mocked":
    pass
    
