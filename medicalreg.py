from tkinter import *

states = []
state1 = []
def sympress(i):
    states[i] = not states[i]
def prevpress(i):
    state1[i] = not state1[i]
def tobacco(tstatus):
    tstatus = not tstatus

def alcohol(alstatus):
    alstatus = not alstatus
medreg = Tk()


lbl = Label(medreg, text="Namaste", fg="orange")
lbl.propagate(0)
lbl.place(x=400,y=0, anchor="n")
lbl.grid(row=1, column=1)

ogtreatlbl = Label(medreg, text='Any Ongoing treatments ?\n Please mention if any')
ogtreatlbl.grid()
ogtreat = Entry(medreg, width='50')
ogtreat.grid(row =2, column=1)

pulselbl = Label(medreg, text='Pulse ?')
pulselbl.grid()
pulse = Entry(medreg, width='50')
pulse.grid(row =3, column=1)

bplbl = Label(medreg, text='Blood Pressure ?')
bplbl.grid()
bp = Entry(medreg, width='50')
bp.grid(row =2, column=1)


sinjurylbl = Label(medreg, text='Any Serious injuries in the past :')
sinjurylbl.grid()
sinjury = Entry(medreg, width='50')
sinjury.grid(row =2, column=1)





bgplbl = Label(medreg, text='Blood Group :')
bgplbl.grid()
bgp = Entry(medreg, width='50')
bgp.grid(row =2, column=1)

inheritlbl = Label(medreg, text='Any Inherited chronic diseases ?')
inheritlbl.grid()



symptoms = Label(medreg, text='Visible Symptoms :')
symptoms.grid()










symp = ['Chest Pain','Respiratory Problems', 'Cardio Problems', 'Cardiovascular problems',
        'Haematological problems', 'Lymphatic ', 'Neurological Problems', 'Psychiatric Issues',
        'GastroIntestinal issues', 'Weight Gain', 'Weight loss', 'Musculoskeletal', 'Geniturinary']
sym = ['Asthama', 'Cancer', 'Cardiovascular Problems', 'Diabetes', 'Hypertension', 'Psychiatric Disorders', 'Epilepsy']
for i in range(len(sym)):
    chk = Checkbutton(medreg, text=sym[i], command=(lambda i=i: sympress(i)) )
    chk.grid(row=i+4, column=0, sticky='W')
    states.append(0)
for i in range(len(symp)):
    chk = Checkbutton(medreg, text = symp[i], command = (lambda i=i: prevpress(i)))
    chk.grid(row=i+4, column=2, sticky='W')
    state1.append(0)


print (states)
print (state1)







medreg.mainloop()

print (states)
print (state1)
