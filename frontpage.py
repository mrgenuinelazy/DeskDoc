from tkinter import *
import pickle

class Pickling:
    def __init__(self):
        self.dataset = []


def new():
    inst = Pickling()
    return inst


def dump():
    datalist = [states, state1, tkvar1, tkvar, pulse, bp, sinjury, inherit, symptoms ]
    open('myfile.txt','w').close()
    filehandler = open('myfile.txt','w')
    filehandler.write(datalist)
    filehandler.close()
def gotoplogin():
    top.destroy()
    plogin = Tk()
    plogin.title("DeskDoc App : Patients Login")
    lbl4 = Label(plogin, text="Patients Sign in Here", fg="orange")
    lbl4.propagate(0)
    lbl4.place(x=50, y=0, anchor="n")
    lbl4.grid(row=0, column=1)

    em1lbl = Label(plogin, text="Email : ")
    em1lbl.grid(row=3, column=0)
    em1 = Entry(plogin, width=50)
    em1.grid(row=3, column=1)

    pwd1lbl = Label(plogin, text="Password : ")
    pwd1lbl.grid(row=4, column=0)
    pwd1 = Entry(plogin, width=50)
    pwd1.grid(row=4, column=1)

    medregp = Button(plogin, text="proceed", command=gotomedicalreg)
    medregp.grid(row=5, column=1)

    plogin.mainloop()

def gotodlogin():
    top.destroy()
    dlogin = Tk()
    dlogin.title("DeskDoc App : Doctors Login")
    lbl4 = Label(dlogin, text="Doctors Sign in Here", fg="orange")
    lbl4.propagate(0)
    lbl4.place(x=50, y=0, anchor="n")
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
    em0 = Entry(dlogin, width=50)
    em0.grid(row=3, column=1)

    pwd0lbl = Label(dlogin, text="Password : ")
    pwd0lbl.grid(row=4, column=0)
    pwd0 = Entry(dlogin, width=50)
    pwd0.grid(row=4, column=1)

    docpage = Button(dlogin, text="proceed", command=dentry)
    docpage.grid(row=5, column=1)

    dlogin.mainloop()





def dentry():
    mid = Tk()
    mid.title("Deskdoc app : Doctors Portal")
    lbl3 = Label(mid, text="Doctors treat patients here", fg="orange")
    lbl3.propagate(0)
    lbl3.place(x=400, y=0, anchor="n")
    lbl3.grid(row=0, column=1)

    newfile = open('myfile.txt', 'rb')
    list2.readlines()







def gotonewuserpage():
    top.destroy()
    bottom = Tk()
    bottom.title("DeskDoc App : New user Sign in")
    lbl4 = Label(bottom, text="New Patients Sign in Here", fg="orange")
    lbl4.propagate(0)
    lbl4.place(x=400, y=0, anchor="n")
    lbl4.grid(row=0, column=1)

    namelbl = Label(bottom, text="Name : ")
    namelbl.grid(row=1, column=0)
    name = Entry(bottom, width=50)
    name.grid(row=1, column=1)

    genderlbl = Label(bottom, text="Gender : ")
    genderlbl.grid(row=2, column=0)
    gender = Entry(bottom, width=50)
    gender.grid(row=2, column=1)

    contactlbl = Label(bottom, text="Mobile Number : ")
    contactlbl.grid(row=3, column=0)
    contact = Entry(bottom, width=50)
    contact.grid(row=3, column=1)

    emlbl = Label(bottom, text="Email :")
    emlbl.grid(row=4, column=0)
    em = Entry(bottom, width=50)
    em.grid(row=4, column=1)

    pwdlbl = Label(bottom, text="Password :")

    pwdlbl.grid(column=0, row=5)

    pwd = Entry(bottom, width=10)

    pwd.grid(column=1, row=5)

    repwdlbl = Label(bottom, text="Re- Enter Password :")

    repwdlbl.grid(column=0, row=6)

    repwd = Entry(bottom, width=10)

    repwd.grid(column=1, row=6)

    btn = Button(bottom, text="Proceed", command=bottom.destroy)

    btn.grid(column=2, row=6)
    bottom.mainloop()


def gotomedicalreg():
    global states
    global state1, tkvar1, tkvar, pulse, bp, sinjury, inherit, symptoms
    states,state1 = [],[]

    def sympress(i):
        states[i] = not states[i]

    def prevpress(i):
        state1[i] = not state1[i]



    medreg = Tk()

    lbl = Label(medreg, text="Namaste", fg="orange")
    lbl.propagate(0)
    lbl.place(x=400, y=0, anchor="n")
    lbl.grid(row=1, column=1)

    ogtreatlbl = Label(medreg, text='Any Ongoing treatments ?\n Please mention if any')
    ogtreatlbl.grid()
    ogtreat = Entry(medreg, width='50')
    ogtreat.grid(row=2, column=1)

    # Add a grid
    mainframe = Frame(medreg)
    mainframe.grid(column=2, row=2, sticky=(N, W, E, S))

    # Create a Tkinter variable
    tkvar1 = StringVar(medreg)

    # Dictionary with options
    choices1 = {'Serious', 'Critical', 'Acute', 'Chronic'}
    tkvar1.set('Select severity')  # set the default option

    popupMenu1 = OptionMenu(mainframe, tkvar1, *choices1)
    Label(mainframe, text="Department").grid(row=1, column=1)
    popupMenu1.grid(row=2, column=1)

    # on change dropdown value
    def change_dropdown1(*args):
        print(tkvar.get())

    # link function to change dropdown
    tkvar1.trace('w', change_dropdown1)

    pulselbl = Label(medreg, text='Pulse ?')
    pulselbl.grid()
    pulse = Entry(medreg, width='50')
    pulse.grid(row=3, column=1)

    bplbl = Label(medreg, text='Blood Pressure ?')
    bplbl.grid()
    bp = Entry(medreg, width='50')
    bp.grid(row=4, column=1)

    sinjurylbl = Label(medreg, text='Any Serious injuries in the past :')
    sinjurylbl.grid()
    sinjury = Entry(medreg, width='50')
    sinjury.grid(row=5, column=1)

    bgplbl = Label(medreg, text='Blood Group :')
    bgplbl.grid()
    bgp = Entry(medreg, width='50')
    bgp.grid(row=6, column=1)

    inheritlbl = Label(medreg, text='Any Inherited chronic diseases ?')
    inheritlbl.grid()
    inherit = Entry(medreg, width='50')
    inherit.grid(row=7, column=1)

    symptoms = Label(medreg, text='Visible Symptoms :')
    symptoms.grid()
    symptoms = Entry(medreg, width='50')
    symptoms.grid(row=8, column=1)

    symp = ['Chest Pain', 'Respiratory Problems', 'Cardio Problems', 'Cardiovascular problems',
            'Haematological problems', 'Lymphatic ', 'Neurological Problems', 'Psychiatric Issues',
            'GastroIntestinal issues', 'Weight Gain', 'Weight loss', 'Musculoskeletal', 'Geniturinary']
    sym = ['Asthama', 'Cancer', 'Cardiovascular Problems', 'Diabetes', 'Hypertension', 'Psychiatric Disorders',
           'Epilepsy']
    for i in range(len(sym)):
        chk = Checkbutton(medreg, text=sym[i], command=(lambda i=i: sympress(i)))
        chk.grid(row=i + 9, column=0, sticky='W')
        states.append(0)
    for i in range(len(symp)):
        chk = Checkbutton(medreg, text=symp[i], command=(lambda i=i: prevpress(i)))
        chk.grid(row=i + 10, column=2, sticky='W')
        state1.append(0)

    # Add a grid
    mainframe = Frame(medreg)
    mainframe.grid(column=1, row=len(symp)+10, sticky=(N, W, E, S))

    # Create a Tkinter variable
    tkvar = StringVar(medreg)

    # Dictionary with options
    choices = {'Select specialisation', 'Cardiologist', 'Dermatologist', 'Medicine_Specialist',
               'Nephrologist', 'Neurologist', 'Obs. & Gyne.', 'Opthamalogist', 'Orthopaedician',
               'Pediatrician', 'Psychiatrist'}
    tkvar.set('Select specialisation')  # set the default option

    popupMenu = OptionMenu(mainframe, tkvar, *choices)
    Label(mainframe, text="Department").grid(row=1, column=1)
    popupMenu.grid(row=2, column=2)

    # on change dropdown value
    def change_dropdown(*args):
        print(tkvar.get())

    # link function to change dropdown
    tkvar.trace('w', change_dropdown)

    print(states)
    print(state1)

    by = Button(medreg, text = 'Save', command=dump)
    by.grid(row=2, column=len(state1)+11 )

    medreg.mainloop()




top = Tk()
top.title("DeskDoc App")
lbl = Label(top, text="Welcome to the DeskDoc app", fg="orange")
lbl.propagate(0)
lbl.place(x=400,y=0, anchor="n")
lbl.grid(row=0, column=0)

b1 = Button(top,text="Patients Login", width="50", command = gotoplogin )
b2 = Button(top,text="Doctors Login ", width="50", command= gotodlogin)
b3 = Button(top,text="New User ? Sign in here ", width="50", command=gotonewuserpage)
b4 = Button(top,text="Know your doctor's Schedule", width="50")
b1.grid(row=2, column=0)
b2.grid(row=4, column=0)
b3.grid(row=6, column=0)
b4.grid(row=8, column=0)


top.mainloop()
