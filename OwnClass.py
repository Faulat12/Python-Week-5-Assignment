class Superhero:
    """Base Superhero class with common attributes and methods"""
    
    # Class variable to keep track of all superheroes
    total_heroes = 0
    
    def __init__(self, name, real_name, power_level, primary_power):
        """Constructor to initialize a superhero"""
        self.name = name
        self.real_name = real_name
        self.power_level = power_level
        self.primary_power = primary_power
        self.energy = 100  # All heroes start with full energy
        self.is_active = True
        self.__secret_weakness = "Unknown"  # Private attribute (encapsulation)
        
        # Increment the total number of heroes
        Superhero.total_heroes += 1
    
    def introduce(self):
        """Method to introduce the superhero"""
        return f"I am {self.name}! My primary power is {self.primary_power}."
    
    def use_power(self, intensity=1):
        """Method to use superhero's power"""
        energy_cost = intensity * 10
        if self.energy >= energy_cost:
            self.energy -= energy_cost
            return f"{self.name} uses {self.primary_power} with intensity {intensity}! Energy remaining: {self.energy}"
        else:
            return f"{self.name} is too tired to use their power! Energy: {self.energy}"
    
    def rest(self):
        """Method to restore energy"""
        self.energy = min(100, self.energy + 30)
        return f"{self.name} rests and recovers energy. Current energy: {self.energy}"
    
    def get_status(self):
        """Method to get current status"""
        status = "Active" if self.is_active else "Inactive"
        return f"{self.name} - Power Level: {self.power_level}, Energy: {self.energy}, Status: {status}"
    
    def _set_weakness(self, weakness):
        """Protected method to set weakness"""
        self.__secret_weakness = weakness
    
    def __str__(self):
        """String representation of the superhero"""
        return f"{self.name} (Real name: {self.real_name})"
    
    @classmethod
    def get_hero_count(cls):
        """Class method to get total number of heroes"""
        return f"Total superheroes created: {cls.total_heroes}"


class FlyingHero(Superhero):
    """Inherited class for heroes who can fly"""
    
    def __init__(self, name, real_name, power_level, primary_power, max_altitude):
        # Call parent constructor
        super().__init__(name, real_name, power_level, primary_power)
        self.max_altitude = max_altitude
        self.current_altitude = 0
        self.is_flying = False
    
    def take_off(self):
        """Method specific to flying heroes"""
        if not self.is_flying and self.energy >= 15:
            self.is_flying = True
            self.current_altitude = 100
            self.energy -= 15
            return f"{self.name} takes off and soars to {self.current_altitude} feet!"
        elif self.energy < 15:
            return f"{self.name} is too tired to fly!"
        else:
            return f"{self.name} is already flying!"
    
    def land(self):
        """Method to land"""
        if self.is_flying:
            self.is_flying = False
            self.current_altitude = 0
            return f"{self.name} lands safely on the ground."
        else:
            return f"{self.name} is already on the ground."
    
    def fly_higher(self):
        """Method to increase altitude"""
        if self.is_flying and self.current_altitude < self.max_altitude:
            self.current_altitude = min(self.max_altitude, self.current_altitude + 500)
            return f"{self.name} flies higher to {self.current_altitude} feet!"
        elif not self.is_flying:
            return f"{self.name} needs to take off first!"
        else:
            return f"{self.name} has reached maximum altitude of {self.max_altitude} feet!"
    
    # Method overriding (Polymorphism)
    def use_power(self, intensity=1):
        """Overridden method - flying heroes use less energy when airborne"""
        energy_cost = intensity * 10
        if self.is_flying:
            energy_cost = energy_cost * 0.8  # 20% less energy cost when flying
        
        if self.energy >= energy_cost:
            self.energy -= int(energy_cost)
            flight_bonus = " (with aerial advantage)" if self.is_flying else ""
            return f"{self.name} uses {self.primary_power} with intensity {intensity}{flight_bonus}! Energy remaining: {self.energy}"
        else:
            return f"{self.name} is too tired to use their power! Energy: {self.energy}"


class TechHero(Superhero):
    """Inherited class for technology-based heroes"""
    
    def __init__(self, name, real_name, power_level, primary_power, gadget_count):
        super().__init__(name, real_name, power_level, primary_power)
        self.gadget_count = gadget_count
        self.gadgets = []
        self.tech_level = 1
    
    def add_gadget(self, gadget_name):
        """Method to add a new gadget"""
        if len(self.gadgets) < self.gadget_count:
            self.gadgets.append(gadget_name)
            return f"{self.name} adds {gadget_name} to their arsenal!"
        else:
            return f"{self.name}'s gadget capacity is full! ({self.gadget_count} max)"
    
    def upgrade_tech(self):
        """Method to upgrade technology level"""
        if self.energy >= 25:
            self.tech_level += 1
            self.energy -= 25
            return f"{self.name} upgrades their tech to level {self.tech_level}!"
        else:
            return f"{self.name} needs more energy to upgrade tech!"
    
    def use_gadget(self, gadget_name):
        """Method to use a specific gadget"""
        if gadget_name in self.gadgets:
            tech_bonus = self.tech_level * 5
            return f"{self.name} uses {gadget_name} (Tech Level {self.tech_level} bonus: +{tech_bonus} effectiveness)!"
        else:
            return f"{self.name} doesn't have {gadget_name} in their arsenal!"
    
    # Method overriding (Polymorphism)
    def get_status(self):
        """Overridden method to include tech-specific info"""
        base_status = super().get_status()
        return f"{base_status}, Tech Level: {self.tech_level}, Gadgets: {len(self.gadgets)}/{self.gadget_count}"


# Demonstration of the class system
if __name__ == "__main__":
    print("=== SUPERHERO CLASS DEMONSTRATION ===\n")
    
    # Create different types of heroes
    superman = FlyingHero("Superman", "Clark Kent", 95, "Super Strength", 50000)
    batman = TechHero("Batman", "Bruce Wayne", 85, "Strategic Combat", 10)
    wonder_woman = Superhero("Wonder Woman", "Diana Prince", 90, "Divine Powers")
    
    print("1. HERO INTRODUCTIONS:")
    print(superman.introduce())
    print(batman.introduce())
    print(wonder_woman.introduce())
    print()
    
    print("2. BASIC POWER USAGE:")
    print(superman.use_power(2))
    print(batman.use_power(1))
    print(wonder_woman.use_power(3))
    print()
    
    print("3. FLYING HERO ABILITIES:")
    print(superman.take_off())
    print(superman.fly_higher())
    print(superman.use_power(2))  # Should use less energy while flying
    print(superman.land())
    print()
    
    print("4. TECH HERO ABILITIES:")
    print(batman.add_gadget("Grappling Hook"))
    print(batman.add_gadget("Smoke Bombs"))
    print(batman.add_gadget("Batarang"))
    print(batman.use_gadget("Batarang"))
    print(batman.upgrade_tech())
    print(batman.use_gadget("Grappling Hook"))
    print()
    
    print("5. HERO STATUS (Polymorphism in action):")
    print(superman.get_status())
    print(batman.get_status())  # Shows additional tech info
    print(wonder_woman.get_status())
    print()
    
    print("6. REST AND RECOVERY:")
    print(superman.rest())
    print(batman.rest())
    print(wonder_woman.rest())
    print()
    
    print("7. CLASS METHOD:")
    print(Superhero.get_hero_count())
    print()
    
    print("8. STRING REPRESENTATION:")
    print(f"Heroes: {superman}, {batman}, {wonder_woman}")