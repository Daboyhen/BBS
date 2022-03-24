class Car:
    
    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')


    def __updatesoftware(self):
        print('updatingsoftware')    
#teslacar = Car()
#teslacar.drive()



class Cars:
    __maxspeed =0
    __name =''
    
    def __init__(self):
        self.__maxspeed =200
        self.__name = 'tesla car'

    def drive(self):
        print('driving. maxspeed' + str(self.__maxspeed))

    #using the setter method to change the value of a private variable
    def setMaxSpeed(self, speed):
        self.__maxspeed= speed

teslacar =Cars()
teslacar.drive()
teslacar.setMaxSpeed(50)
teslacar.drive()