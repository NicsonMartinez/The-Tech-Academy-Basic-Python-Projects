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
        self.master.config(bg='Lightgray') #background color

        self.varFName = StringVar() #we are instantiating StringVar. That instance is called varFName
        self.varLName = StringVar()
        self.varFName.set('Bob')
        self.varLName.set('Smith')

        # Must write self because if we don't, it will not know how to access that object and you'll get a NameError: not defined.
        print(self.varFName.get())
        print(self.varLName.get())
        

        # Here we are creating a text box where the user entry will be stored in self.varFName
        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFName.pack()
        # pack() will place the entry on the frame without having to specify its placement.
        # Later on I will learn about the grid manager to be more specific on where to place things.

        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.pack()





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() #if we don't do the mainloop() function, the window would not stay up. it would open and close right away.

