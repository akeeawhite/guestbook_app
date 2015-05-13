__author__ = 'Owner'
from tkinter import messagebox
from tkinter import *
import sqlite3

# create a connection to the newly made database
cxn = sqlite3.connect('GuestDB')
# initialize a cursor object to run execute commands on the connected database.
cur = cxn.cursor()

#Class for deleting guests
class DeleteGuest():

    #myMainWindowClass = MainWindow(empName)
    def __init__(self, master):

        #creates master window for calculation window, changes title, and sets size
        self.master = master
        self.master.title("Delete Guest")
        self.master.geometry("220x70")

        self.lastName = StringVar()

        #Creates labels for outputting the calculations
        self.lblLast = Label(self.master, text="Last Name: ")
        txtBoxEmployeeLastName = Entry(self.master, textvariable=self.lastName)


        #Close Button
        self.btnClose = Button(self.master, text="Close", width=8, command=self.quit)

        #Aligns button in grid
        self.btnClose.grid(row=2, column=2)

        #Aligns the labels using the grid
        self.lblLast.grid(row=1, column=1, sticky=W)
        txtBoxEmployeeLastName.grid(row=1, column=2)

        self.btnDelete = Button(self.master, text="Delete", width=8, command=self.delete)
        self.btnDelete.grid(row=2, column=1)

    def quit(self):
        self.master.destroy()

    def delete(self):
        # Delete guests to the database
        last = self.lastName.get()

        if last == '':
            messagebox.showwarning("Error", "Please specify the guest you want to add!")

        else:
            try:
                cur.execute('DELETE FROM Guest WHERE lastName = ?', (last,))
                messagebox.showwarning("Guest Deleted", " Guest successfully deleted")

            except sqlite3.Error as e:
                messagebox.showwarning(e)

            finally:
                #cur.close()
                cxn.commit()
                #cxn.close()
