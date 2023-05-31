import socket

s = socket.socket()
host = '10.10.1.1'
port = 60000

s.connect((host, port))
s.send("Hello server!".encode())

with open ('received_file', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        f.write(data)

f.close()
print('successfully get the file')
s.close()
print('connection closed')
