from tkinter import *
root = Tk()
def myclick():
    my_label = Label(root,text = "hey you clicked")
    my_label.pack()
my_button = Button(root,text = 'click me',command = myclick,bg = 'purple',fg='yellow')
my_button.pack()
root.mainloop()     






root = Tk()
# create a frame
my_label = Label(root,text="hello world")
my_label.pack()
# shows it on screen
root.mainloop()
