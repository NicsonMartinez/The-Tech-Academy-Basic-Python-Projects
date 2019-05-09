#this file would be condidered a module that can be used in a differnt python file.

def print_app():
    name = (__name__) #Means to get the name of this file, app.py and store it in variable 'name'
    return name

