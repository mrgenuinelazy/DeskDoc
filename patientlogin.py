from tkinter import *
plogin = Tk()
plogin.title("DeskDoc App : Patients Login")
lbl4 = Label(plogin, text="Patients Sign in Here", fg="orange")
lbl4.propagate(0)
lbl4.place(x=50,y=0, anchor="n")
lbl4.grid(row=0, column=1)




em1lbl = Label(plogin, text="Email : ")
em1lbl.grid(row=3, column=0)
em1 = Entry(plogin, width = 50)
em1.grid(row=3, column=1)


pwd1lbl = Label(plogin, text="Password : ")
pwd1lbl.grid(row=4, column=0)
pwd1 = Entry(plogin, width = 50)
pwd1.grid(row=4, column=1)

medregp = Button(plogin, text="proceed", command=quit)
medregp.grid(row=5,column=1)


plogin.mainloop()
