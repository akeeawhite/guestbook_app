__author__ = 'Owner'
from tkinter import messagebox
from tkinter import *
import sqlite3

# create a connection to the newly made database
cxn = sqlite3.connect('GuestDB')
# initialize a cursor object to run execute commands on the connected database.
cur = cxn.cursor()

#Class for displaying paycheck after calculations
class AddGuest():

    #myMainWindowClass = MainWindow(empName)
    def __init__(self, master):

        #creates master window for calculation window, changes title, and sets size
        self.master = master
        self.master.title("Add Guest")
        self.master.geometry("250x180")

        self.firstName = StringVar()
        self.lastName = StringVar()
        self.address = StringVar()
        self.checkInDate = StringVar()
        self.checkOutDate = StringVar()

        #Creates labels for outputting the calculations
        self.lblFirst = Label(self.master, text="First Name: ")
        txtBoxFirstName = Entry(self.master, textvariable=self.firstName)
        self.lblLast = Label(self.master, text="Last Name: ")
        txtBoxLastName = Entry(self.master, textvariable=self.lastName)
        self.lblAddress = Label(self.master, text="Address: ")
        txtBoxAddress = Entry(self.master, textvariable=self.address)
        self.lblCheckIn = Label(self.master, text="Check In Date: ")
        txtBoxCheckIn = Entry(self.master, textvariable=self.checkInDate)
        self.lblCheckOut = Label(self.master, text="Check Out Date: ")
        txtBoxCheckOut = Entry(self.master, textvariable=self.checkOutDate)

        #Close Button
        self.btnClose = Button(self.master, text="Close", width=8, command=self.quit)

        #Aligns button in grid
        self.btnClose.grid(row=7, column=2)

        #Aligns the labels using the grid
        self.lblFirst.grid(row=1, column=1, sticky=W)
        txtBoxFirstName.grid(row=1, column=2, sticky=E)
        self.lblLast.grid(row=2, column=1, sticky=W)
        txtBoxLastName.grid(row=2, column=2)
        self.lblAddress.grid(row=3, column=1, sticky=W)
        txtBoxAddress.grid(row=3, column=2)
        self.lblCheckIn.grid(row=4, column=1, sticky=W)
        txtBoxCheckIn.grid(row=4, column=2, sticky=E)
        self.lblCheckOut.grid(row=5, column=1, sticky=W)
        txtBoxCheckOut.grid(row=5, column=2)
        self.btnAdd = Button(self.master, text="Add", width=8, command=self.add)
        self.btnAdd.grid(row=6, column=2)

    def quit(self):
        self.master.destroy()

    def add(self):
        # Add instructors to the database
        first = self.firstName.get()
        last = self.lastName.get()
        address = self.address.get()
        checkIn = self.checkInDate.get()
        checkOut = self.checkOutDate.get()


        if first == '' or last == '' or address == '':
            messagebox.showwarning("Error", "Please fill in all empty text boxes!")

        else:
            try:
                cur.execute('INSERT INTO Guest VALUES(NULL, ?, ?, ?, ?, ?)', (first, last, address, checkIn, checkOut))
                messagebox.showwarning("New Guest Added", "New Guest successfully added")

            except sqlite3.IntegrityError:
                messagebox.showwarning("New Guest could not be added")

            finally:
                cxn.commit()