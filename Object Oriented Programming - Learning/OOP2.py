


# parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None #Type 'None' is like a 'Null' value
    arms = None
    dna = "Squence A"
    origin = "Unknown"
    carbon_based = True

    #passing in 'self' gives access to the attributes and values above
    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

# child class instance
# by doing this we the child class gets to inherit attributes from  its parent class
class Human(Organism):
    name = 'MacGuyver'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and roll of duct tape!"
        return msg

# another child calss instance
class Dog(Organism):
    name = 'Spot'
    species = 'canine'
    legs = 4
    arms = 0
    dna = 'Sequence B'
    origin = 'Earth'

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on its target!"
        return msg

# another child class instance
class Bacterium(Organism):
    name = 'x'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = 'Sequence C'
    origin = 'Mars'

    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two organisms!"
        return msg



if __name__ ==  "__main__":
    human = Human() # we are instantiating 'Human()' and giving it the name of 'human'
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())


    
