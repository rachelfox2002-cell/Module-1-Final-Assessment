class Planet:
    def __init__(self, name, mass, distance, moons):
        self.name = name 
        self.mass = mass
        self.distance = distance
        self.moons = moons
    
    def moon_count(self):
        return len(self.moons)
    
class SolarSystem:
    def __init__(self):
        self.planets = []
        self.planet_data()
    
    def planet_data(self):
        self.planets.append(Planet("Mercury", 3.30e23, 58, []))
        self.planets.append(Planet("Venus", 4.87e24, 108, []))
        self.planets.append(Planet("Earth", 5.97e24, 150, ["Moon"]))
        self.planets.append(Planet("Mars", 6.42e23, 228, ["Phobos", "Deimos"]))
        self.planets.append(Planet("Jupiter", 1.90e27, 778, ["Io", "Europa", "Ganymede", "Callisto"]))
        self.planets.append(Planet("Saturn", 5.68e26, 1430, ["Titan", "Enceladus", "Rhea", "Mimas"]))
        self.planets.append(Planet("Uranus", 8.68e25, 2870, ["Miranda", "Titania", "Oberon", "Ariel"]))
        self.planets.append(Planet("Neptune", 1.02e26, 4490, ["Triton", "Thalassa"]))
  
    def get_planet(self, name):
        for planet in self.planets:
            if planet.name.lower() == name.lower():
                return planet
        return []
    
def menu(solar_system):
    print("Solar system facts!")
    print("1. All Planet information")
    print("2. Mass of the planet")
    print("3. Is the planet in the lists of planets")
    print("4. Number of main moons the planets have")

    choice = input("Choose an option:")

    if choice == "1":
        name = input("Planet name: ")
        planet = system.get_planet(name)
        if Planet:
            print("Name: ")
            print("Mass:", planet.mass, "kg")
            print("Distance from Sun:", planet.distance, "million km")
            if planet.moons == "none":
                print("Moons: none")
            else: 
                print("Moons:" ", ".join(planet.moons))
        else:
             print("Enter a different Planet")

    if choice == "2":
        name = input("Planet name: ")
        planet = system.get_planet(name)
        if Planet:
            print(planet.name, "Mass:", planet.mass, "kg")
        else:
            print("Enter a different Planet")

    if choice == "3":
        name = input("Planet name: ")
        if system.get_planet(name):
            print("Yes")
        else:
            print("No")
            
    if choice == "4":
        name = input("Planet name: ")
        planet = system.get_planet(name)
        if Planet:
            print(planet.name ,"has", planet.moon_count(), "moons")
        else:
            print("Enter a different Planet")

system = SolarSystem()
menu(system)

         
