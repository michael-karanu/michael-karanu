from tkinter import *
root = Tk()
e = Entry(root,width=50,bg="#00FFFF",fg="black")
e.pack()
e.insert(0,"enter your name")
def myclick():
    Hello = "hello" + e.get()
    my_label = Label(root,text = Hello )
    my_label.pack()
my_button = Button(root,text = 'ENTER NAME',command = myclick,bg = 'purple',fg='yellow')
my_button.pack()
root.mainloop()     

