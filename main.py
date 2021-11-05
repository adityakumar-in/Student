# Work in Progress

from tkinter import *
from tkinter.ttk import * # For combobox

classNo = "Null"

class Submit:
    @staticmethod
    def infoSubmit():
        pass

class Delete:
    @staticmethod
    def deleteInfo():
        deleteInfos = Tk()
        deleteInfos.title(f"Delete Screen for {classNo}")
        deleteInfos.geometry('200x120')
        deleteInfos.resizable(0, 0)

        Label(deleteInfos, text="Enter Name", font="comicsansmc 15 bold").pack(pady=5)
        Entry(deleteInfos).pack(pady=5)
        Button(deleteInfos, text="Delete").pack(pady=8)

        deleteInfos.mainloop()

class Input:
    @staticmethod
    def inputInfo():
        # Creating Variables for storing values
        Name = StringVar()
        Class = IntVar()
        RollNo = IntVar()
        Address = StringVar()
        PhoneNo = IntVar()
        AltNo = IntVar()
        MotherName = StringVar()
        MotherOccupation = StringVar()
        FatherName = StringVar()
        FatherOccupation = StringVar()
        Dob = []
        DateOfBirth = StringVar()
        Caste = StringVar()
        Gender = StringVar()

        inputInfos = Tk()
        inputInfos.title(f"Input Screen for {classNo}")
        inputInfos.geometry('490x460')
        inputInfos.resizable(0, 0)

        inputs = Frame(inputInfos)
        Label(inputs, text="Input details below", font="comicsansmc 17 bold", justify='center').grid(row=0, column=0, pady=10, padx=10)
        # Name
        Label(inputs, text="Name: ", font="comicsansmc 11", justify='left').grid(row=1, column=0, pady=5)
        Entry(inputs, textvariable=Name).grid(row=1, column=1, pady=5)
        # Class--
        Label(inputs, text="Class: ", font="comicsansmc 11").grid(row=2, column=0)
        classes = Combobox(inputs, state='readonly', values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], width=17)
        classes.grid(column=1, row=2)
        # Roll No.
        Label(inputs, text="Roll No.: ", font="comicsansmc 11").grid(row=3, column=0, pady=5)
        Entry(inputs, textvariable=RollNo).grid(row=3, column=1, pady=5)
        # Address
        Label(inputs, text="Address: ", font="comicsansmc 11").grid(row=4, column=0)
        Entry(inputs, textvariable=Address).grid(row=4, column=1)
        # Phone No.
        Label(inputs, text="Phone No.: ", font="comicsansmc 11").grid(row=5, column=0, pady=5)
        Entry(inputs, textvariable=PhoneNo).grid(row=5, column=1, pady=5)
        # Alternative No.
        Label(inputs, text="Alternative No.: ", font="comicsansmc 11").grid(row=6, column=0)
        Entry(inputs, textvariable=AltNo).grid(row=6, column=1)
        # Mother
        Label(inputs, text="Mother Name: ", font="comicsansmc 11").grid(row=7, column=0, pady=5)
        Entry(inputs, textvariable=MotherName).grid(row=7, column=1, pady=5)
        Label(inputs, text="Mother's Occupation: ", font="comicsansmc 11").grid(row=8, column=0)
        Entry(inputs, textvariable=MotherOccupation).grid(row=8, column=1)
        # Father
        Label(inputs, text="Father Name: ", font="comicsansmc 11").grid(row=9, column=0, pady=5)
        Entry(inputs, textvariable=FatherName).grid(row=9, column=1, pady=5)
        Label(inputs, text="Father's Occupation: ", font="comicsansmc 11").grid(row=10, column=0)
        Entry(inputs, textvariable=FatherOccupation).grid(row=10, column=1)
        # Date of Birth--
        Label(inputs, text="Date of Birth: ", font="comicsansmc 11").grid(row=11, column=0, pady=5)
        month = Combobox(inputs, state='readonly', values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], width=17)
        month.grid(column=1, row=11)
        day = Combobox(inputs, state='readonly', values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], width=2)
        day.grid(column=2, row=11)
        year = Entry(inputs, width=8)
        year.grid(row=11, column=3, pady=5)
        # Caste--
        Label(inputs, text="Caste: ", font="comicsansmc 11").grid(row=12, column=0)
        caste = Combobox(inputs, state='readonly', values=["Hindu", "Muslim", "Sikh", "Christian", "Others"], width=17)
        caste.grid(column=1, row=12)
        # Gender--
        Label(inputs, text="Gender: ", font="comicsansmc 11").grid(row=13, column=0, pady=5)
        caste = Combobox(inputs, state='readonly', values=["Male", "Female", "Others"], width=17)
        caste.grid(column=1, row=13, pady=5)
        # Submit Button
        Button(inputs, text="Submit", command=Submit.infoSubmit).grid(row=14, column=1, pady=20)
        inputs.grid(row=0, column=0, padx=15)

        inputInfos.mainloop()

class Edit:
    @staticmethod
    def editInfo():
        editInfos = Tk()
        editInfos.title(f"Edit Screen for {classNo}")
        editInfos.geometry('200x120')
        editInfos.resizable(0, 0)

        Label(editInfos, text="Enter Name", font="comicsansmc 15 bold").pack(pady=5)
        Entry(editInfos).pack(pady=5)
        Button(editInfos, text="Enter").pack(pady=8)

        editInfos.mainloop()

class View:
    @staticmethod
    def viewInfo():
        viewInfos = Tk()
        viewInfos.title(f"View Screen for {classNo}")
        viewInfos.geometry('200x120')
        viewInfos.resizable(0, 0)

        Label(viewInfos, text="Enter Name", font="comicsansmc 15 bold").pack(pady=5)
        Entry(viewInfos).pack(pady=5)
        Button(viewInfos, text="Enter").pack(pady=8)

        viewInfos.mainloop()

class System:
    @staticmethod
    def infoManagementSystem():
        ims = Tk()
        ims.title(f"{classNo}")
        ims.geometry('450x235')
        ims.resizable(0, 0)

        Label(ims, text="Info Management System", font="comicsansmc 17 bold").pack(pady=10)
        index = Frame(ims)
        Button(index, text="   Add Student Details    ", command=Input.inputInfo).pack(pady=14)
        Button(index, text="Remove Student Details", command=Delete.deleteInfo).pack()
        Button(index, text="    Edit Student Details    ", command=Edit.editInfo).pack(pady=14)
        Button(index, text="   View Student Details   ", command=View.viewInfo).pack()
        index.pack()

        ims.mainloop()

class Main:
    @staticmethod
    def mainScreen():
        ms = Tk()
        ms.title(f"{classNo}")
        ms.geometry('450x235')
        ms.resizable(0, 0)

        Label(ms, text="Students Management System", font="comicsansmc 17 bold").pack(side=TOP, pady=10)

        index = Frame(ms)
        Button(index, text="       Info Management System        ", command=System.infoManagementSystem).pack(pady=14)
        Button(index, text="        Fee Management System         ").pack()
        Button(index, text=" Attendence Management System ").pack(pady=14)
        Button(index, text="      Library Management System     ").pack()
        index.pack(side=TOP)

        ms.mainloop()

    @staticmethod
    def getVal(val):
        global classNo
        classNo = val
        Main.mainScreen()

    @staticmethod
    def classScreen():
        cs = Tk()
        cs.title("Holy Trinity Church School")
        cs.geometry('450x560')
        cs.resizable(0, 0)

        Label(cs, text="Select Class", font="comicsansmc 17 bold").pack(side=TOP, pady=10)

        index = Frame(cs)
        Button(index, text=" Class 1 ", command=lambda m="Class 1": Main.getVal(m)).pack(pady=14)
        Button(index, text=" Class 2 ", command=lambda m="Class 2": Main.getVal(m)).pack()
        Button(index, text=" Class 3 ", command=lambda m="Class 3": Main.getVal(m)).pack(pady=14)
        Button(index, text=" Class 4 ", command=lambda m="Class 4": Main.getVal(m)).pack()
        Button(index, text=" Class 5 ", command=lambda m="Class 5": Main.getVal(m)).pack(pady=14)
        Button(index, text=" Class 6 ", command=lambda m="Class 6": Main.getVal(m)).pack()
        Button(index, text=" Class 7 ", command=lambda m="Class 7": Main.getVal(m)).pack(pady=14)
        Button(index, text=" Class 8 ", command=lambda m="Class 8": Main.getVal(m)).pack()
        Button(index, text=" Class 9 ", command=lambda m="Class 9": Main.getVal(m)).pack(pady=14)
        Button(index, text=" Class 10 ", command=lambda m="Class 10": Main.getVal(m)).pack()
        Button(index, text=" Class 11 ", command=lambda m="Class 11": Main.getVal(m)).pack(pady=14)
        Button(index, text=" Class 12 ", command=lambda m="Class 12": Main.getVal(m)).pack()
        index.pack(side=TOP, fill=BOTH)
        
        cs.mainloop()

Main.classScreen()