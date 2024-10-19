import os
from pathlib import Path

from aws_cdk import App, CfnOutput, Duration, Environment, Stack
from aws_cdk.aws_lambda import (
    Architecture,
    DockerImageCode,
    DockerImageFunction,
    FunctionUrlAuthType,
)
from constructs import Construct


class GradioLambda(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create function
        lambda_fn = DockerImageFunction(
            self,
            "GradioApp",
            code=DockerImageCode.from_image_asset(str(Path.cwd()), file="Dockerfile"),
            architecture=Architecture.X86_64,
            memory_size=8192,
            timeout=Duration.minutes(2),
        )
        # add HTTPS url
        fn_url = lambda_fn.add_function_url(auth_type=FunctionUrlAuthType.NONE)
        CfnOutput(self, "functionUrl", value=fn_url.url)


app = App()
environment = Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"]
)
rust_lambda = GradioLambda(app, "GradioLambda", env=environment)

app.synth()