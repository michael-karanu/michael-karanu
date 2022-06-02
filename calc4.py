from tkinter import *
root = Tk()
e1 = Entry(root,width=50,bg="white",fg="black")
e1.pack()
e1.insert(0,"enter first number ")
e2 = Entry(root,width=50,bg = 'white',fg='black')
e2.pack()
e2.insert(0,"eneter second number")
def myclick():
    f_no = float(e1.get())
    s_no = float(e2.get())
    add = f_no + s_no
    sub = f_no - s_no
    divis = f_no / s_no
    mult = f_no * s_no    
    ANS = "Add :" + str(add) + "\n Sub :" + str(sub) + "\nDivis :" + str(divis) + "\nMult :" + str(mult)
    my_label = Label(root,text =ANS)
    my_label.pack()
my_button = Button(root,text="answer",command=myclick,bg = "white",fg = "black")
my_button.pack()    
root.mainloop()     

