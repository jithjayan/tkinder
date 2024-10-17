import tkinter
win=tkinter.Tk()
win.title("login")
win.configure(bg="lime")
win.minsize(500,500)
win.maxsize(700,700)

def reg():
    win=tkinter.Tk()
    win.minsize(500,500)
    win.maxsize(700,700)

    l4=tkinter.Label(win,text="REGISTER",bg="tan",fg='black')
    l4.place(x=190,y=20)

    l5=tkinter.Label(win,text="name")
    l5.place(x=150,y=70)


    e3=tkinter.Entry(win)
    e3.place(x=220,y=70)

    l3=tkinter.Label(win,text="password")
    l3.place(x=150,y=100)
    e2=tkinter.Entry(win)
    e2.place(x=220,y=100)
    
    win.mainloop()



l1=tkinter.Label(win,text="LOGIN",bg="tan",fg='black')
l1.place(x=190,y=20)

l2=tkinter.Label(win,text="name")
l2.place(x=150,y=70)


e1=tkinter.Entry(win)
e1.place(x=220,y=70)

l3=tkinter.Label(win,text="password")
l3.place(x=150,y=100)


e2=tkinter.Entry(win)
e2.place(x=220,y=100)

bt1=tkinter.Button(win,text="login",bg="light blue",activebackground="grey",activeforeground="white")
bt1.place(x=170,y=140)

bt2=tkinter.Button(win,text="Register",bg="light blue",activebackground="grey",activeforeground="white",command=reg)
bt2.place(x=170,y=180)


win.mainloop()

