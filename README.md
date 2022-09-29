# C2 Project Overview

The main reason I am writing this is to learn more about how C2 servers work on a fundamental level, so I figured the best way to do this would be to create one! I also want to learn and understand TCP sockets and the libraries needed to do this which will help me in future projects. 

A C2 (Command and control) server uses the Client-Server method having an external c2 server in the cloud that the infected client reaches out to receive commands. The client "beacons" out to the server at a certain interval and the c2 server can respond to the beacons by sending commands or telling the client to stop beaconing/change its beaconing interval. 

The server software has 6 options: run a command on the client and receive the output, extract a test file,  encrypt a test file, change the beaconing interval of the client, and DDOS a test website (continous ping). TCP will be used for this traffic and the client/server programs will be written in Python. The beaconing interval for this project is also set at random to simulate real c2 behavior.

**Disclaimer**: This software is for test purposes only on authorized hosts and is not warranted for malicious purposes. 

Here is my YouTube demonstration of the software and a walkthrough of the code:

[Software Demo Video](https://youtu.be/JveHtE4GKAc)

# Network Communication

I used the client-server model for this software. In order to test it, I had the two softwares communicate with each other over different ports but it can also be used to communicate between machines not on the same network.

I used TCP for this project and allowed the user to choose which port numbers they want to use but have the default set at 443 which is commonly allowed through a firewall.

I did not spend much time on the format of the traffic and just had it send the raw text between each other encoded in Base64.

## Development Environment

This project was written in Python3. I also used the following libraries: cryptography, socket, socketserver, time, os, random, base64

For the server, I based the code off of the socketserver library which makes it really easy to create the desired client-server model as it has a feature to continuously serve and buffer requests. To run the software, separate places are needed for the client and server software to run.


## Useful Websites I used for this project

* [Python Server Libraries](https://docs.python.org/3.6/library/socketserver.html)
* [Python Socket Libraries](https://docs.python.org/3.6/library/socket.html)
* [Encrypt and Decrypt Files using Python](https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/)

## Future Work

* Ability to change encoding methods or use encryption for all communication
* Make the traffic appear as http or dns to appear legitimate
* Allow the server to send commands to change directories
