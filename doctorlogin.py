from tkinter import *
dlogin = Tk()
dlogin.title("DeskDoc App : Doctors Login")
lbl4 = Label(dlogin, text="Doctors Sign in Here", fg="orange")
lbl4.propagate(0)
lbl4.place(x=50,y=0, anchor="n")
lbl4.grid(row=0, column=1)

# Add a grid
mainframe = Frame(dlogin)
mainframe.grid(column=1, row=2, sticky=(N, W, E, S))


# Create a Tkinter variable
tkvar = StringVar(dlogin)

# Dictionary with options
choices = {'Select specialisation', 'Cardiologist', 'Dermatologist', 'Medicine_Specialist',
           'Nephrologist', 'Neurologist', 'Obs. & Gyne.', 'Opthamalogist', 'Orthopaedician',
           'Pediatrician', 'Psychiatrist'}
tkvar.set('Select specialisation')  # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Department").grid(row=1, column=1)
popupMenu.grid(row=2, column=1)


# on change dropdown value
def change_dropdown(*args):
    print(tkvar.get())


# link function to change dropdown
tkvar.trace('w', change_dropdown)


em0lbl = Label(dlogin, text="Email : ")
em0lbl.grid(row=3, column=0)
em0 = Entry(dlogin, width = 50)
em0.grid(row=3, column=1)


pwd0lbl = Label(dlogin, text="Password : ")
pwd0lbl.grid(row=4, column=0)
pwd0 = Entry(dlogin, width = 50)
pwd0.grid(row=4, column=1)



docpage = Button(dlogin, text="proceed", command=gotodocpage)
docpage.grid(row=5,column=1)

dlogin.mainloop()
