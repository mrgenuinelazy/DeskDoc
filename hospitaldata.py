class patient():
    def __init__(self):
        self.name = ""
        self.name = input("Enter your Name : ")
        self.gender = input("Gender : ")
        self.age = input("Enter Age")
        self.contact = input("Enter Contact number :")
        self.marital = input("Married ?")
        self.treatment = ''
        self.pulse = input("Enter pulse")
        self.bp = input("BP : ?")
        self.injury = True
        self.serious = input("NAme any serious injuries in the past")
        self.group = input("Enter Blood group :")
        self.chronic = input("Any inherited chronic diseases ?")
        self.chest_pain = False
        self.respiratory = True
        self.cardiac_disease = True
        self.cardiovascular = True
        self.hematological = True
        self.lymphatic = True
        self.neurological = True
        self.psychiatric = True
        self.gastro = True
        self.gain = True
        self.loss = True
        self.medication = True
        self.allergic = True
        self.tobacco = True
        self.recreational = True
        self.alcohol = True
        self.lastalcohol = ("When was the last time you consumed alcohol :")

    def details(self):

        self.name = input ("Enter your Name : ")
        self.gender = input("Gender : ")
        self.age = input("Enter Age")
        self.contact = input("Enter Contact number :")
        self.marital = input("Married ?")

    def medical(self):
        self.treatment = ''
        self.pulse = input("Enter pulse")
        self.bp = input("BP : ?")
        self.injury = True
        self.serious = input("NAme any serious injuries in the past")
        self.group = input("Enter Blood group :")
        self.chronic = input("Any inherited chronic diseases ?")

    def symptom(self):
        self.chest_pain = False
        self.respiratory  = True
        self.cardiac_disease  = True
        self.cardiovascular  = True
        self.hematological  = True
        self.lymphatic  = True
        self.neurological  = True
        self.psychiatric  = True
        self.gastro  = True
        self.gain  = True
        self.loss  = True
        self.medication  = True
        self.allergic  = True
        self.tobacco  = True
        self.recreational  = True
        self.alcohol  = True
        self.lastalcohol = ("When was the last time you consumed alcohol :")
