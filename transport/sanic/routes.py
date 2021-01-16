from configs.config import ApplicationConfig
from transport.sanic.endpoints.helth import health_endpoint


def get_routes(config: ApplicationConfig):
    return (
        (health_endpoint, '/', ['POST', 'GET']),
    )
