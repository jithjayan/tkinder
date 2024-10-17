import tkinter

win=tkinter.Tk()
win.title("demo")
win.configure(bg="green")
win.minsize(500,500)
win.maxsize(700,700)

def save():
    # print(e1.get())
    l4.config(text=e1.get())


l1=tkinter.Label(win,text="welcome all",bg="green",fg='blue')
# l1.pack()
l1.place(x=200,y=20)
# l1.grid(row=0,column=0)

# l2=tkinter.Label(win,text="sample text")
# l2.grid(row=10,column=10)


l3=tkinter.Label(win,text="name")
l3.place(x=80,y=70)

e1=tkinter.Entry(win)
e1.place(x=170,y=70)

bt1=tkinter.Button(win,text="save",bg="light blue",activebackground="grey",activeforeground="white",command=save)
bt1.place(x=170,y=100)

l4=tkinter.Label(win)
l4.place(x=120,y=150)



win.mainloop()