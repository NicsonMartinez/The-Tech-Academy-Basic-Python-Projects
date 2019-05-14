# The Tech Academy - GUI Drill 1
#
# Nicson Martinez
# 5/14/19

import tkinter
from tkinter import *

class TheMainWindow (Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(595, 185))
        self.master.title('Check Files')
        
#-----------------------------------------Row 0-------------------------------------------
        self.btnBrowse1 = Button(self.master, text='Browse...', width=15)
        self.btnBrowse1.grid(row=0, column=0, padx=(20,0), pady=(50,0))

        self.txtBox1 = Entry(self.master, font=('Arial', 10), fg='black', width=58)
        self.txtBox1.grid(row=0, column=1, padx=(30,0), pady=(50,0))

#-----------------------------------------Row 1-------------------------------------------

        self.btnBrowse2 = Button(self.master, text='Browse...', width=15)
        self.btnBrowse2.grid(row=1, column=0, padx=(20,0), pady=(10,0))

        self.txtBox2 = Entry(self.master, font=('Arial', 10), fg='black', width=58)
        self.txtBox2.grid(row=1, column=1, padx=(30,0), pady=(10,0))

#-----------------------------------------Row 2-------------------------------------------

        self.btnFileCheck = Button(self.master, text='Check for files...', width=15, height=2)
        self.btnFileCheck.grid(row=2, column=0, padx=(20,0), pady=(10,0))

        self.btnCloseProg = Button(self.master, text='Close Program', width=15, height=2)
        self.btnCloseProg.grid(row=2, column=1, sticky=SE)




if __name__=="__main__":
    root = Tk()
    App = TheMainWindow(root)
    root.mainloop()