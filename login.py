import tkinter
import sqlite3
# con=sqlite3.connect("tkinterdb.db")
# con.execute("create table sample(usrname text,password text)")
win=tkinter.Tk()
win.title("login")
win.configure(bg="lime")
win.minsize(500,500)
win.maxsize(700,700)

def home():
    win2=tkinter.Tk()
    l1=tkinter.Label(win2,text="home page",bg="tan",fg="black")
    l1.place(x=200,y=40)
    bt1=tkinter.Button(win2,text="logout",command=win2.quit)
    bt1.place(x=200,y=70)
    win2.mainloop()




def login():
    con=sqlite3.connect("tkinterdb.db")
    data=con.execute("select * from sample")
    f=0
    for i in data:
        if i[0]==e1.get() and i[1]==e2.get():
            f=1
            home()
    if f==0:
        l6.config(text="invalid username or password")        

def reg():
    win1=tkinter.Tk()
    win1.configure(bg="coral")
    win1.minsize(500,500)
    win1.maxsize(700,700)

    def regst():
        con=sqlite3.connect("tkinterdb.db")
        con.execute("insert into sample(usrname,password)values(?,?)",(e3.get(),e4.get()))
        con.commit()
        win1.destroy()

    l4=tkinter.Label(win1,text="REGISTER",bg="tan",fg='black')
    l4.place(x=190,y=20)

    l5=tkinter.Label(win1,text="name")
    l5.place(x=150,y=70)


    e3=tkinter.Entry(win1)
    e3.place(x=220,y=70)

    l3=tkinter.Label(win1,text="password")
    l3.place(x=150,y=100)
    e4=tkinter.Entry(win1)
    e4.place(x=220,y=100)

    bt3=tkinter.Button(win1,text="Submit",bg="light blue",activebackground="grey",activeforeground="white",command=regst)
    bt3.place(x=170,y=180)

    win1.mainloop()



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

bt1=tkinter.Button(win,text="login",bg="light blue",activebackground="grey",activeforeground="white",command=login)
bt1.place(x=170,y=140)

bt2=tkinter.Button(win,text="Register",bg="light blue",activebackground="grey",activeforeground="white",command=reg)
bt2.place(x=170,y=180)

l6=tkinter.Label(win)
l6.place(x=220,y=220)

win.mainloop()

