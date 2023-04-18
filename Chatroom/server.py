import socket
from threading import Thread

host = "127.0.0.1"
port = 8080
clients = {}
addresses = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))


def broadcast(msg, prefix=""):
    for x in clients:
        x.send(bytes(prefix, "utf8")+msg)


def handle_clients(conn, address):
    name = conn.recv(1024).decode()
    welcome = "Welcome " + name + ". You can type #quit if you ever want to leave the chat room."
    conn.recv(bytes(welcome, "utf8"))
    msg = name + " has recently joined the Chat room."
    broadcast(bytes(msg,"utf8"))
    clients[conn] = name

    while True:
        msg = conn.recv(1024)
        if msg != bytes("#quit", "utf8"):
            broadcast(msg, name + ":")
        else:
            conn.send(bytes("#quit", "utf8"))
            conn.close()
            del clients[conn]
            broadcast(bytes(name + " has left the chat room."))


def accept_clients_connection():
    while True:
        client_connection, client_address = sock.accept()
        print(client_address, " has connected.")
        client_connection.send("Welcome to the Chat room, Please type your name to continue".encode('utf8'))
        addresses[client_connection] = client_address

        Thread(target=handle_clients, args=(client_connection, client_address)).start()


if __name__ == "__main__":
    sock.listen(5)
    print("The Server is running and listening to clients requests.")

    t1 = Thread(target=accept_clients_connection)
    t1.start()
    t1.join()
