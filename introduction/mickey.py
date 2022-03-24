class Persons:
    def __init__(self,name,age):
        self.name =name
        self.age =age 

    def read(self):
        return'{}is now reading'.format(self.name)
        john=Persons('john',15)

print(john.run('42 km'))
print(john.read())