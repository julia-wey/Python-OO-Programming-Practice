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
        cls.all.append(new_pet)

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
