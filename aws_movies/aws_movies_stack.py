from inspect import Attribute
import os
from pyclbr import Function
from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_dynamodb as dynamodb
)


class AwsMoviesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        table = dynamodb.Table(self, "Users",
                               partition_key=dynamodb.Attribute(
                                   name="id", type=dynamodb.AttributeType.NUMBER)
                               # could not find schema definition?
                               )

        get_users_lambda = _lambda.Function(self, "GetAll",
                                            runtime=_lambda.Runtime.PYTHON_3_9,
                                            code=_lambda.Code.from_asset(
                                                os.path.dirname("lambda_services/")),
                                            handler="use_cases.users_use_case.get_list_record_lambda.lambda_handler",
                                            timeout=Duration.seconds(300),
                                            environment={
                                                "db_provider": "dynamodb",
                                                "table_name": "aws-movies-Users0A0EEA89-O054KIUS56WD"
                                                # how to get table name from table?
                                            },
                                            )

        create_user_lambda = _lambda.Function(self, "CreateUser",
                                              runtime=_lambda.Runtime.PYTHON_3_9,
                                              code=_lambda.Code.from_asset(
                                                  os.path.dirname("lambda_services/")),
                                              handler="use_cases.users_use_case.create_record_lambda.lambda_handler",
                                              timeout=Duration.seconds(300),
                                              environment={
                                                  "db_provider": "dynamodb",
                                                  "table_name": "aws-movies-Users0A0EEA89-O054KIUS56WD"
                                              },

                                              )

        get_user_by_id_lamda = _lambda.Function(self, "GetUser",
                                                runtime=_lambda.Runtime.PYTHON_3_9,
                                                code=_lambda.Code.from_asset(
                                                    os.path.dirname("lambda_services/")),
                                                handler="use_cases.users_use_case.get_single_record_lambda.lambda_handler",
                                                timeout=Duration.seconds(300),
                                                environment={
                                                    "db_provider": "dynamodb",
                                                    "table_name": "aws-movies-Users0A0EEA89-O054KIUS56WD"
                                                },
                                                )

        update_user_lambda = _lambda.Function(self, "UpdateUser",
                                              runtime=_lambda.Runtime.PYTHON_3_9,
                                              code=_lambda.Code.from_asset(
                                                  os.path.dirname("lambda_services/")),
                                              handler="use_cases.users_use_case.update_record_lambda.lambda_handler",
                                              timeout=Duration.seconds(300),
                                              environment={
                                                  "db_provider": "dynamodb",
                                                  "table_name": "aws-movies-Users0A0EEA89-O054KIUS56WD"
                                              },

                                              )

        delete_user_by_id_lambda = _lambda.Function(self, "DeleteUser",
                                                    runtime=_lambda.Runtime.PYTHON_3_9,
                                                    code=_lambda.Code.from_asset(
                                                        os.path.dirname("lambda_services/")),
                                                    handler="use_cases.users_use_case.delete_record_lambda.lambda_handler",
                                                    timeout=Duration.seconds(
                                                        300),
                                                    environment={
                                                        "db_provider": "dynamodb",
                                                        "table_name": "aws-movies-Users0A0EEA89-O054KIUS56WD"
                                                    },

                                                    )

        get_user_cars = _lambda.Function(self, "GetUserCars",
                                         runtime=_lambda.Runtime.PYTHON_3_9,
                                         code=_lambda.Code.from_asset(
                                             os.path.dirname("lambda_services/")),
                                         handler="use_cases.cars_use_case.get_list_of_cars_record.lambda_handler",
                                         timeout=Duration.seconds(300),
                                         environment={
                                             "db_provider": "dynamodb",
                                             "table_name": "aws-movies-Users0A0EEA89-O054KIUS56WD"
                                         },
                                         )

        create_user_cars = _lambda.Function(self, "CreateUserCars",
                                            runtime=_lambda.Runtime.PYTHON_3_9,
                                            code=_lambda.Code.from_asset(
                                                os.path.dirname("lambda_services/")),
                                            handler="use_cases.cars_use_case.create_cars_record_lambda.lambda_handler",
                                            timeout=Duration.seconds(300),
                                            environment={
                                                "db_provider": "dynamodb",
                                                "table_name": "aws-movies-Users0A0EEA89-O054KIUS56WD"
                                            },
                                            )

        get_user_car = _lambda.Function(self, "GetUserCar",
                                        runtime=_lambda.Runtime.PYTHON_3_9,
                                        code=_lambda.Code.from_asset(
                                            os.path.dirname("lambda_services/")),
                                        handler="use_cases.cars_use_case.get_single_car_record_lambda.lambda_handler",
                                        timeout=Duration.seconds(300),
                                        environment={
                                            "db_provider": "dynamodb",
                                            "table_name": "aws-movies-Users0A0EEA89-O054KIUS56WD"
                                        },
                                        )

        update_user_car = _lambda.Function(self, "UpdateUserCar",
                                           runtime=_lambda.Runtime.PYTHON_3_9,
                                           code=_lambda.Code.from_asset(
                                               os.path.dirname("lambda_services/")),
                                           handler="use_cases.cars_use_case.update_car_record_lambda.lambda_handler",
                                           timeout=Duration.seconds(300),
                                           environment={
                                               "db_provider": "dynamodb",
                                               "table_name": "aws-movies-Users0A0EEA89-O054KIUS56WD"
                                           },
                                           )


        delete_user_cars = _lambda.Function(self, "DeleteUserCars",
                                           runtime=_lambda.Runtime.PYTHON_3_9,
                                           code=_lambda.Code.from_asset(
                                               os.path.dirname("lambda_services/")),
                                           handler="use_cases.cars_use_case.delete_cars_record_lambda.lambda_handler",
                                           timeout=Duration.seconds(300),
                                           environment={
                                               "db_provider": "dynamodb",
                                               "table_name": "aws-movies-Users0A0EEA89-O054KIUS56WD"
                                           },
                                           )


        delete_user_car = _lambda.Function(self, "DeleteUserCar",
                                           runtime=_lambda.Runtime.PYTHON_3_9,
                                           code=_lambda.Code.from_asset(
                                               os.path.dirname("lambda_services/")),
                                           handler="use_cases.cars_use_case.delete_car_record_lambda.lambda_handler",
                                           timeout=Duration.seconds(300),
                                           environment={
                                               "db_provider": "dynamodb",
                                               "table_name": "aws-movies-Users0A0EEA89-O054KIUS56WD"
                                           },
                                           )


        table.grant_full_access(get_user_by_id_lamda)
        table.grant_write_data(create_user_lambda)
        table.grant_read_data(get_users_lambda)
        table.grant_full_access(update_user_lambda)
        table.grant_full_access(delete_user_by_id_lambda)
        table.grant_full_access(get_user_cars)
        table.grant_full_access(create_user_cars)
        table.grant_full_access(get_user_car)
        table.grant_full_access(update_user_car)
        table.grant_full_access(delete_user_cars)
        table.grant_full_access(delete_user_car)

        api = apigateway.RestApi(
            self, 'Endpoint'
        )

        users = api.root.add_resource("users")
        users.add_method("GET", apigateway.LambdaIntegration(get_users_lambda))
        users.add_method("POST",
                         apigateway.LambdaIntegration(create_user_lambda))

        user = users.add_resource("{user_id}")
        user.add_method("GET",
                        apigateway.LambdaIntegration(get_user_by_id_lamda))
        user.add_method(
                        "PUT",
                        apigateway.LambdaIntegration(update_user_lambda))
        user.add_method("DELETE",
                        apigateway.LambdaIntegration(delete_user_by_id_lambda))

        cars = user.add_resource("cars")
        cars.add_method("GET", apigateway.LambdaIntegration(get_user_cars))
        cars.add_method("POST", apigateway.LambdaIntegration(create_user_cars))
        cars.add_method("PUT", apigateway.LambdaIntegration(create_user_cars))  # create update are same
        cars.add_method("DELETE", apigateway.LambdaIntegration(delete_user_cars))

        car = cars.add_resource("{car_id}")
        car.add_method("GET", apigateway.LambdaIntegration(get_user_car))
        car.add_method("PUT", apigateway.LambdaIntegration(update_user_car))
        car.add_method("DELETE", apigateway.LambdaIntegration(delete_user_car))
