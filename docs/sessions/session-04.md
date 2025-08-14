# Session 4: Object Model & Class Fundamentals

**Week:** 4  
**Element:** ICTPRG430 Element 2.1  
**Duration:** 4 hours  
**Phase:** Object-Oriented Programming Theory

---

## Learning Objectives

By the end of this session, you will be able to:

- Understand fundamental OOP concepts: classes, objects, and object instantiation
- Implement states (using instance variables) and behaviors (using instance methods) for robot systems  
- Explain constructor design and instance variables
- Apply encapsulation principles in robotics contexts

---

## Session Overview

This session introduces the fundamental concepts of Object-Oriented Programming (OOP) through the lens of robotics applications. You'll learn why OOP is particularly valuable for robotics development and how to implement basic class structures.

## Pre-Session Preparation

!!! info "Required Reading"
    Review the following materials before class:
    
    - OOP programming fundamentals documentation
    - Class design principles guide
    - [Download: Basic Robot Class Starter](../downloads.md#week-4-object-model--class-fundamentals)

!!! tip "Setup Check"
    Ensure your Python development environment is configured:
    
    - Python 3.9+ installed and working
    - VS Code with Python extension
    - pytest framework installed

---

## 1. Why Object-Oriented Programming for Robotics?

Object-Oriented Programming was developed to manage the increasing complexity of large software systems. Robotics deals with highly intricate systems involving numerous sensors, actuators, and algorithms, making OOP an invaluable paradigm for developing robust and maintainable robot software.

### Key Advantages for Robotics

=== "Encapsulation"
    
    **Real-world Example:** E-puck robot motors
    
    You don't need to know the internal wiring or low-level data formats to control motors. OOP's encapsulation hides complexity behind clear interfaces like `set_speed()` methods.
    
    ```python
    # Clean interface - implementation details hidden
    motor = RobotMotor("left_wheel")
    motor.set_speed(0.5)  # Simple, clear method call
    ```

=== "Modularity"
    
    **Real-world Example:** Robot subsystems
    
    Instead of monolithic code, your robot software becomes a collection of interacting components - motors, sensors, navigation modules.
    
    ```python
    # Modular design
    navigation = NavigationSystem()
    sensors = ProximitySensors()
    motors = MotorController()
    ```

=== "Reusability"
    
    **Real-world Example:** Cross-platform compatibility
    
    Once you define a `Motor` class, it can be reused for every motor on your robot or even across different robot platforms.
    
    ```python
    # Reusable across different robots
    left_motor = Motor("left_wheel")
    right_motor = Motor("right_wheel")
    arm_motor = Motor("gripper")
    ```

=== "Flexibility"
    
    **Real-world Example:** Sensor polymorphism
    
    Different sensor types can respond to the same interface, making your code adaptable to hardware changes.
    
    ```python
    # All sensors respond to read_value()
    proximity_sensor.read_value()
    light_sensor.read_value()
    temperature_sensor.read_value()
    ```

---

## 2. Classes and Objects: The Foundation

### Understanding the Relationship

!!! abstract "Key Concepts"
    
    **Class:** A blueprint, template, or mold for creating objects
    
    - Like architectural plans for a building
    - Defines structure and capabilities
    - Uses PascalCase naming (e.g., `RobotLED`, `EPuckMotor`)
    
    **Object (Instance):** Individual "things" created from a class
    
    - Like actual buildings constructed from plans
    - Has unique state and identity  
    - Can have multiple objects from one class

### Practical Example: Robot LED System

Let's compare procedural vs object-oriented approaches:

=== "Procedural Approach"
    
    ```python
    # Global variable - problematic for multiple LEDs
    e_puck_led_is_on = False
    
    def turn_led_on():
        global e_puck_led_is_on
        e_puck_led_is_on = True
        print(f"LED is now ON: {e_puck_led_is_on}")
    
    def turn_led_off():
        global e_puck_led_is_on
        e_puck_led_is_on = False
        print(f"LED is now OFF: {e_puck_led_is_on}")
    ```
    
    **Problems:**
    - Global variables create management issues
    - Difficult to handle multiple LEDs
    - Data and functions are disconnected
    - Limited reusability

=== "Object-Oriented Approach"
    
    ```python
    class RobotLED:
        """Blueprint for robot LED objects."""
        
        def __init__(self, led_id: str):
            """Initialize LED with unique identifier."""
            self.led_id = led_id
            self.is_on = False
            print(f"LED '{self.led_id}' initialized (OFF)")
        
        def turn_on(self):
            """Turn the LED on."""
            self.is_on = True
            print(f"LED '{self.led_id}' is now ON")
        
        def turn_off(self):
            """Turn the LED off."""
            self.is_on = False
            print(f"LED '{self.led_id}' is now OFF")
    
    # Usage - multiple independent LEDs
    front_led = RobotLED("front")
    back_led = RobotLED("back")
    
    front_led.turn_on()   # Only affects front LED
    back_led.turn_off()   # Independent control
    ```

---

## 3. Object Instantiation Process

**Instantiation** creates new objects from a class blueprint. Understanding this process is crucial for effective OOP.

### The Two-Step Process

```python
# When you write this:
robot = EPuckRobot("Alpha_7", 98.5)

# Python internally does:
# 1. __new__() - Allocates memory for the object
# 2. __init__() - Initializes the object's state
```

### Behind the Scenes

1. **Memory Allocation (`__new__`)**: Python allocates memory space for the new object
2. **Initialization (`__init__`)**: Your constructor method sets up the object's initial state

---

## 4. Constructor Design and Instance Variables

The `__init__` method is your constructor - it defines how objects are created and initialized.

### Constructor Best Practices

```python
class EPuckRobot:
    """A blueprint for EPuck robot objects."""
    
    def __init__(self, robot_id: str, initial_battery_percentage: float):
        """
        Initialize a new EPuckRobot object.
        
        Args:
            robot_id (str): Unique identifier for the robot
            initial_battery_percentage (float): Battery level (0.0-100.0)
        """
        # Instance variables define object state
        self.robot_id = robot_id
        self.battery_percentage = initial_battery_percentage
        self.current_speed = 0.0
        self.is_moving = False
        
        print(f"EPuckRobot '{self.robot_id}' initialized with {self.battery_percentage}% battery")
```

### Instance Variables (State)

Instance variables store data unique to each object:

```python
# Each robot has its own independent state
robot_alpha = EPuckRobot("Alpha_7", 98.5)
robot_beta = EPuckRobot("Beta_12", 75.0)

# Modifying one doesn't affect the other
robot_alpha.current_speed = 0.5
robot_alpha.is_moving = True

print(f"Alpha speed: {robot_alpha.current_speed}")  # 0.5
print(f"Beta speed: {robot_beta.current_speed}")    # 0.0 (unchanged)
```

---

## 5. Instance Methods (Behavior)

Instance methods define what objects can do - their behaviors.

### Method Definition Rules

```python
class EPuckRobot:
    def __init__(self, robot_id: str, initial_battery_percentage: float):
        self.robot_id = robot_id
        self.battery_percentage = initial_battery_percentage
        self.current_speed = 0.0
        self.is_moving = False
    
    def move_forward(self, speed: float):
        """Start moving the robot forward at specified speed."""
        if 0.0 <= speed <= 1.0:
            self.current_speed = speed
            self.is_moving = True
            print(f"Robot {self.robot_id} moving forward at speed {speed}")
        else:
            print("Speed must be between 0.0 and 1.0")
    
    def stop(self):
        """Stop the robot movement."""
        self.current_speed = 0.0
        self.is_moving = False
        print(f"Robot {self.robot_id} stopped")
    
    def report_status(self):
        """Report current robot status."""
        status = f"Robot {self.robot_id}:\n"
        status += f"  Battery: {self.battery_percentage}%\n"
        status += f"  Speed: {self.current_speed}\n"
        status += f"  Moving: {self.is_moving}"
        return status
```

---

## In-Class Activities

### Activity 1: Basic Robot Class (30 minutes)

Create a `SimpleRobot` class with the following requirements:

!!! example "Implementation Task"
    ```python
    class SimpleRobot:
        # TODO: Implement constructor with name and battery_level
        # TODO: Add instance variables for position (x, y)
        # TODO: Implement move_to(x, y) method
        # TODO: Implement get_distance_from_origin() method
    ```

### Activity 2: Multiple Object Management (20 minutes)

Create and manage multiple robot instances:

!!! example "Multi-Robot Task"
    - Create 3 different robot objects
    - Give each robot different starting positions
    - Move them to different locations
    - Compare their distances from origin

### Activity 3: Encapsulation Challenge (25 minutes)

Implement proper encapsulation for a sensor class:

!!! example "Sensor Encapsulation"
    - Create a `ProximitySensor` class
    - Hide internal calibration data
    - Provide public methods for reading values
    - Add data validation

---

## Structured Out-of-Class Activities

### Required (3 hours)

**Task:** Implement basic Robot class hierarchy with proper encapsulation

1. **Robot Base Class (1 hour)**
   - Design and implement a base `Robot` class
   - Include essential attributes: ID, position, battery level
   - Implement basic movement and status methods

2. **Specialized Robot Classes (1.5 hours)**
   - Create `MobileRobot` subclass with wheel control
   - Create `SensorRobot` subclass with sensor arrays
   - Demonstrate proper inheritance usage

3. **Testing and Documentation (0.5 hour)**
   - Write unit tests for your classes
   - Document all methods with proper docstrings
   - Test object instantiation and method calls

### Submission Requirements

Upload to your portfolio:
- Python source files with complete implementations
- Test files demonstrating functionality  
- Documentation explaining design decisions
- Screenshots of successful test runs

---

## Key Takeaways

!!! success "Session Summary"
    - **OOP Benefits**: Encapsulation, modularity, reusability, and flexibility
    - **Classes vs Objects**: Blueprints vs instances
    - **Instantiation**: Memory allocation + initialization process
    - **Instance Variables**: Store unique object state
    - **Instance Methods**: Define object behaviors
    - **Constructor Design**: Proper `__init__` method implementation

---

## Next Session Preview

**Week 5: Advanced Class Features & Magic Methods**

- Python magic methods (`__str__`, `__repr__`, `__eq__`)
- Property decorators and getters/setters
- Class methods and static methods
- Operator overloading for custom classes

---

## Resources

### Downloads
- [:material-download: Class implementation examples](../downloads.md)
- [:material-download: Unit test templates](../downloads.md)
- [:material-download: Robot class starter code](../downloads.md)

### Further Reading
- Python Classes Documentation
- OOP Design Patterns
- Robotics Software Architecture

---

**Navigation:**  
[← Week 3](session-03.md) | [Learning Plan](../revised-lap.md) | [Week 5 →](session-05.md)