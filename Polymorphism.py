from abc import ABC, abstractmethod
import random

class Vehicle(ABC):
    """Abstract base class for all vehicles"""
    
    def __init__(self, name, speed, fuel_capacity):
        self.name = name
        self.speed = speed  # km/h
        self.fuel_capacity = fuel_capacity
        self.current_fuel = fuel_capacity
        self.distance_traveled = 0
        self.is_moving = False
    
    @abstractmethod
    def move(self):
        """Abstract method - must be implemented by all subclasses"""
        pass
    
    @abstractmethod
    def get_movement_sound(self):
        """Abstract method for movement sounds"""
        pass
    
    def refuel(self):
        """Common method for all vehicles"""
        self.current_fuel = self.fuel_capacity
        return f"{self.name} has been refueled to {self.fuel_capacity}L!"
    
    def get_status(self):
        """Get current vehicle status"""
        status = "Moving" if self.is_moving else "Stationary"
        return f"{self.name} - Speed: {self.speed} km/h, Fuel: {self.current_fuel}L, Status: {status}, Distance: {self.distance_traveled}km"
    
    def stop(self):
        """Stop the vehicle"""
        if self.is_moving:
            self.is_moving = False
            return f"{self.name} has stopped."
        return f"{self.name} is already stopped."


class Car(Vehicle):
    """Car class - moves by driving"""
    
    def __init__(self, name, speed, fuel_capacity, num_doors):
        super().__init__(name, speed, fuel_capacity)
        self.num_doors = num_doors
        self.gear = 1
    
    def move(self):
        """Car-specific movement implementation"""
        if self.current_fuel > 0:
            self.is_moving = True
            self.current_fuel -= 2
            self.distance_traveled += 10
            return f"🚗 {self.name} is driving on the road! {self.get_movement_sound()}"
        else:
            return f"{self.name} is out of fuel and cannot drive!"
    
    def get_movement_sound(self):
        """Car movement sounds"""
        sounds = ["Vroom vroom!", "Engine purring smoothly", "Tires gripping the asphalt"]
        return random.choice(sounds)
    
    def change_gear(self, new_gear):
        """Car-specific method"""
        if 1 <= new_gear <= 5:
            self.gear = new_gear
            return f"{self.name} shifts to gear {self.gear}"
        return f"Invalid gear for {self.name}!"


class Plane(Vehicle):
    """Plane class - moves by flying"""
    
    def __init__(self, name, speed, fuel_capacity, altitude_limit):
        super().__init__(name, speed, fuel_capacity)
        self.altitude_limit = altitude_limit
        self.current_altitude = 0
        self.is_airborne = False
    
    def move(self):
        """Plane-specific movement implementation"""
        if self.current_fuel > 5:
            self.is_moving = True
            self.current_fuel -= 5
            self.distance_traveled += 50
            if not self.is_airborne:
                self.current_altitude = 10000
                self.is_airborne = True
            return f"✈️ {self.name} is flying through the skies at {self.current_altitude}ft! {self.get_movement_sound()}"
        else:
            return f"{self.name} is out of fuel and cannot fly!"
    
    def get_movement_sound(self):
        """Plane movement sounds"""
        sounds = ["Whoooosh through the clouds!", "Jet engines roaring!", "Soaring silently above"]
        return random.choice(sounds)
    
    def land(self):
        """Plane-specific method"""
        if self.is_airborne:
            self.is_airborne = False
            self.current_altitude = 0
            self.is_moving = False
            return f"{self.name} has landed safely!"
        return f"{self.name} is already on the ground!"


class Boat(Vehicle):
    """Boat class - moves by sailing/motoring"""
    
    def __init__(self, name, speed, fuel_capacity, boat_type):
        super().__init__(name, speed, fuel_capacity)
        self.boat_type = boat_type  # "sailboat", "motorboat", "yacht"
        self.anchor_dropped = False
    
    def move(self):
        """Boat-specific movement implementation"""
        if self.anchor_dropped:
            return f"⚓ {self.name} cannot move - anchor is dropped!"
        
        if self.current_fuel > 1:
            self.is_moving = True
            self.current_fuel -= 1
            self.distance_traveled += 5
            return f"🚤 {self.name} is sailing across the water! {self.get_movement_sound()}"
        else:
            return f"{self.name} is out of fuel and cannot sail!"
    
    def get_movement_sound(self):
        """Boat movement sounds"""
        sounds = ["Splash splash through the waves!", "Cutting through the water smoothly", "Wind filling the sails!"]
        return random.choice(sounds)
    
    def drop_anchor(self):
        """Boat-specific method"""
        self.anchor_dropped = True
        self.is_moving = False
        return f"⚓ {self.name} has dropped anchor!"
    
    def raise_anchor(self):
        """Boat-specific method"""
        self.anchor_dropped = False
        return f"⚓ {self.name} has raised anchor and is ready to sail!"


class Bicycle(Vehicle):
    """Bicycle class - moves by pedaling (human-powered)"""
    
    def __init__(self, name, speed):
        # Bicycles don't use fuel, so we set it to 100 (representing rider's energy)
        super().__init__(name, speed, 100)
        self.gear_count = 21
        self.current_gear = 1
    
    def move(self):
        """Bicycle-specific movement implementation"""
        if self.current_fuel > 5:  # Rider's energy
            self.is_moving = True
            self.current_fuel -= 5  # Rider gets tired
            self.distance_traveled += 2
            return f"🚴 {self.name} is pedaling along the path! {self.get_movement_sound()}"
        else:
            return f"The rider of {self.name} is too tired to pedal!"
    
    def get_movement_sound(self):
        """Bicycle movement sounds"""
        sounds = ["Pedaling rhythmically!", "Chain spinning smoothly", "Wheels rolling quietly"]
        return random.choice(sounds)
    
    def refuel(self):
        """Override refuel - for bicycles, this means the rider rests"""
        self.current_fuel = self.fuel_capacity
        return f"The rider of {self.name} has rested and is energized!"


class Train(Vehicle):
    """Train class - moves on tracks"""
    
    def __init__(self, name, speed, fuel_capacity, car_count):
        super().__init__(name, speed, fuel_capacity)
        self.car_count = car_count
        self.on_tracks = True
    
    def move(self):
        """Train-specific movement implementation"""
        if not self.on_tracks:
            return f"{self.name} is derailed and cannot move!"
        
        if self.current_fuel > 3:
            self.is_moving = True
            self.current_fuel -= 3
            self.distance_traveled += 30
            return f"🚂 {self.name} is chugging along the railway! {self.get_movement_sound()}"
        else:
            return f"{self.name} is out of fuel and cannot run!"
    
    def get_movement_sound(self):
        """Train movement sounds"""
        sounds = ["Choo choo! All aboard!", "Clickety-clack on the tracks", "Steam hissing, wheels turning"]
        return random.choice(sounds)
    
    def derail(self):
        """Train-specific emergency method"""
        self.on_tracks = False
        self.is_moving = False
        return f"⚠️ {self.name} has derailed!"


# Demonstration function showing polymorphism
def transportation_demo():
    """Function to demonstrate polymorphism with different vehicles"""
    print("=== TRANSPORTATION POLYMORPHISM DEMO ===\n")
    
    # Create different types of vehicles
    vehicles = [
        Car("Toyota Camry", 120, 50, 4),
        Plane("Boeing 747", 900, 200000, 42000),
        Boat("Ocean Breeze", 25, 100, "yacht"),
        Bicycle("Mountain Bike", 25),
        Train("Express Line", 200, 5000, 8)
    ]
    
    print("1. VEHICLE INTRODUCTIONS:")
    for vehicle in vehicles:
        print(vehicle.get_status())
    print()
    
    print("2. ALL VEHICLES MOVE (Polymorphism in Action!):")
    for vehicle in vehicles:
        print(vehicle.move())  # Same method name, different behavior!
    print()
    
    print("3. MOVE AGAIN TO SEE VARIETY:")
    for vehicle in vehicles:
        print(vehicle.move())
    print()
    
    print("4. VEHICLE-SPECIFIC ACTIONS:")
    car = vehicles[0]
    plane = vehicles[1] 
    boat = vehicles[2]
    train = vehicles[4]
    
    print(car.change_gear(3))
    print(plane.land())
    print(boat.drop_anchor())
    print(boat.move())  # Should fail because anchor is dropped
    print(boat.raise_anchor())
    print(train.derail())
    print(train.move())  # Should fail because derailed
    print()
    
    print("5. REFUEL ALL VEHICLES:")
    for vehicle in vehicles:
        print(vehicle.refuel())
    print()
    
    print("6. FINAL STATUS:")
    for vehicle in vehicles:
        print(vehicle.get_status())


# Function to show polymorphism with a list
def move_all_vehicles(vehicle_list):
    """Polymorphic function - works with any Vehicle subclass"""
    print("\n=== MOVING ALL VEHICLES POLYMORPHICALLY ===")
    for vehicle in vehicle_list:
        print(vehicle.move())  # Polymorphism: same method, different implementations


# Main execution
if __name__ == "__main__":
    transportation_demo()
    
    print("\n" + "="*50)
    print("BONUS: Polymorphism with Mixed Vehicle List")
    
    # Create a mixed list of vehicles
    mixed_fleet = [
        Car("Sports Car", 200, 60, 2),
        Plane("Fighter Jet", 1500, 1000, 50000),
        Bicycle("Racing Bike", 40)
    ]
    
    move_all_vehicles(mixed_fleet)
    
    print("\n" + "="*50)
    print("The power of polymorphism: One method name, many behaviors! 🚗✈️🚤🚴🚂")