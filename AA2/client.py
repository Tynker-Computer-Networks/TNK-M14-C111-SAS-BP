import socket
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))
print("Connected with the server...")

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.resizable(width=False, height=False)
        self.configure(width=400, height=300, bg='#DAFFFB')
        # Remove page_label
        self.page_label = Label( text = "Please login to continue",
                                font = "Helvetica 14 bold", bg='#DAFFFB')
        self.page_label.place(relx = 0.2, rely = 0.07)
        
        # Change height, width and position of the elements to get desired layout
        self.name_entry = Entry(font = "Helvetica 14",
							bg = "#b1e5e2",
							fg = "#222222")
        self.name_entry.place(relwidth = 0.4,
                            relheight = 0.12,
                            relx = 0.35,
                            rely = 0.2)
        self.name_entry.focus()

        self.name_label = Label( text = "Name:",
                                font = "Helvetica 12", bg='#DAFFFB')
        self.name_label.place(relx = 0.1, rely = 0.2)

        self.clear_button = Button(text = "Clear",
                                  font = "Helvetica 14 bold",
                                  bg = "#176B87",
                                  fg = "#ffffff",
                                  command = lambda: self.reset()
                                  )
        
        self.clear_button.place(relx = 0.4, rely = 0.35)

        self.login_button = Button(text = "Login",
                                  font = "Helvetica 14 bold",
                                  bg = "#176B87",
                                  fg = "#ffffff",
                                  command = lambda: self.login(self.name_entry.get())
                                  )
        self.login_button.place(relx = 0.4, rely = 0.55)

    def reset(self):
        self.name_entry.delete(0,END)

    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                print(message)
            except Exception as e:
                print("An error occurred!", e)
                client.close()
                break
        
    def login(self, name):
        self.name = name
        receive_thread = Thread(target=self.receive)
        receive_thread.start()

def write():
    while True:
        message = '{}: {}'.format("nickname", input(''))
        client.send(message.encode('utf-8'))

write_thread = Thread(target=write)
write_thread.start()


app = GUI()
app.mainloop()