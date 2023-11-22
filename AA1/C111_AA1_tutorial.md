Add a Clear Button
=================




In this activity, you will add a clear button and create a function to clear the text in the textbox.




<video src= "https://s3.amazonaws.com/media-p.slid.es/videos/1525749/E-mhPHB2/aa1.mp4" width = "480" height = "215"></video>


Follow the given steps to complete this activity.
	
1. Create a button widget


* Open the file `client.py`.


* Create a new button to clear the text.
~~~python
self.clear_button = Button(text = "Clear",
                                  font = "Helvetica 14 bold",
                                  bg = "#176B87",
                                  fg = "#ffffff"
~~~
2. Place the button
*  Place the button below the textbox on the window.
~~~python
self.clear_button.place(relx = 0.4, rely = 0.35)
~~~
* Define a method to reset the tetbox.
~~~python
def reset(self):
self.name_entry.delete(0,END)


~~~


* Add the given code to the Button widget to call the reset function when the button is clicked.
~~~python
self.clear_button = Button(.....
...
...,
command = lambda: self.reset()
~~~
* Save and run the code of the server and client to check the output.