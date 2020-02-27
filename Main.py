from Planatarium import Planatarium
planets=Planatarium()
for i in range(len(planets.planets)):
    print(f"{i}: {planets.planets[i].name}")
ind=int(input("Which Number Would you Like to see?"))
print(f"Name:{planets.planets[ind].name}")
print(f"Mass:{planets.planets[ind].mass}")
print(f"Color:{planets.planets[ind].color}")