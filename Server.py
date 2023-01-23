import socket
import threading


# Connection Data


host = "127.0.0.1"
port = 55555

#Starting the server 

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind((host, port))
server.listen()



# Litest for Client andtheir Nicknames 


clients = []
nicknames = []

# Sending Messages to All connected Clients 

def broadcast(message):
    for client in clients:
        client.send(message)
    


def handle(client):
    while True:
        try:
            #Broadcasting Messages 
            message = client.recv(1024)
            broadcast(message)
        except:
            #Removing and losing Clients 
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left !".encode('ascii'))
            nicknames.remove(nickname)
            break
    

#Receiving / Listening Function 
 
def receive():
    while True:
        #Accept Connection 
        client , address = server.accept()
        print(f"Connected with {str(address)}")

        #Request and store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)


        #Print and Broadcast Nickname
        print(f"Nick is {nickname} ")
        broadcast(f"{nickname} joined!".encode('ascii'))
        client.send('Connected to server ! ' .encode('ascii'))

        #StartHnadling Thread For client 
        thread = threading.Thread(target=handle , args=(client,))
        thread.start() 


print("Server listening ...... !")
receive()

