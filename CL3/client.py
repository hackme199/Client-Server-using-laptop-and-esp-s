import socket
import select
import errno
import sys
from machine import Signal,Pin

led1 = Signal(0,Pin.OUT,invert=False)
led2 = Signal(4,Pin.OUT,invert=False)
led3 = Signal(5,Pin.OUT,invert=False)
led1.value(0)
led2.value(0)
led3.value(0)

HEADER_LENGTH = 10

IP = "192.168.43.165"
PORT = 1234

def f(a,b):
    a = str(a)
    return a + (b-len(a))*' '


#my_username = input("Username: ")
my_username = 'node3'
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode("utf-8")
# username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
username_header = f(len(username),HEADER_LENGTH).encode('utf-8')
client_socket.send(username_header + username)

while 1:
    # message = input("{} > ".format(my_username))
    message = ''

    if message:
        message = message.encode("utf-8")
        # message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
        message_header = f(len(message),HEADER_LENGTH).encode('utf-8')
        client_socket.send(message_header + message)
    try:
        while 1:
            #recieve things
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("connection closed by the server")
                sys.exit()
            username_length = int(username_header.decode("utf-8").strip())
            username = client_socket.recv(username_length).decode("utf-8")

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode("utf-8").strip())
            message = str(client_socket.recv(message_length).decode("utf-8"))
            if message == '7on':
                led1.value(1)
                client_socket.send((f(14,10)+"led7 STATUS:ON").encode('utf-8'))
                print("{} > {}".format(username,message))
                continue
            if message == '7off':
                led1.value(0)
                client_socket.send((f(15,10)+"led7 STATUS:OFF").encode('utf-8'))
                print("{} > {}".format(username,message))
                continue
            if message == '8on':
                led2.value(1)
                client_socket.send((f(14,10)+"led8 STATUS:ON").encode('utf-8'))
                print("{} > {}".format(username,message))
                continue
            if message == '8off':
                led2.value(0)
                client_socket.send((f(15,10)+"led8 STATUS:OFF").encode('utf-8'))
                print("{} > {}".format(username,message))
                continue
            if message == '9on':
                led3.value(1)
                client_socket.send((f(14,10)+"led9 STATUS:ON").encode('utf-8'))
                print("{} > {}".format(username,message))
                continue
            if message == '9off':
                led3.value(0)
                client_socket.send((f(15,10)+"led9 STATUS:OFF").encode('utf-8'))
                print("{} > {}".format(username,message))
                continue

            print("{} > {}".format(username,message))

    # except IOError as e:
    #     if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
    #         print('Reading error',str(e))
    #         sys.exit()
    #     continue

    # except Exception as e:
    #     print('General error',str(e))
    #     sys.exit()

    except:
        continue
