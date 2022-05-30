from tkinter import *
root = Tk()
# create a frame
my_label1 = Label(root,text="hello world")
my_label2 = Label(root,text="hello world")
my_label1.grid(row=2,column=10)
my_label2.grid(row=0,column=10)
# shows it on screen
root.mainloop()