"""
Lab: Build a Planet Class

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

1. You should create a class named Planet.

2. The Planet class should have an __init__ method that:
   - Has four parameters: self, name, planet_type, and star.
   - Raises a TypeError with the message "name, planet type, and star must be strings" if any of the arguments passed in is not a string type.
   - Raises a ValueError with the message "name, planet_type, and star must be non-empty strings" if any of the arguments passed in is an empty string.
   - Assigns the values passed in to the instance attributes name, planet_type, and star.

3. The Planet class should have an orbit method that returns a string in the format "{name} is orbiting around {star}...."

4. The Planet class should have a __str__ method that returns a string in the format "Planet: {name} | Type: {planet_type} | Star: {star}".

5. You should create three instances of the Planet class named planet_1, planet_2, and planet_3.

6. You should print each planet object to see the __str__ method output.

7. You should call the orbit method on each planet object and print the result.
"""

class Planet:
    def __init__(self, name, planet_type, star):
        if not isinstance(name, str):
            raise TypeError("name, planet type, and star must be strings")
        if not isinstance(planet_type, str):
            raise TypeError("name, planet type, and star must be strings")
        if not isinstance(star, str):
            raise TypeError("name, planet type, and star must be strings")
        
        if name == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")
        if planet_type == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")
        if star == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")
        
        self.name = name
        self.planet_type = planet_type
        self.star = star
    
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."
    
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


planet_1 = Planet("Earth", "Terrestrial", "Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "Sun")
planet_3 = Planet("Mars", "Terrestrial", "Sun")

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())