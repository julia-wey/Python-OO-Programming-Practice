import ipdb;

from models import Pet, Owner

apollo = Pet(name="Apollo", age=2, breed="Dog")
daisy = Pet(name="Daisy", breed="cat")

julia = Owner(name="Julia", age=22)
shannon = Owner(name="Shannon", age=33)
leah = Owner(name="Leah", age=44)


ipdb.set_trace()
