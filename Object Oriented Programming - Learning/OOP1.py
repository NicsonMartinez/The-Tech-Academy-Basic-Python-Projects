

#Writing the class
class Game:
    variable1 = 'Hello'
    variable2 = 'World!'


if __name__ == "__main__":
    x = Game() #instantiating that class,  giving it instance 'x'
    print("{} {}".format(x.variable1,x.variable2)) #giving that instance it's attributes and values
    
