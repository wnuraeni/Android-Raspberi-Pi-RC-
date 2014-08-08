import Pyro.core
#from UltraSonic import UltraSonic
import time

#s = UltraSonic(0)
#time.sleep(1)
#s.stop()
#s.join()
#print "stop"
#time.sleep(1)
#del s 
#s = UltraSonic(0)
son = Pyro.core.getProxyForURI("PYRONAME://sonic")
son.start_sonic()
time.sleep(0.5)
son.stop_sonic()
print "stop"
time.sleep(3)
son.start_sonic()
print "start"
time.sleep(0.5)
son.stop_sonic()
print "stop"
