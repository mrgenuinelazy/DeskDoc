from tkinter import *
bottom = Tk()
bottom.title("DeskDoc App : New user Sign in")
lbl4 = Label(bottom, text="New Patients Sign in Here", fg="orange")
lbl4.propagate(0)
lbl4.place(x=400,y=0, anchor="n")
lbl4.grid(row=0, column=1)


namelbl = Label(bottom, text="Name : ")
namelbl.grid(row=1, column=0)
name = Entry(bottom, width = 50)
name.grid(row=1, column=1)


genderlbl = Label(bottom, text="Gender : ")
genderlbl.grid(row=2, column=0)
gender = Entry(bottom, width = 50)
gender.grid(row=2, column=1)


contactlbl = Label(bottom, text="Mobile Number : ")
contactlbl.grid(row=3, column=0)
contact = Entry(bottom, width = 50)
contact.grid(row=3, column=1)


emlbl = Label(bottom, text="Email :")
emlbl.grid(row=4, column=0)
em = Entry(bottom, width = 50)
em.grid(row=4, column=1)


pwdlbl = Label(bottom, text="Password :")

pwdlbl.grid(column=0, row=5)

pwd = Entry(bottom, width=10)

pwd.grid(column=1, row=5)


repwdlbl = Label(bottom, text="Re- Enter Password :")

repwdlbl.grid(column=0, row=6)

repwd = Entry(bottom, width=10)

repwd.grid(column=1, row=6)

btn = Button(bottom, text="Proceed")

btn.grid(column=2, row=6)
bottom.mainloop()
