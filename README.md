# c2

A C2 (Command and control) server uses the Client-Server method with an external c2 server in the cloud that the local client on my computer will reach out to receive commands. The client beacons out to the server at a set interval and the c2 server can decide when to respond to the beacons and can respond by sending commands or telling the client to stop beaconing. Commands will be to DDOS a test website, exfiltrate a file on the system, and encrypt a file on the system. TCP will be used for this traffic and the client/server programs will be written in Python. 

9/18: Complete research
9/24: Complete implementation for the basic functionality for both the client and server programs, test to make sure basic functionality works.
9/28: Complete advanced functionality and final testing.
9/30: Complete documentation 
