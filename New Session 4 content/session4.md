Session 4: Object Model & Class Fundamentals
This session will introduce you to the foundational concepts of Object-Oriented Programming (OOP) and how they are applied in the context of robotics, particularly with the GCTronic' e-puck robot.
1. Why Object-Oriented Programming (OOP) for Robotics?
Object-Oriented Programming was developed to manage the increasing complexity of large software systems. In robotics, where systems involve numerous sensors, actuators, algorithms, and complex interdependencies, OOP offers a powerful way to manage this complexity and build more robust and scalable robot applications.
Here's why OOP is essential for robot programming:
• Encapsulation: OOP allows you to bundle related data and code into a single unit called a class. Think of a robot's motor: you don't need to know its internal wiring; you just need an interface to set_speed() or turn_off(). This hides implementation details and defines clear boundaries within your robot's software, preventing unintended manipulation and allowing you to think at a higher level of abstraction.
• Modularity: Instead of one monolithic program, your robot's software can be composed of interacting "parts" or objects, each representing a distinct component like a motor, a distance sensor, or a navigation system. This makes the design, development, testing, and debugging of complex robot functionalities more manageable.
• Reusability: Once you define a class for a specific robot component, such as a Motor class or a DistanceSensor class for the e-puck, you can reuse that class for every motor on your robot, or even for similar components on different types of robots. This saves development time and reduces duplicate code.
• Flexibility (Polymorphism & Inheritance): As your robot's capabilities grow, OOP allows for flexible adaptation of existing code. For example, if you add different types of sensors to your e-puck (e.g., a camera sensor in addition to distance sensors), polymorphism allows them to respond to a common interface (e.g., a read_value() method), even if their internal workings differ. Inheritance lets you build specialized robot classes by acquiring behaviors and properties from a more general class, such as a WheeledRobot inheriting from a BaseRobot.
2. Classes, Objects, and Instantiation
Classes
In Python, classes serve as blueprints, templates, or molds from which you create objects. They describe the characteristics common to all objects of a given type. A class defines what an object will look like, including the data it will remember (its state) and the actions it can perform (its behaviors).
For example, you might define an EPuckRobot class that describes the general characteristics and behaviors common to all e-puck robots. By convention, class names in Python use PascalCase (e.g., LightSwitch, WizCoin, Robot).
Here's the simplest form of a Python class:
class MyFirstClass:
    pass
This simply tells Python that MyFirstClass is a class, even though it doesn't have any data or behaviors defined yet.
Objects / Instances
An object (also called an instance or instance object) is an individual "thing" created from a class. Just as many physical e-puck robots can be built from the same design specification, many EPuckRobot objects can be created from a single EPuckRobot class.
Objects are the values for a given type. For example, when you work with Python's built-in str class, my_string = 'Hello' creates a string object, which is an instance of the str class. Similarly, my_number = 42 creates an integer object, an instance of the int class.
Each object created from the same class is distinct and occupies its own space in memory.
Instantiation
Instantiation is the process of creating a new object from a class. When you call a class name followed by parentheses, like EPuckRobot(), you are performing instantiation.
The instantiation process typically involves two main steps:
1. The constructor (e.g., EPuckRobot()) first calls a static method, __new__, which is responsible for allocating memory for the new object.
2. After memory allocation, the constructor calls the special __init__ method. This method is often called the initializer or instance constructor, and its primary purpose is to initialize the instance variables the object needs in its initial state. You will define an __init__ method for nearly every class you create.
3. States and Behaviors in Robot Systems
Objects are fundamentally defined by their state and behavior.
State (Instance Variables)
State refers to the data associated with an individual class instance. For an e-puck robot, this could include its current position_x, position_y, its battery_level, or the distance_sensor_readings from its sensors.
Instance variables are used to track this state information. They are tied to a specific instance of a class. This means every object's state is distinct from other instances of the same type. For example, epuck_robot_A might be at (0, 0) with 90% battery, while epuck_robot_B is at (5, 10) with 75% battery. Each robot object maintains its own independent set of instance variables.
Instance variables are created and accessed using the self.variable_name syntax inside the class. They persist as long as the object exists. It is generally considered good practice to define and initialize all instance variables within the __init__ method to ensure they exist when other methods try to access them.
Behaviors (Instance Methods)
Behavior is what class instance objects can do – i.e., what methods an object can call. For an e-puck robot, behaviors might include move_forward(), read_sensors(), or report_status().
These behaviors are defined as instance methods within the class definition. Instance methods are shared by all class instances. This means both epuck_robot_A and epuck_robot_B can move_forward().
All instance methods must have a self parameter as their first parameter. This self parameter conventionally represents the object that invoked the method. When epuck_robot_A.move_forward() is called, self inside move_forward refers to epuck_robot_A. This allows the methods to access and manipulate the instance variables (state) of the specific object they are called on.
4. Procedural vs. OOP: A Robot Example
To illustrate the benefits of OOP, let's consider a simple robot scenario.
Procedural Example: A Basic Robot
In procedural programming, you might use global variables to store a robot's state and functions to perform actions. This works for simple programs but becomes difficult to manage for more complex systems or when dealing with multiple robots.
Imagine a very basic robot that has a name and a position (x, y).
# procedural_robot.py

# Global variables to represent the robot's state
robot_name = "Bot_A"
robot_pos_x = 0
robot_pos_y = 0
robot_battery = 100.0 # float data type
robot_is_moving = False # boolean data type

# Functions to represent robot behaviors
def move_robot(new_x, new_y):
    global robot_pos_x, robot_pos_y, robot_is_moving
    robot_pos_x = new_x
    robot_pos_y = new_y
    robot_is_moving = True
    print(f"{robot_name} moved to ({robot_pos_x}, {robot_pos_y}).")

def stop_robot():
    global robot_is_moving
    robot_is_moving = False
    print(f"{robot_name} stopped.")

def report_status():
    print(f"--- {robot_name} Status ---")
    print(f"Position: ({robot_pos_x}, {robot_pos_y})")
    print(f"Battery: {robot_battery}%")
    print(f"Moving: {robot_is_moving}")
    print("--------------------")

# Simulate robot actions
report_status()
move_robot(5, 10)
report_status()
stop_robot()
report_status()

# Problem: What if we want another robot? We'd need to duplicate all these global variables and functions!
# Or, if we try to reuse, it becomes confusing which robot's state is being manipulated.
# E.g., for a 'Bot_B', we'd need robot_name_B, robot_pos_x_B, etc. which is not scalable.
This procedural approach is manageable for a single, very simple robot. However, if we wanted to control multiple e-puck robots, we would quickly run into problems with managing global variables and duplicating code for each robot. This leads to programs that are harder to read, modify, and extend.
OOP Comparison: The  Class
Now, let's refactor this into an Object-Oriented approach using a class. This will allow us to create multiple, independent robot objects, each with its own state, while sharing the same behavior definitions.
# oop_epuck_robot.py

class EPuckRobot:
    """
    A class to represent a GCTronic' e-puck robot.
    It encapsulates the robot's state and behaviors.
    """

    def __init__(self, robot_id: str, initial_battery: float):
        """
        Initializes a new EPuckRobot object.

        This is the initializer method, called when an object is instantiated.
        It sets up the initial state (instance variables) of the robot.
        """
        self.robot_id = robot_id # string data type, uniquely identifies the robot
        self.battery_percentage = initial_battery # float data type, current battery level
        self.current_speed = 0.0 # float data type, initialized to 0.0
        self.position_x = 0 # int data type, initial X coordinate
        self.position_y = 0 # int data type, initial Y coordinate
        self.is_moving = False # boolean data type, initial movement status

        print(f"EPuck Robot '{self.robot_id}' initialized with {self.battery_percentage}% battery.")

    def set_speed(self, speed: float):
        """
        Sets the current speed of the robot.
        """
        if speed >= 0:
            self.current_speed = speed
            print(f"{self.robot_id}: Speed set to {self.current_speed} units/sec.")
            self.is_moving = True if speed > 0 else False
        else:
            print(f"{self.robot_id}: Speed cannot be negative.")

    def move_to(self, x: int, y: int):
        """
        Moves the robot to a specified (x, y) position.
        This is a behavior that modifies the robot's state.
        """
        print(f"{self.robot_id}: Moving from ({self.position_x}, {self.position_y}) to ({x}, {y}).")
        self.position_x = x # Accessing and modifying instance variable
        self.position_y = y # Accessing and modifying instance variable
        self.is_moving = True
        print(f"{self.robot_id}: Arrived at ({self.position_x}, {self.position_y}).")

    def stop(self):
        """
        Stops the robot's movement.
        """
        self.is_moving = False
        self.current_speed = 0.0
        print(f"{self.robot_id}: Stopped moving and speed reset to {self.current_speed}.")

    def perform_sensor_scan(self):
        """
        Simulates a sensor scan for the e-puck robot.
        (E-puck robots have distance sensors, for example.)
        """
        print(f"{self.robot_id}: Performing a sensor scan. Detected obstacles at various distances using its distance sensors.")
        # In a real scenario, this would return actual sensor data.
        # For simplicity, we just print a message.

    def report_status(self):
        """
        Reports the current status of the robot.
        """
        print(f"\n--- Status of EPuck Robot '{self.robot_id}' ---")
        print(f"Battery: {self.battery_percentage}%")
        print(f"Current Position: ({self.position_x}, {self.position_y})")
        print(f"Speed: {self.current_speed} units/sec")
        print(f"Is Moving: {self.is_moving}")
        print("--------------------------------------")

# --- Demonstrating Instantiation and Object Interaction ---

# Instantiating multiple EPuckRobot objects
epuck_alpha = EPuckRobot("Alpha-7", 95.5) # First object
epuck_beta = EPuckRobot("Beta-3", 70.0)   # Second object

# Demonstrate distinct states and shared behaviors
epuck_alpha.report_status()
epuck_beta.report_status()

# Interact with epuck_alpha
epuck_alpha.set_speed(10.0)
epuck_alpha.move_to(10, 5)
epuck_alpha.perform_sensor_scan()
epuck_alpha.report_status()

# Interact with epuck_beta (it maintains its own state)
epuck_beta.set_speed(5.0)
epuck_beta.move_to(2, 8)
epuck_beta.report_status()
epuck_beta.stop()
epuck_beta.report_status()

# Notice that changing epuck_alpha's state does not affect epuck_beta's state.
# Both objects share the same method definitions (e.g., set_speed, move_to),
# but operate on their own distinct instance variables.
In this OOP example, the EPuckRobot class serves as a single blueprint for all e-puck robots. When we instantiate epuck_alpha and epuck_beta, we create two independent objects, each with its own robot_id, battery_percentage, current_speed, position_x, position_y, and is_moving instance variables. They all use the same __init__ method for construction and the same instance methods (set_speed, move_to, perform_sensor_scan, report_status) to manipulate their own distinct states. This modularity and reusability are key advantages of OOP in robotics.