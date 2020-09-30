# Client-Server using Laptop(s) and ESP's

Just a practical, hardware touch to Client-Server topology.
Developed basic client-server scripts using python socket module on localhost
and then improvised the code to be compatible with Micropython firmware running on ESP's.

Any device capable of processing python may run the server script and be the server.
ESP clients can only accept commands and give feedback.

The controlling machine runs the client script, connects to server and commands the ESP's
to do an already implemented simple functionality within code to control a 3 X 3
LED Matrix. 

Each ESP controls a row to 3 LED's. LED's can be turned on or off completely
independent of each other.

This system is just a demonstration to show client-server communication out
of the localhost environment and is designed to be a part of a bigger project. 

<img src ="https://github.com/hackme199/Client-Server-using-laptop-and-esp-s/blob/master/ESPClientServerComm(2).png">
