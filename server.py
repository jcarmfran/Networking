import socket
import sys

# connect to computers
def create_socket():
    #defining global variables
    try:
        global host
        global port
        global sock
        host = ''
        port = 9999
        sock = socket.socket()
    except socket.error as msg:
        print('Socket creation error: ' + str(msg))

# binding sockets and listening
def bind_socket():
    try:
        global host
        global port
        global sock
        
        print('Binding port...' + str(port))
        #binding host to port as tuple
        sock.bind((host,port))
        #listening for connection
        sock.listen(5)
    
    except socket.error as msg:
        print('Socket binding error' + str(msg) + '\n' + 'Retrying bind...')
        bind_socket()
        
#establish connection with client if socket is listening
def socket_accept():
    #conn: connection object
    #addr: list storing ip address and port
    conn,addr = sock.accept()
    print('Connection established. \nIP: ' + address[0] + '\nPort: ' + str(addr[1]))
    send_commands(conn)
    conn.close()

# send command to client
def send_commands(conn):
    while True: # infinite loop in order to send as many commands as necessary
        cmd = imput()
        if cmd == 'quit':
            conn.close() # close connection
            s.close() # close socket
            sys.exit() # close command prompt
        if len(str.encode(cmd)) > 0: # encoding in byte format
            conn.send(str.encode(cmd))
            # storing output
            client_response = str(connec.recv(1024, 'utf-8')) # converting to string format
            print(client_response, end="") # print and next line

# function that calls on other functions
def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
                                  