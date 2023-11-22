Create the Application Window
============================


In this activity, you will learn to create an application window using the tkinter library.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10836783/pasted-from-clipboard.png" width = "300" height = "300">


Follow the given steps to complete this activity:


1. Create and initialize the Window


* Open the `client.py` file.


* Import the tkinter library.
~~~python
from tkinter import *
~~~
* Create a class and Inherit from Tk class.
~~~python
	class GUI(Tk):
	def __init__(self):
		super().__init__()
~~~
* Initialize the newly created class and call the Tk class initializer.
~~~python
	def __init__(self):
		super().__init__()
~~~


2. Handle user interactions
* Initialize an instance of the GUI class.
~~~python
app = GUI()
~~~


* Run the event loop to handle user interactions.
~~~python
app.mainloop()
~~~
* Comment the rest of the code.
~~~python
# nickname = input("Choose your nickname: ")


# client.connect((ip_address, port))
# print("Connected with the server...")


# def receive():
.......
.......
.......
~~~
* Save and run the code to check the output.


3. Set the features of the Window
* Set the title of the window.
~~~python
self.title(“Login”)
~~~
* Configure the window to be non-resizable.
~~~html
self.resizable(width=False, height=False)
~~~
* Set the width, height, and background of the window.
~~~html
self.configure(width=400, height=300, bg='#DAFFFB')
~~~       
* Save and run the code to check the output.