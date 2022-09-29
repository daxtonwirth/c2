# Overview

The main reason I am writing this is to learn more about C2 servers, so I figured the best way to do this would be to create one! I also want to learn and understand TCP sockets with the libraries needed to do this which will help me in future projects. 

A C2 (Command and control) server uses the Client-Server method having an external c2 server in the cloud that the infected client reaches out to receive commands. The client beacons out to the server at a set interval and the c2 server can decide when to respond to the beacons and can respond by sending commands or telling the client to stop beaconing. 

The commands for this c2 software will run a desired command and receive the output, extract a test file, change the beaconing interval of the client, encrypt a file, and DDOS a test website. TCP will be used for this traffic and the client/server programs will be written in Python. The beaconing interval for this project is also set at random to similate real c2 behavior.

**Disclaimer**: This software is for test purposes only on authorized hosts and is not warranted for malicious purposes. 

Here is my YouTube demonstration of the software and a walkthrough of the code. {It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) }

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

{Describe the architecture that you used (client/server or peer-to-peer)}

I used TCP for this project and allowed the user to choose which port numbers they want to use but have the default set at 443 which is commonly allowed through a firewall.

{Identify the format of messages being sent between the client and server or the messages sent between two peers.}

# Development Environment

## Requirements:
- cryptography

{Describe the tools that you used to develop the software}

{Describe the programming language that you used and any libraries.}

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Encrypt and Decrypt Files using Python](https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/)
* [Web Site Name](http://url.link.goes.here)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Ability to change encoding methods or use encryption all together
* Have traffic appear has http or dns
* Item 3
