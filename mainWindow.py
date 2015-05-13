__author__ = 'Owner'
from tkinter import *
from AddGuest import AddGuest
from DeleteGuest import DeleteGuest
from Search import Search
import sqlite3

# create a connection to the newly made database
cxn = sqlite3.connect('GuestDB')
# initialize a cursor object to run execute commands on the connected database.
cur = cxn.cursor()


# start a try-except block to handle SQL-Exceptions
# create the table and fill it with data
try:
    cur.execute('CREATE TABLE Instructor(roomID INTEGER PRIMARY KEY, firstName VARCHAR(50), lastName VARCHAR(50), address VARCHAR(50))')
    cur.execute('CREATE TABLE Class(code VARCHAR(8) PRIMARY KEY, description VARCHAR(50), price FLOAT, instructorID INTEGER REFERENCES Instructor(roomID))')
    cur.execute('CREATE TABLE Schedule(code VARCHAR(8) REFERENCES Class(code), Day TEXT, time TEXT)')
    cur.execute('CREATE TABLE Student(id INTEGER PRIMARY KEY, firstName VARCHAR(50), lastName VARCHAR(50), address VARCHAR(50), amountDue FLOAT)')
    cur.execute('CREATE TABLE ClassStudent(code VARCHAR(8) REFERENCES Class(code), sequence INTEGER, studentID INTEGER REFERENCES Student(id))')
except sqlite3.OperationalError:
    print("The tables have been created already")

# Create some test data
try:
    def insert():
        cur.execute('INSERT INTO Instructor VALUES(NULL, "Bob", "Smith", "1234 Street")')
        cur.execute('INSERT INTO Class VALUES("Weight", "Lifting weights", 250.00, 1)')
        cur.execute('INSERT INTO Schedule VALUES("Weight", "Monday", "19:00")')
        cur.execute('INSERT INTO ClassStudent VALUES("Weight", 1, 1)')
        cur.execute('INSERT INTO Student VALUES(NULL, "Jane", "Smith", "1500 Tree Rd.", 0)')
except sqlite3.IntegrityError:
    print("Test data has been put in already")

class mainWindow():

    def __init__(self, master):

            #sets window to master, sets title, and window size
            self.master = master
            self.master.title("Class Manager")
            self.master.geometry("230x150")

#Declares and defines labels, buttons, and textboxes
            self.btnAddGuest = Button(self.master, text="Add Guest", width=13, command=self.addGuest)
            self.btnDeleteGuest = Button(self.master, text="Delete Guest", width=13, command=self.deleteInstructor)
            self.btnSearch = Button(self.master, text="Search", width=13, command=self.search)
            self.btnQuit = Button(self.master, text="Quit", width=13, command=self.quit)

            #Aligns all of the labels, buttons, and textboxes in grid form
            self.btnAddGuest.grid(row=1, column=1, sticky=W)
            self.btnDeleteGuest.grid(row=3, column=1, sticky=W)
            self.btnSearch.grid(row=4, column=1, sticky=W)
            self.btnQuit.grid(row=5, column=1)

    #Function for quit button to close window
    def quit(self):
        self.master.destroy()

    #Function for displaying the add instructor window
    def addInstructor(self):
        #Sets the addInstructor class to root2 so it is displayed when Add Instructor button is clicked
        root2 = Toplevel(self.master)
        AddGuest(root2)

    #Function for displaying the delete instructor window
    def deleteInstructor(self):
        #Sets the addInstructor class to root2 so it is displayed when Add Instructor button is clicked
        root2 = Toplevel(self.master)
        DeleteGuest(root2)

    #Function for displaying the searching window
    def search(self):
         #Sets the addInstructor class to root2 so it is displayed when Add Instructor button is clicked
        root2 = Toplevel(self.master)
        Search(root2)

##Creates the root window and loops it
def main():
    root = Tk()
    mainWindow(root)
    root.mainloop()

#Loops the code so the windows stay open
if __name__ == "__main__":
    main()

"""class Main:

    def __init__(self, master):
            #Creates variables for the textboxes
            self.name = StringVar()
            self.address = StringVar()
            self.city = DoubleVar()
            self.empHours = DoubleVar()

            #sets window to master, sets title, and window size
            self.master = master
            self.master.title("Guestbook Application")
            self.master.geometry("640x480")

            #Declares and defines labels, buttons, and textboxes
            self.lblTitle = Label(self.master, text="Guestbook Application", font=("Purisa", 12, "bold"), fg="blue")
            self.lblName = Label(self.master, text="Name: ")
            self.lblAddress = Label(self.master, text="Address: ")
            self.lblCity = Label(self.master, text ="City: ")
            self.btnCalculate = Button(self.master, text="Calculate Pay", width=13)
            self.btnQuit = Button(self.master, text="Quit", width=13, command=self.quit)
            txtBoxName = Entry(self.master, textvariable=self.name)
            txtBoxAddress = Entry(self.master, textvariable=self.city)
            txtBoxCity = Entry(self.master, textvariable=self.empHours)

            #Aligns all of the labels, buttons, and textboxes in grid form
            self.lblTitle.grid(columnspan=3)
            self.lblName.grid(row=1, column=1, sticky=W)
            self.lblAddress.grid(row=2, column=1, sticky=W)
            self.lblCity.grid(row=3, column=1, sticky=W)
            txtBoxName.grid(row=1, column=2)
            txtBoxAddress.grid(row=2, column=2)
            txtBoxCity.grid(row=3, column=2)
            self.btnCalculate.grid(columnspan=4)
            self.btnQuit.grid(columnspan=4)

    #Function for quit button to close window
    def quit(self):
        self.master.destroy()"""


##Creates the root window and loops it
def main():
    root = Tk()
    mainWindow(root)
    root.mainloop()

#Loops the code so the windows stay open
if __name__ == "__main__":
    main()