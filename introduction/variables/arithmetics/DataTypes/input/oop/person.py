class person:
    category ='person'

    def __init__(self, name, age,weight):
        self.name = name
        self.age = age
        self.weight = weight


john = person('john',15,14)
mary = person('mary',14,40)
david =person('david',12,35)

print('John is a {}'.format(john.__class__.category))
print('mary is also a {}'.format(mary.__class__.category))
print('david is a{}'.format(david.__class__.category))

print('{} is {} years old.his weight is {}'.format(john.name, john.age, john.weight))
print('{} is {} years old.her weight is {}'.format(mary.name,mary.age, mary.weight))
print('{}is{}years old.his weight is{}'.format(david.name,david.age,david.weight))



    

    
        
        
        
    








class Persons:
    
    def __init__(self ,name ,age):
        self.name =name
        self.age =age

    def run(self,marathon):
        return '{} runs a{}'.format(self.name,marathon)


    def read(self):
        return'{}is now reading'.format(self.name)

john = Persons('John',15)

print(john.run('42 km'))
print(john.read())