import ipdb;

class Pet:
    def __init__(self, name="Pet", age=0, breed="Unknown"):
        self.name = name
        self.age = age
        self.breed = breed

    def hello(self):
        print('hello')
    
    def speak(self):
        if self.breed == 'dog':
            print('Bark')
        elif self.breed == 'cat':
            print('Meow')
        else:
            print('silence')
    
    def __repr__(self):
        return f'<Pet name={self.name}>'

apollo = Pet(name='Apollo', age=2, breed= 'dog')
daisy = Pet(name='Daisy', breed='cat')

