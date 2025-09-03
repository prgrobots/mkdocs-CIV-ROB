# Session 6: Inheritance & Polymorphism

**Week:** 6  
**Element:** ICTPRG430 Element 2.1  
**Duration:** 4 hours  
**Phase:** Object-Oriented Programming Theory

---

## Session Introduction

In this session, you will learn two fundamental concepts of Object-Oriented Programming: **Inheritance** and **Polymorphism**. You'll understand how to create specialized robot classes that share common functionality and how different objects can respond to the same commands in their own unique ways.

## Learning Objectives

By the end of this session, you will be able to:

- **Create class hierarchies using inheritance**
- **Override methods in subclasses**
- **Use the `super()` function appropriately**
- **Implement polymorphic behavior**
- **Understand when to use inheritance vs composition**

---

## 1. Introduction to Inheritance

**Inheritance** allows a class to acquire attributes and methods from another class. This creates a parent-child relationship and promotes code reuse.

### Basic Inheritance Example

```python
class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.current_speed = 0
    
    def accelerate(self, amount):
        self.current_speed = min(self.current_speed + amount, self.max_speed)
        print(f"Speed: {self.current_speed}")

class Car(Vehicle):  # Car inherits from Vehicle
    def __init__(self, max_speed, doors):
        super().__init__(max_speed)  # Call parent constructor
        self.doors = doors
    
    def honk(self):
        print("Beep beep!")

# Usage
my_car = Car(120, 4)
my_car.accelerate(30)  # Inherited method
my_car.honk()          # Own method
```

### Robot Inheritance Example

```python
class Robot:
    def __init__(self, name):
        self.name = name
        self.battery = 100
        self.position = [0, 0]
    
    def move(self, direction):
        print(f"{self.name} moving {direction}")
        self.battery -= 5
    
    def check_battery(self):
        print(f"{self.name} battery: {self.battery}%")

class CleaningRobot(Robot):
    def __init__(self, name):
        super().__init__(name)  # Initialize parent
        self.dust_collected = 0
    
    def clean(self):
        print(f"{self.name} is cleaning")
        self.dust_collected += 10
        self.battery -= 10
    
    def move(self, direction):  # Override parent method
        super().move(direction)  # Call parent method
        print("Cleaning while moving")

# Usage
cleaner = CleaningRobot("RoboVac")
cleaner.move("forward")
cleaner.clean()
cleaner.check_battery()
```

---

## 2. Method Overriding and super()

Subclasses can **override** inherited methods to provide specialized behavior.

```python
class DeliveryRobot(Robot):
    def __init__(self, name):
        super().__init__(name)
        self.cargo = None
    
    def move(self, direction):
        if self.cargo:
            print(f"{self.name} carefully moving {direction} with cargo")
            self.battery -= 8  # Uses more battery when carrying cargo
        else:
            super().move(direction)  # Use parent's move method
    
    def pick_up(self, item):
        self.cargo = item
        print(f"{self.name} picked up {item}")
    
    def deliver(self):
        if self.cargo:
            print(f"{self.name} delivered {self.cargo}")
            self.cargo = None
        else:
            print("No cargo to deliver")
```

**Key Points:**

- Use `super()` to call the parent class methods
- You can override any inherited method
- `super()` is especially important in `__init__` methods

---

## 3. Polymorphism: Same Interface, Different Behavior

**Polymorphism** means "many forms" - different objects can respond to the same method call in their own way.

```python
class SecurityRobot(Robot):
    def __init__(self, name):
        super().__init__(name)
        self.alert_level = "Normal"
    
    def move(self, direction):
        super().move(direction)
        print("Scanning for threats while moving")
    
    def patrol(self):
        print(f"{self.name} is patrolling")

# Polymorphism in action
def operate_robots(robot_list):
    for robot in robot_list:
        robot.move("forward")  # Same method call, different behavior
        robot.check_battery()  # All robots have this method

# Create different robot types
robots = [
    CleaningRobot("Cleaner-1"),
    DeliveryRobot("Delivery-1"), 
    SecurityRobot("Guard-1")
]

# Operate all robots the same way (polymorphically)
operate_robots(robots)
```

### Practical Polymorphism Example

```python
class RobotManager:
    def __init__(self):
        self.robots = []
    
    def add_robot(self, robot):
        self.robots.append(robot)
        print(f"Added {robot.name} to fleet")
    
    def move_all_robots(self, direction):
        for robot in self.robots:
            robot.move(direction)  # Polymorphic method call
    
    def check_all_batteries(self):
        for robot in self.robots:
            robot.check_battery()

# Usage
manager = RobotManager()
manager.add_robot(CleaningRobot("Vacuum-Bot"))
manager.add_robot(DeliveryRobot("Mail-Bot"))

manager.move_all_robots("forward")  # Each robot moves differently
manager.check_all_batteries()
```

---

## 4. Composition: "Has-a" vs "Is-a" Relationships

Sometimes it's better to use **composition** (has-a) instead of **inheritance** (is-a).

```python
class Sensor:
    def __init__(self, sensor_type):
        self.sensor_type = sensor_type
    
    def read(self):
        return f"{self.sensor_type} reading: 42"

class Motor:
    def __init__(self, power):
        self.power = power
    
    def start(self):
        print(f"Motor started at {self.power}% power")

class SmartRobot:
    def __init__(self, name):
        self.name = name
        # Composition: Robot HAS-A sensor and motor
        self.sensor = Sensor("Distance")
        self.motor = Motor(75)
        self.battery = 100
    
    def scan_environment(self):
        reading = self.sensor.read()
        print(f"{self.name}: {reading}")
    
    def start_moving(self):
        self.motor.start()
        print(f"{self.name} is now moving")

smart_robot = SmartRobot("Explorer")
smart_robot.scan_environment()
smart_robot.start_moving()
```

**When to use composition:**

- When you need flexibility to change components
- When objects don't have a clear "is-a" relationship
- When you want to reuse components in multiple classes

---

## Hands-on Exercise: Build a Simple Robot Family

Create a robot hierarchy with the following requirements:

### Base Robot Class

```python
class Robot:
    def __init__(self, name, robot_type):
        # Initialize name, robot_type, battery (100), and position (0, 0)
        pass
    
    def move(self, distance):
        # Print movement message and reduce battery by distance
        pass
    
    def recharge(self):
        # Set battery back to 100
        pass
    
    def status(self):
        # Return robot status as string
        pass
```

### Specialized Robot Classes

Create two specialized robots that inherit from Robot:

1. **ServiceRobot** - can serve customers
2. **FactoryRobot** - can manufacture items

### Test Your Implementation

```python
# Create different robots
service_bot = ServiceRobot("Waiter-1")
factory_bot = FactoryRobot("Builder-1")

# Test polymorphic behavior
robots = [service_bot, factory_bot]
for robot in robots:
    robot.move(5)
    print(robot.status())
```

---

## Session Summary

### Key Concepts Learned

1. **Inheritance**: Creating specialized classes from base classes using "is-a" relationships
2. **Method Overriding**: Customizing inherited methods in subclasses
3. **super()**: Calling parent class methods safely
4. **Polymorphism**: Same interface, different implementations
5. **Composition**: Building objects with components using "has-a" relationships

### When to Use Each Concept

- **Inheritance**: When you have a clear "is-a" relationship (CleaningRobot IS-A Robot)
- **Polymorphism**: When different objects need to respond to same commands differently
- **Composition**: When you need flexibility and "has-a" relationships (Robot HAS-A Sensor)

### Real-World Applications

These concepts are used in:

- Robot Operating System (ROS) frameworks
- Game development (different character types)
- Web applications (different user types)
- Device drivers (different hardware types)

---

**Next Session Preview:** We'll explore error handling and debugging techniques to make your robot programs more robust and reliable.