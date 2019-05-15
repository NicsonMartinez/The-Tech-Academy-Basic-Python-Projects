# The Tech Academy - GUI Drill 2
#
# Drill Description:
# For this drill, you will need to write a script that creates a GUI with a button widget 
# and a text widget. Your script will also include a function that when it is called will 
# invoke a dialog modal which will allow users with the ability to select a folder directory 
# from their system. Finally, your script will show the user’s selected directory path into 
# the text field.
#
# Nicson Martinez
# 5/14/19


from tkinter import * 
from tkinter import filedialog
from tkinter import Tk
import os

class TheMainWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(595, 190))
        self.master.title('Check Files')
        self.master.config(bg='lightgray')
        
#-------------------------------------GUI Row 0-------------------------------------------
        self.btnBrowse1 = Button(self.master, text='Browse...', width=15, height=2, command = self.browseDirectory)
        self.btnBrowse1.grid(row=0, column=0, padx=(20,0), pady=(50,0))

        self.txtBox1 = Entry(self.master, font=('Arial', 10), fg='black', width=60)
        self.txtBox1.grid(row=0, column=1, padx=(10,0), pady=(45,0))

#-------------------------------------GUI Row 1-------------------------------------------

        self.lblMsg = Label(self.master, text='', font=('Arial', 10), fg='black', width=55, bg='lightgray')
        self.lblMsg.grid(row=1, column=1, padx=(5,0), pady=(0,20))

#-------------------------------------GUI Row 2-------------------------------------------

        self.btnCloseProg = Button(self.master, text='Close Program', width=15, height=2, command=self.close)
        self.btnCloseProg.grid(row=2, column=1, sticky=SE)

#---------------------------------[ Button Functions ]--------------------------------------

    def browseDirectory(self):
        # This is done in case the user decided to type something in the textbox before
        # pressing the [Browse...] button.
        test = self.txtBox1.get() 
        print(test)

        test1 = self.txtBox1.delete(0, END) #Deletes chars located in index 0,1,2,3...until END.
        print(test1)
        
        dirVariable = filedialog.askdirectory()
        self.lblMsg.config(text='Above is the directory path you have selected!')
        self.txtBox1.insert(0, dirVariable)
        print(self.txtBox1.get())

    def close(self):
        self.master.destroy()

if __name__=="__main__":
    root = Tk()
    App = TheMainWindow(root)
    root.mainloop()