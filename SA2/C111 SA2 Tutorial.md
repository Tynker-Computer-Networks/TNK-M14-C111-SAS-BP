Connect to the Chatroom
======================




In this activity, you will learn to connect to the chatroom.




<video src= "https://s3.amazonaws.com/media-p.slid.es/videos/1525749/oy8UJO31/sa3.mp4" width = "480" height = "215"></video>


Follow the given steps to complete this activity:


1. Connect to the server.


* Open the file `client.py`.


* Connect to the server by uncommenting the code to connect the client to the server.
~~~python
client.connect((ip_address, port))
print("Connected with the server...")
~~~
* Check if the connection to the server is successful or not by uncommenting the receive method.
~~~python
class GUI(Tk):
...
...
...
 def receive(self):
   while True:
     try:
       message =
        client.recv(2048).decode('utf-8')
       print(message)
     except Exception as e:
       print("An error occurred!", e)
       client.close()
       break
~~~


2. Login to the chatroom.


* Create a method to login to the chatroom.
~~~python
def login(self, name):
   self.name = name
~~~
* Uncomment the given piece of code and place it inside the login method.
~~~python
   
   receive_thread = Thread(target=self.receive)
   receive_thread.start()
~~~
* Login to the chatroom by calling the login method when the button is clicked.
~~~python
self.login_button = Button(
.......
.......
  ,command = lambda: self.login(self.name_entry.get()))
~~~


3. Display the chat.
* Display the message by uncommenting the code to write the messages on the screen.
~~~python
def write():
    while True:
        message = '{}: {}'.format("nickname", input(''))
        client.send(message.encode('utf-8'))
write_thread = Thread(target=write)
write_thread.start()
~~~
* Save and run the code to check the output.
