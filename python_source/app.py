import Pyro.core
from cgi import parse_qs
from UltraSonic import UltraSonic

def application(environ, start_response):

    # Connect to Pyro
    #ultra_sonic = UltraSonic(0)
    movement = Pyro.core.getProxyForURI("PYRONAME://robotmovement")

    parameters = parse_qs(environ['QUERY_STRING'])	

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
          elif direction == 'SonicOn':
		#movement.ultrasonic_start(0)
		s = UltraSonic(0);
		s.counter = True;
		s.start();
		status = 'call ultrasonic';
	  elif direction == 'SonicOff':
		#movement.ultrasonic_stop(0)
		e = UltraSonic(0);
		e.counter=False;
		e.start();
#          status = '200 OK'

    else:
          status = '400 Bad Request'
    
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(status)))]
    start_response(status, response_headers)
    return [status]
