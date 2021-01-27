from typing import Tuple

from configs.config import ApplicationConfig
from context import Context
from transport.sanic import endpoints


def get_routes(config: ApplicationConfig, context: Context) -> Tuple:
    return (
        endpoints.HealthEndpoint(config=config, context=context, uri='/', methods=['GET', 'POST']),
        endpoints.CreateEmployeeEndpoint(config=config, context=context, uri='/employee', methods=['POST']),
        endpoints.AuthEmployeeEndpoint(config, context, uri='/employee/auth', methods=['POST'])
    )
