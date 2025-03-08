#!/usr/bin/env python3
import ipdb;

class Owner(Person):
    
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

