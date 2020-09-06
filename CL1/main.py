#!/usr/bin/python3
from machine import Signal, Pin
import socket,time

led1 = Signal(0,Pin.OUT,invert=False)
led2 = Signal(4,Pin.OUT,invert=False)
led3 = Signal(5,Pin.OUT,invert=False)
led4 = Signal(14,Pin.OUT,invert=False)
led5 = Signal(12,Pin.OUT,invert=False)
led6 = Signal(13,Pin.OUT,invert=False)


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.4.1",80))

while 1:
    time.sleep(1)
    try:
        msg = s.recv(10).decode("utf-8")
        # print(msg)
        if msg =='led1on':
            led1.value(1)
            message = 'led1 on'
            s.send(message.encode('utf-8'))
            print('led1 on')
        if msg =='led1off':
            led1.value(0)
            message = 'led1 off'
            s.send(message.encode('utf-8'))
            print('led1 off')
        if msg =='led2on':
            led2.value(1)
            message = 'led2 on'
            s.send(message.encode('utf-8'))
            print('led2 on')
        if msg =='led2off':
            led2.value(0)
            message = 'led2 off'
            s.send(message.encode('utf-8'))
            print('led2 off')
        if msg =='led3on':
            led3.value(1)
            message = 'led3 on'
            s.send(message.encode('utf-8'))
            print('led3 on')
        if msg =='led3off':
            led3.value(0)
            message = 'led3 off'
            s.send(message.encode('utf-8'))
            print('led3 off')
        if msg =='led4on':
            led4.value(1)
            message = 'led4 on'
            s.send(message.encode('utf-8'))
            print('led4 on')
        if msg =='led4off':
            led4.value(0)
            message = 'led4 off'
            s.send(message.encode('utf-8'))
            print('led4 off')
        if msg =='led5on':
            led5.value(1)
            message = 'led5 on'
            s.send(message.encode('utf-8'))
            print('led5 on')
        if msg =='led5off':
            led5.value(0)
            message = 'led5 off'
            s.send(message.encode('utf-8'))
            print('led5 off')
        if msg =='led6on':
            led6.value(1)
            message = 'led6 on'
            s.send(message.encode('utf-8'))
            print('led6 on')
        if msg =='led6off':
            led6.value(0)
            message = 'led6 off'
            s.send(message.encode('utf-8'))
            print('led6 off')
    except:
        pass



    

# while 1:
#     msg = s.recv(10)
#     if len(msg) <= 0:
#         break
#     full_msg += msg.decode("utf-8")

# print(full_msg)
