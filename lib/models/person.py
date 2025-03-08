class Person:
    def __init__(self, name="Jane Doe", age=0):
        self.name = name
        self.age = age
        self.hygiene = 10
    
    def workout(self, type_of_workout):
        decrement = 2
        if type_of_workout == 'Run':
            decrement = 5
        
        self.hypiene = self.hygiene - decrement
        self.print_current_hygiene()
        if self.hygiene < 4:
            print('Take a shower!')
        
    def take_shower(self):
        self.hygiene = 10
        self.print_current_hygiene()
    
    def take_shower(self):
        self.hygiene = 10
        self.print_current_hygiene()
    
    def print_current_hygiene(self):
        print(f"Your current hygiene level is noe {self.hygiene}")
    
    def get_age(self):
        return self.get_age
    
    def set_age(self, new_age):
        if isinstance(new_age, int):
            if new_age > 12:
                self._age =new_age
            else:
                raise ValueError('Age must be greater than 12')
        else:
            raise TypeError('Age must be of type int')
        
    age = property(get_age, set_age)
    