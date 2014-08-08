import Pyro.core
from cgi import parse_qs

def application(environ, start_response):

    # Connect to Pyro
    movement = Pyro.core.getProxyForURI("PYRONAME://robotmovement")

    parameters = parse_qs(environ['QUERY_STRING'])

    #s = 0
	
    if 'seconds' in parameters and 'direction' in parameters:
        direction = parameters['direction'][0]
        seconds = int(parameters['seconds'][0])

        # Call the appropriate function
        if direction == 'Stop':
           movement.stop()
	elif direction == 'CamUp':
	     movement.camera_up(seconds)
 	elif direction == 'CamDown':
	     movement.camera_down(seconds)
	elif direction == 'CamLeft':
	     movement.camera_left(seconds)
	elif direction == 'CamRight':
             movement.camera_right(seconds)
        elif direction == 'Forwards':
             movement.forward(seconds)
        elif direction == 'Backwards':
             movement.backward(seconds)
        elif direction == 'Left':
             movement.left(seconds)
        elif direction == 'Right':
             movement.right(seconds)
	elif direction == 'Berhenti':
	     movement.berhenti(seconds)
	elif direction == 'CamCenter':
	     movement.camera_center(seconds)
	elif direction == 'Netral':
	     movement.netral(seconds)
     	elif direction == 'SonicOn':
	     movement.ultrasonic_start(0)
		
	elif direction == 'SonicOff':
	     movement.ultrasonic_stop(0);
        status = '200 OK'

    else:
        status = '400 Bad Request'
    
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(status)))]
    start_response(status, response_headers)
    return [status]
