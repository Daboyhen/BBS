class Hen(object):
    def feed(self):
        print('eats seeds')


class Duck(object):
    def feed(self):
        print('filter feeding')


def canFeed(birdType):
    birdType.feed()

henobj =Hen()
duckobj =Duck()
    
canFeed(henobj)
canFeed(duckobj)



#second example

class Vehicle:
    def __init__(self ,name):
        self.name =name  

    def stop(self):
        raise NotImplementedError('subclass must \
            abstract method')


class SUV(Vehicle):
    def drive(self):
        return'SUV is a very comfortable Vehicle'


    def stop(self):
        return 'The SUV is easy to control and make it stop'


class Bus(Vehicle):
    def drive(self):
        return 'be careful when stopping the bus'


Vehiclesobj =[Bus('Goes to CBD'),
Bus ('Goes to other places from CBD'),
SUV('Tesla')]

for Vehicle in Vehiclesobj:
     print (Vehicle.name + ':' + Vehicle.drive())



class Student:
    def __init__(self ,name):
        self.name =name

    def read(self):
        raise NotImplementedError('subclass must abstract method')


class Boy(Student):
    def read(self):
        return'Goes to school in the morning'


    def writing(self):
        return 'has lunch at school'


class Pupil:
    def __init__(self,name):
        self.name =name

    def writing(self):
        return 'goes home everyday'

class Girl(Pupil):
    def read(self):
        return 'walks to school everyday'


Studentobj=[Boy('plays ball'),
Boy('plays ball everywhere')]
Pupilobj=[Girl('takes care of baby'),
Girl('takes care of many babies')]

for Student in Studentobj:
    print (Student.name +':' + Student.read())



class