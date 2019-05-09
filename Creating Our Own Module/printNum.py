import ourModule
#To import the module, this file has to be in the same directory as the file, and in that case it will find it.
#Or else, we have to put the full path to that file tin order to import 

if __name__ == "__main__":
    results = ourModule.getNumbers(5,9)
    #We are using one of the functions in our module in the same way we use math.floor().
    print(results)
