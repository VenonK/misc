# tkinter comes as part of the standard install - message box has to be imported explicitly
from tkinter import *
from tkinter import messagebox

def saveStaff():
    StaffIDSave = StaffIDVar.get()
    StaffIDSave = StaffIDSave.ljust(50)

    FirstNameSave = FirstNameVar.get()
    FirstNameSave = FirstNameSave.ljust(50)

    SurnameSave = SurnameVar.get()
    SurnameSave = SurnameSave.ljust(50)

    PostcodeSave = PostcodeVar.get()
    PostcodeSave = PostcodeSave.ljust(50)

    # 3 steps for file handling
    # 1. Open the file and select read or write
    # 2. Do something - usually read or write
    # 3. Close the file!

    fileObject = open("employee.txt","a")
    fileObject.write(StaffIDSave + FirstNameSave + SurnameSave + PostcodeSave + "\n")
    fileObject.close()

    return 

def countStaff():
    # two local variables
    StaffCount = 0
    CountNeeded = 0

    # Get the data from the entry boxes - Thus will used to search the file
    StaffIDSave = StaffIDVar.get()
    FirstNameSave = FirstNameVar.get()
    SurnameSave = SurnameVar.get()
    PostcodeSave = PostcodeVar.get()

    # presence check to see if something has been entered
    # if its been entered we need to check the file to see if the data is present

    if not StaffIDSave == "":
        CountNeeded += 1
    if not FirstNameSave == "":
        CountNeeded += 1
    if not SurnameSave == "":
        CountNeeded += 1
    if not PostcodeSave == "":
        CountNeeded += 1

    if CountNeeded == 0:
        messagebox.showerror("Error","Please enter something to count")
        return
    
    try:
        fileObject = open("employee.txt","r")
    except IOError:
        messagebox.showerror("Error","No file to read")
    else:
        while True:
            CountGot = 0
            recordVar = fileObject.readline()

            if recordVar == "":
                fileObject.close()
                break
                
            if (StaffIDSave in recordVar[0:50]) and (not(StaffIDSave == "")):
                CountGot += 1
            
            if (FirstNameSave in recordVar[0:50]) and (not(FirstNameSave == "")):
                CountGot += 1

            if (SurnameSave in recordVar[0:50]) and (not(SurnameSave == "")):
                CountGot += 1

            if (PostcodeSave in recordVar[0:50]) and (not(PostcodeSave == "")):
                CountGot += 1

            if CountGot == CountNeeded:
                StaffCount += 1
        
        messagebox.showinfo("Found: ",str(StaffCount))

            
    


def makeWindow():

    # Put your global variable here
    global StaffIDVar, FirstNameVar, SurnameVar, PostcodeVar

    #Create a window
    window = Tk()

    # Creation of the first frame, for the 
    frame1 = Frame(window)
    frame1.pack()

    Label(frame1, text= "Pauls Pizzeria Employees", font=("Arial")).grid(row=0,column=0)
    
    Label(frame1, text="StaffID").grid(row=1, column=0, sticky=W)
    StaffIDVar = StringVar()
    StaffID = Entry(frame1, textvariable=StaffIDVar)
    StaffID.grid(row=1, column=1, sticky=W)


    Label(frame1, text="First name").grid(row=2, column=0, sticky=W)
    FirstNameVar = StringVar()
    FirstName = Entry(frame1, textvariable=FirstNameVar)
    FirstName.grid(row=2, column=1, sticky=W)


    Label(frame1, text="Surname").grid(row=3, column=0, sticky=W)
    SurnameVar = StringVar()
    Surname = Entry(frame1, textvariable=SurnameVar)
    Surname.grid(row=3, column=1, sticky=W)

    Label(frame1, text="Postcode").grid(row=4, column=0, sticky=W)
    PostcodeVar = StringVar()
    Postcode = Entry(frame1, textvariable=PostcodeVar)
    Postcode.grid(row=4, column=1, sticky=W)
    
    frame2 = Frame(window)
    frame2.pack()
    b1 = Button(frame2, text="Save Staff", command=saveStaff)
    b2 = Button(frame2, text="Count Staff", command=countStaff)
    b1.pack(side=LEFT); b2.pack(side=LEFT)

    return window

# This is the main program
window = makeWindow()
window.mainloop()