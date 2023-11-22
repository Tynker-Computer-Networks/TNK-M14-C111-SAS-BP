Add Widgets to the Window
===========================


In this activity, you will learn to add widgets to the window.


<video src= "https://s3.amazonaws.com/media-p.slid.es/videos/1525749/pyl1Nk_c/sa2.mp4" width = "480" height = "215"></video>


Follow the given steps to complete this activity:


1. Create the Widget.


* Open the file `client.py`.


*  Create a label widget with the text “Name” in it.
~~~python
self.name_label = Label( text = "Name:",
  font = "Helvetica 12", 
  bg='#DAFFFB')
~~~
*  Create a button widget with the text “Login” in it.
~~~python
self.login_button = Button(text = "Login",
                           font = "Helvetica 14 bold",
                           bg = "#176B87",
                           fg = "#ffffff",)
~~~
2. Place the Widget
*  Place the label widget with the text “Name” on the window.
~~~python
self.name_label.place(relx = 0.1, rely = 0.2)
~~~
*  Place the button widget with the text “Login” on the window.
~~~python
self.login_button.place(relx = 0.4, rely = 0.55)
~~~


* Save and run the code to check the output.

