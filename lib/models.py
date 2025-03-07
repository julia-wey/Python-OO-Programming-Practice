#!/usr/bin/env python3
import ipdb;

class Pet:
    pet_count = 0
    all = []

    def __init__(self, name="Pet", age=0, breed="Unknown"):
        self.name = name
        self.age = age
        self.breed = breed

        Pet.increment_pets()
        Pet.add_new_pet(self)

    @classmethod
    def increment_pets(cls):
        cls.pet_count += 1

    @classmethod
    def add_new_pet(cls, new_pet):
        cls.all.apped(new_pet)

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

#apollo = Pet(name='Apollo', age=2, breed= 'dog')
#daisy = Pet(name='Daisy', breed='cat')
#teddy = Pet(name="Teddy", breed="dog", age=3)

class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        print("get_name was called")
        return self._name 
    
    def set_name(self, new_name):
        print('set_name was called')
        if type(new_name) == str:
            self._name = new_name
        else:
            raise TypeError("Name must be of type string")
        
    name = property(get_name, set_name)

    def get_age(self):
        return self._age 
    
    def set_age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
        else:
            raise TypeError('Age must be an interger')
        
    age = property(get_age, set_age)

#ipdb.set_trace()

