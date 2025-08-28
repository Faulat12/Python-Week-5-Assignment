# Object-Oriented Programming Assignments 🚀

This repository contains two Python assignments that demonstrate core Object-Oriented Programming (OOP) concepts including inheritance, polymorphism, encapsulation, and abstraction.

## 📋 Assignment Overview

### Assignment 1: Superhero Class System 🦸‍♂️
**File:** 'ownclass.py'

A comprehensive class hierarchy featuring superheroes with inheritance and specialized abilities.

**Features:**
- **Base Superhero Class** with common attributes and methods
- **FlyingHero Class** - inherits from Superhero with flight capabilities
- **TechHero Class** - inherits from Superhero with gadget management
- Demonstrates all four OOP pillars

### Assignment 2: Vehicle Polymorphism System 🚗✈️🚤
**File:** `polymorphism.py`

A transportation system showcasing polymorphism through different vehicle types that all implement the same `move()` method differently.

**Features:**
- **Abstract Vehicle Base Class** using ABC module
- **5 Vehicle Types:** Car, Plane, Boat, Bicycle, Train
- Each vehicle moves uniquely while sharing common interface
- Perfect demonstration of polymorphism in action

## 🎯 Learning Objectives

Both assignments teach:

### 1. **Inheritance** 🧬
- Child classes inherit from parent classes
- `super()` method to call parent constructors
- Extending base functionality

### 2. **Polymorphism** 🔄
- Same method name, different implementations
- Method overriding in child classes
- Runtime method resolution

### 3. **Encapsulation** 🔒
- Private attributes (`__attribute`)
- Protected methods (`_method`)
- Data hiding and access control

### 4. **Abstraction** 📝
- Abstract base classes (Assignment 2)
- Interface definition
- Forcing implementation in subclasses

## 🚀 How to Run

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Running Assignment 1 (Superhero System)
```bash
python superhero_classes.py
```

**Expected Output:**
- Hero introductions and basic abilities
- Flying hero taking off and landing
- Tech hero using gadgets and upgrades
- Status displays showing polymorphism
- Class method demonstrating total hero count

### Running Assignment 2 (Vehicle System)
```bash
python vehicle_polymorphism.py
```

**Expected Output:**
- All vehicles moving with unique behaviors
- Vehicle-specific actions (gear changes, landing, anchoring)
- Polymorphic function calls
- Error handling (out of fuel, mechanical issues)

## 🔍 Key Code Examples

### Inheritance Example
```python
class FlyingHero(Superhero):  # Inherits from Superhero
    def __init__(self, name, real_name, power_level, primary_power, max_altitude):
        super().__init__(name, real_name, power_level, primary_power)  # Call parent constructor
        self.max_altitude = max_altitude  # Add new attribute
```

### Polymorphism Example
```python
# Same method name, different implementations
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    vehicle.move()  # Each vehicle moves differently!
```

### Encapsulation Example
```python
class Superhero:
    def __init__(self, name):
        self.__secret_weakness = "Unknown"  # Private attribute
    
    def _set_weakness(self, weakness):  # Protected method
        self.__secret_weakness = weakness
```

## 📚 Concepts Demonstrated

| Concept | Assignment 1 | Assignment 2 |
|---------|--------------|--------------|
| **Classes & Objects** | ✅ Superhero, FlyingHero, TechHero | ✅ Vehicle, Car, Plane, Boat, etc. |
| **Constructors** | ✅ Custom initialization for each hero type | ✅ Vehicle-specific initialization |
| **Inheritance** | ✅ Heroes inherit common abilities | ✅ All vehicles inherit from Vehicle |
| **Polymorphism** | ✅ Overridden methods behave differently | ✅ Each vehicle's move() is unique |
| **Encapsulation** | ✅ Private weakness attribute | ✅ Protected and private methods |
| **Abstraction** | ✅ Base class with common interface | ✅ Abstract base class with ABC |
| **Class Variables** | ✅ Total hero counter | ✅ N/A |
| **Method Overriding** | ✅ Flying heroes use less energy | ✅ Each vehicle implements move() |

## 🎮 Interactive Features

### Assignment 1 Features:
- Energy management system
- Hero status tracking
- Flying mechanics with altitude
- Gadget inventory system
- Power usage with intensity levels

### Assignment 2 Features:
- Fuel consumption simulation
- Vehicle-specific actions (gears, anchors, etc.)
- Random movement sounds for variety
- Error handling (out of fuel, mechanical failures)
- Distance tracking

## 🛠️ Extending the Code

### Adding New Heroes (Assignment 1):
```python
class MagicHero(Superhero):
    def __init__(self, name, real_name, power_level, primary_power, spell_count):
        super().__init__(name, real_name, power_level, primary_power)
        self.spell_count = spell_count
    
    def cast_spell(self, spell_name):
        # Custom magic hero behavior
        pass
```

### Adding New Vehicles (Assignment 2):
```python
class Submarine(Vehicle):
    def move(self):
        return f"🚇 {self.name} is diving underwater!"
    
    def get_movement_sound(self):
        return "Sonar pinging through the depths!"
```

