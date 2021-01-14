from transport.sanic.endpoints.helth import health_endpoint


def get_routes():
    return (
        (health_endpoint, '/', ['POST', 'GET']),
    )
