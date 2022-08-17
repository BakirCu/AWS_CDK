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
        partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.NUMBER)
        )

        my_lambda = _lambda.Function(
            self, 'Main',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='main.main',
               
        )
        get_users_lambda = _lambda.Function(self, "GetAll",
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset(os.path.dirname("lambda_services/use_cases/users_use_case/")),
            handler='get_list_record_lambda.get_all_lambda_handler',
            timeout= Duration.seconds(300),
            )
        
        create_user_lambda = _lambda.Function(self, "CreateUser",
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset(os.path.dirname("lambda_services/use_cases/users_use_case/")),
            handler='create_record_lambda.create_record_lambda_handler',
            timeout= Duration.seconds(300),
            )

        get_user_by_id_lamda = _lambda.Function(self, "GetUser",
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset(os.path.dirname("lambda_services/use_cases/users_use_case/")),
            handler='get_single_record_lambda.get_record_lambda_handler',
            timeout= Duration.seconds(300),
            )

        table.grant_full_access(get_user_by_id_lamda)
        table.grant_write_data(create_user_lambda)
        table.grant_read_data(get_users_lambda)

        api = apigateway.RestApi(
            self, 'Endpoint'
        )

        books = api.root.add_resource("users")
        books.add_method("GET",apigateway.LambdaIntegration(get_users_lambda))
        books.add_method("POST", apigateway.LambdaIntegration(create_user_lambda))

        book = books.add_resource("{user_id}")
        book.add_method("GET")
        book.add_method("DELETE")
        
