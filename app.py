#!/usr/bin/env python3

import aws_cdk as cdk

from aws_movies.aws_movies_stack import AwsMoviesStack


app = cdk.App()
AwsMoviesStack(app, "aws-movies")

app.synth()
