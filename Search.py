__author__ = 'Owner'
from tkinter import messagebox
from tkinter import *
import sqlite3

# create a connection to the newly made database
cxn = sqlite3.connect('GuestDB')
# initialize a cursor object to run execute commands on the connected database.
cur = cxn.cursor()

#Class for searching for instructors, times, or classes
class Search():

    #myMainWindowClass = MainWindow(empName)
    def __init__(self, master):
        #creates master window for calculation window, changes title, and sets size
        self.master = master
        self.master.title("Search")
        self.master.geometry("250x200")

        #Sets the string variable and checkBox variables
        self.userSearchInput = StringVar()

        #Widgets
        self.lblSearchInformation = Label(self.master, text="Search For Guest Last Name")
        self.lblSearch = Label(self.master, text="Search: ")
        self.txtBoxSearch = Entry(self.master, textvariable=self.userSearchInput)

        #Search Button
        self.btnSearch = Button(self.master, text="Search", width=12, command=self.searchQuery)
        #Close Button
        self.btnClose = Button(self.master, text="Close", width=12, command=self.quit)

        #Aligns the labels using the grid
        self.lblSearchInformation.grid(row=1, columnspan=1, sticky=W)
        self.lblSearch.grid(row=5, columnspan=1, sticky=W)
        self.txtBoxSearch.grid(row=6, columnspan=1, sticky=W)
        self.btnSearch.grid(row=7, columnspan=1, sticky=W)
        self.btnClose.grid(row=8, columnspan=1, sticky=W)

    #Searh Query Function
    def searchQuery(self):
        self.userSearchCriteria = self.userSearchInput.get()

        if(self.userSearchCriteria == ""):
            messagebox.showerror("Entry Error", "Textbox cannot be empty")
        else:
            try:
                    guestList = []
                    cur.execute("SELECT * FROM Guest WHERE lastName LIKE ?", (self.userSearchCriteria + "%",))
                    for info in cur.fetchall():
                        guest = "Room Number ID: " + str(info[0]) + " Name: " + info[1] + " " + info[2] + \
                                     "Address: " + info[3] + " Check In Date: " + info[4] + " Check Out Date: " + info[5]
                        guestList.append(guest)
                    msg = "\n".join(guestList)
                    messagebox.showinfo("Query Results", msg)

            except sqlite3.IntegrityError:
                messagebox.showwarning("Search Error", "No matches could be found")

            finally:
                cxn.commit()

    def quit(self):
        cur.close()
        cxn.commit()
        cxn.close()
        self.master.destroy()
