import tkinter
from tkinter import * 


# in __init__ we are referencing our class as 'master', and we are referencing our Frame as 'master'
class ParentWindow(Frame): # 'Frame' (inheriting from tkinter)
    def __init__ (self, master):# def __init__ (self, master, **args, **kwargs): NOTE: extra things that developer use.
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False) #can't resize
        self.master.geometry('{}x{}'.format(700, 400)) #syntax, width x height
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray') #background color

        self.varFName = StringVar() #we are instantiating StringVar. That instance is called varFName
        self.varLName = StringVar()

        #You cannot use grid() and pack() managers.. it will create an error. 
        self.lblFName = Label(self.master, text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))
        # For padx/pady the first patameter is for the left of our object and the second parameter is for the right of our object.
        

        self.lblFName = Label(self.master, text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblFName.grid(row=1, column=0, padx=(30,0), pady=(30,0))
        #It is possible to use two clumns in a row for an object by using columnspan eg. x.grid(columnspan=2)

        #This is the placeholder for the message we want to generate from the firs/last name entries
        self.lblDisplay = Label(self.master, text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        # Here we are creating a text box where the user entry will be stored in self.varFName
        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))
        
        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)
        # The 'ticky' option decides which corner or side should the object lean/stick to.

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varFName.get() #Gets the value of what is insde of self.varFNAME and stores it in fn.
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))
        # When we want to dinamically change an object on our GUI we use config()

    def cancel(self):
        self.master.destroy()





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() #if we don't do the mainloop() function, the window would not stay up. it would open and close right away.

