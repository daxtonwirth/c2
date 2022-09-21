import socketserver  

class MyTCPHandler(socketserver.BaseRequestHandler):
    """ 
    """

    def handle(self):
        self.data = self.request.recv(2048).strip()
        print("Received connection from {}:{}".format(self.client_address[0], self.data))

        command = input("Enter command: ")
        # if command = reverse shell, but this may be noisy
        # if command = exfil data then data.write(name)
        self.request.sendall(bytes(command, "utf-8"))
        self.data = self.request.recv(2048).strip()
        print(self.data)

    def menu():
        print("Type exit to stop beacon")

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()