import time
import RPi.GPIO as GPIO
import Pyro.core
import Pyro.naming
from UltraSonic import UltraSonic

class Sonic(Pyro.core.ObjBase):

	def _setup(self):
		self.ultra_run = False

	def __init__(self):
		Pyro.core.ObjBase.__init__(self)
		self._setup()

	def start_sonic(self):
		self.s = UltraSonic(0)
		self.s.start_threaded()
		self.s.start()
	def stop_sonic(self):
		self.s.stop()
		self.s.join()
		self.s = UltraSonic(0)
		self.s.stop()
		del self.s

if __name__ == "__main__":
	Pyro.core.initServer()
	ns = Pyro.naming.NameServerLocator().getNS()
	daemon = Pyro.core.Daemon()
	daemon.useNameServer(ns)
	uri = daemon.connect(Sonic(),"sonic")
	daemon.requestLoop()
