import socket
import threading
#Client 2 
nickname = input("Choose Your Nickname : ")
host = "127.0.0.1"
port = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def receive():
    while True:
        try:
            #Receive Message From Server 
            # If "Nick " send Nickname 
            message = client.recv(1024).decode('ascii')
            if message == "NICK":
                client.send(nickname.encode('ascii'))
            else: 
                print(message)
        except:
            #Close Connection When Error
            print("An error occured!")
            client.close()
            break



def write():
    while True:
        message = f"{nickname}:{input('')}"
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target = write )
write_thread.start()