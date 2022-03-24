class Person:
    def __init__(self):
        print('person class is ready')
    def whoisthis(self):
        print('person')

    def walk(self):
        print('walk to any direction')


class adult (Person):

    def __init__(self):
        super().__init__()
        print('adult is ready')


def whoisthis(self): 
    print('adult')

def read(self):
    super().__init__()
    print('adult is ready')

def whoisthis(self):
    print ('walk to any direction')

class adult(Person):

    def __init__(Self):
        super().__init__()
        print("adult is ready")

    def whoisthis(self):
        print('adult')
    
    def read(self):
        print('reading')

chirles = adult()
chirles.whoisthis()
chirles.walk()
chirles.read()



class  vehicle:

    def __init__(self):
        super().__init__()
    print('vehicle is broken')

    def __init__(self):
        super().__init__()
        print('vehicle is expensive')



    def __init__(self):
        super().__init__()
    print('vehicle has been bought')