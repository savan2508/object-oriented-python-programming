import tkinter
import socket
from tkinter import *
from threading import Thread


def receive():
    while True:
        try:
            msg = sock.recv(1024).decode("utf8")
            msg_list.insert(tkinter.END, msg)

        except:
            print("There is an Error receiving the Message")


def send():
    msg = my_msg.get()
    my_msg.set("")
    sock.send(bytes(msg, "utf8"))
    if msg == "#quit":
        sock.close()
        window.close()


def on_closing():
    my_msg.set("#quit")
    send()


window = Tk()
window.title("Chat Room Application")
window.configure(background="green")

message_frame = Frame(window, height=100, width=100, background='red')
message_frame.pack()

my_msg = StringVar()
my_msg.set("")

scroll_bar = Scrollbar(message_frame)
msg_list = Listbox(message_frame, height=15, width=100, background="red", yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

label = Label(window, text="Enter the Message", fg='blue', font="Aerial", background="red")
label.pack()

entry_field = Entry(window, textvariable=my_msg, foreground="red", width=50)
entry_field.pack()

send_button = Button(window, text="Send", font="Aerial", foreground="white", command=send)
send_button.pack()

quit_button = Button(window, text="Quit", font="Aerial", foreground="white", command=on_closing)
quit_button.pack()

Host = "127.0.0.1"
Port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((Host, Port))

receive_thread = Thread(target=receive)
receive_thread.start()

mainloop()
