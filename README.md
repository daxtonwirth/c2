# c2

A C2 (Command and control) server uses the Client-Server method with an external c2 server in the cloud that the local client on my computer will reach out to receive commands. The client beacons out to the server at a set interval and the c2 server can decide when to respond to the beacons and can respond by sending commands or telling the client to stop beaconing. Commands will be to DDOS a test website, exfiltrate a file on the system, and encrypt a file on the system. TCP will be used for this traffic and the client/server programs will be written in Python. 

9/18: Complete research
9/24: Complete implementation for the basic functionality for both the client and server programs, test to make sure basic functionality works.
9/28: Complete advanced functionality and final testing.
9/30: Complete documentation 


# Overview

I want to learn more about C2 servers so I figured the best way to do this would be to create one! This will also help me to understand TCP sockets and the libraries needed to do this which will help me in future projects. 

{Provide a description the networking program that you wrote. Describe how to use your software.  If you did Client/Server, then you will need to describe how to start both.}

{Describe your purpose for writing this software.}

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

{Describe the architecture that you used (client/server or peer-to-peer)}

{Identify if you are using TCP or UDP and what port numbers are used.}

{Identify the format of messages being sent between the client and server or the messages sent between two peers.}

# Development Environment

{Describe the tools that you used to develop the software}

{Describe the programming language that you used and any libraries.}

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Web Site Name](http://url.link.goes.here)
* [Web Site Name](http://url.link.goes.here)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Item 1
* Item 2
* Item 3
