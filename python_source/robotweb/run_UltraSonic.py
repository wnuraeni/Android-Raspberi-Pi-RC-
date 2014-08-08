from UltraSonic import UltraSonic
import time

s = UltraSonic(0)
s.start_thread()
s.start()
time.sleep(1)
s.stop()
s.join()
print "stop"
time.sleep(1)
s = UltraSonic(0)
s.stop()
#u.start_thread()
#u.start()
