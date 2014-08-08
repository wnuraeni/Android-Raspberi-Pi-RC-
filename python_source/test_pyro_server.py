import Pyro.core
from cgi import parse_qs

def application(environ, start_response):

    # Connect to Pyro
    movement = Pyro.core.getProxyForURI("PYRONAME://robotmovement")

    parameters = parse_qs(environ['QUERY_STRING'])

    if 'seconds' in parameters and 'direction' in parameters:
  	direction = parameters['direction'][0]
        seconds = int(parameters['seconds'][0])

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(status)))]
    start_response(status, response_headers)
    return [status]


