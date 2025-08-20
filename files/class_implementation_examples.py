"""
Class Implementation Examples
ICTPRG430 - Week 4: Object Model & Class Fundamentals

This file contains complete implementations of the classes discussed in Session 4,
serving as reference examples for students.
"""

import random
import math


class IRSensor:
    """
    Complete implementation of the IR Sensor class from Session 4 hands-on exercise.
    
    This class simulates an infrared distance sensor commonly found on robots
    like the e-puck.
    """
    
    def __init__(self, name: str):
        """
        Initialize the IR sensor with a position name.
        
        Args:
            name (str): The position/name of the sensor (e.g., "Front Left")
        """
        self.name = name
        self.calibration_offset = random.uniform(-2, 2)  # Simulate sensor variance
        print(f"IR Sensor '{self.name}' initialized")
    
    def get_reading(self) -> int:
        """
        Simulate getting a distance measurement from the IR sensor.
        
        Parameters:
            None
        
        Returns:
            int: Distance measurement in centimeters (1–100).
        """
        # Simulate reading with some calibration offset
        base_reading = random.randint(1, 100)
        adjusted_reading = max(1, min(100, int(base_reading + self.calibration_offset)))
        
        print(f"{self.name} sensor reading: {adjusted_reading} cm")
        return adjusted_reading
    
    def calibrate(self, reference_distance: int):
        """
        Calibrate the sensor against a known distance.
        
        Args:
            reference_distance (int): Known distance in cm for calibration
        """
        current_reading = random.randint(1, 100)  # Simulate current reading
        self.calibration_offset = reference_distance - current_reading
        print(f"Sensor '{self.name}' calibrated. Offset: {self.calibration_offset:.2f}")


class Lidar:
    """
    Complete implementation of the LIDAR class from Session 4 live demonstration.
    
    This class simulates a LIDAR sensor with configurable parameters for
    robotics applications.
    """
    
    def __init__(self, num_measurements: int = 36):
        """
        Initialize LIDAR with specified number of measurements.
        
        Args:
            num_measurements (int): Number of measurements per scan (default: 36)
        """
        self.num_measurements = num_measurements
        self.min_range = 1      # Minimum detection range in cm
        self.max_range = 1200   # Maximum detection range in cm
        self.scan_count = 0     # Track number of scans performed
        
        print(f"LIDAR initialized with {self.num_measurements} measurement points")

    def get_measurement(self) -> int:
        """
        Simulates a single LIDAR measurement.
        
        Returns:
            int: Distance measurement in centimeters
        """
        # Simulate realistic LIDAR behavior with some noise
        return random.randint(self.min_range, self.max_range)

    def scan(self) -> list:
        """
        Performs a full scan and returns a list of measurements.
        
        Returns:
            list: List of distance measurements in centimeters
        """
        readings = []
        for i in range(self.num_measurements):
            # Add slight variation based on angle for realism
            angle_factor = math.sin(i * 2 * math.pi / self.num_measurements) * 50
            base_measurement = self.get_measurement()
            adjusted_measurement = max(self.min_range, 
                                     min(self.max_range, 
                                         int(base_measurement + angle_factor)))
            readings.append(adjusted_measurement)
        
        self.scan_count += 1
        return readings
    
    def scan_filtered(self, start: int = 0, end: int = None) -> list:
        """
        Return scan results between given indices.
        
        Args:
            start (int): Starting index (default: 0)
            end (int): Ending index (default: num_measurements)
            
        Returns:
            list: Filtered scan results
        """
        if end is None:
            end = self.num_measurements
            
        full_scan = self.scan()
        return full_scan[start:end]
    
    def get_status(self) -> str:
        """
        Returns the current status of the LIDAR sensor.
        
        Returns:
            str: Status information string
        """
        return (f"LIDAR Status: {self.num_measurements} measurement points configured, "
                f"{self.scan_count} scans completed, "
                f"Range: {self.min_range}-{self.max_range} cm")


class Robot:
    """
    Complete implementation of the Robot class template.
    
    This class serves as a foundation for creating robot objects with
    common attributes and behaviors.
    """
    
    def __init__(self, robot_id: str, initial_battery: float):
        """
        Initialize a new Robot object.
        
        Args:
            robot_id (str): Unique identifier for the robot
            initial_battery (float): Starting battery level (0.0-100.0)
        """
        self.robot_id = robot_id
        self.battery_level = max(0.0, min(100.0, initial_battery))  # Clamp to valid range
        self.position_x = 0
        self.position_y = 0
        self.is_moving = False
        self.total_distance = 0.0
        
        print(f"Robot '{self.robot_id}' initialized with {self.battery_level}% battery")
    
    def move_to(self, x: int, y: int):
        """
        Move the robot to specified coordinates.
        
        Args:
            x (int): Target x coordinate
            y (int): Target y coordinate
        """
        if self.battery_level <= 0:
            print(f"Robot {self.robot_id}: Cannot move - battery depleted!")
            return
        
        # Calculate distance and battery consumption
        distance = math.sqrt((x - self.position_x)**2 + (y - self.position_y)**2)
        battery_cost = distance * 0.1  # 0.1% battery per unit distance
        
        if battery_cost > self.battery_level:
            print(f"Robot {self.robot_id}: Insufficient battery for this move!")
            return
        
        # Perform the move
        print(f"Robot {self.robot_id}: Moving from ({self.position_x}, {self.position_y}) to ({x}, {y})")
        self.position_x = x
        self.position_y = y
        self.battery_level -= battery_cost
        self.total_distance += distance
        self.is_moving = False  # Movement complete
        
        print(f"Robot {self.robot_id}: Arrived at ({x}, {y}). Battery: {self.battery_level:.1f}%")
    
    def get_status(self) -> str:
        """
        Get current robot status information.
        
        Returns:
            str: Formatted status string
        """
        status = f"=== Robot {self.robot_id} Status ===\n"
        status += f"Position: ({self.position_x}, {self.position_y})\n"
        status += f"Battery: {self.battery_level:.1f}%\n"
        status += f"Moving: {self.is_moving}\n"
        status += f"Total Distance: {self.total_distance:.1f} units\n"
        status += "=" * (len(f"Robot {self.robot_id} Status") + 6)
        return status
    
    def charge_battery(self, amount: float):
        """
        Charge the robot's battery.
        
        Args:
            amount (float): Amount to charge (percentage)
        """
        old_level = self.battery_level
        self.battery_level = min(100.0, self.battery_level + amount)
        actual_charge = self.battery_level - old_level
        
        print(f"Robot {self.robot_id}: Charged {actual_charge:.1f}% "
              f"(Battery: {old_level:.1f}% → {self.battery_level:.1f}%)")
    
    def get_distance_from_origin(self) -> float:
        """
        Calculate distance from origin (0, 0).
        
        Returns:
            float: Distance from origin
        """
        return math.sqrt(self.position_x**2 + self.position_y**2)


class EPuckRobot(Robot):
    """
    E-puck robot specific implementation.
    
    Extends the base Robot class with e-puck specific features like
    LED control and sensor management.
    """
    
    def __init__(self, robot_id: str, initial_battery: float):
        """
        Initialize an E-puck robot.
        
        Args:
            robot_id (str): Unique identifier for the robot
            initial_battery (float): Starting battery level (0.0-100.0)
        """
        super().__init__(robot_id, initial_battery)
        
        # E-puck specific attributes
        self.led_states = [False] * 8  # 8 LEDs on e-puck
        self.sensors = self._initialize_sensors()
        self.wheel_speeds = {"left": 0.0, "right": 0.0}
        
        print(f"E-puck robot '{self.robot_id}' ready with {len(self.sensors)} sensors")
    
    def _initialize_sensors(self) -> list:
        """
        Initialize the proximity sensors for the e-puck.
        
        Returns:
            list: List of IRSensor objects
        """
        sensor_positions = [
            "Front Right", "Front Right Side", "Right Side", "Back Right",
            "Back Left", "Left Side", "Front Left Side", "Front Left"
        ]
        return [IRSensor(position) for position in sensor_positions]
    
    def read_sensors(self) -> list:
        """
        Read proximity sensor values.
        
        Returns:
            list: List of sensor readings
        """
        readings = []
        print(f"Robot {self.robot_id}: Reading proximity sensors...")
        
        for i, sensor in enumerate(self.sensors):
            reading = sensor.get_reading()
            readings.append(reading)
        
        return readings
    
    def set_led_state(self, led_id: int, state: bool):
        """
        Control individual LEDs on the e-puck.
        
        Args:
            led_id (int): LED identifier (0-7)
            state (bool): True to turn on, False to turn off
        """
        if 0 <= led_id < 8:
            self.led_states[led_id] = state
            status = "ON" if state else "OFF"
            print(f"Robot {self.robot_id}: LED {led_id} turned {status}")
        else:
            print(f"Robot {self.robot_id}: Invalid LED ID {led_id}. Must be 0-7.")
    
    def set_all_leds(self, state: bool):
        """
        Turn all LEDs on or off.
        
        Args:
            state (bool): True to turn all on, False to turn all off
        """
        for i in range(8):
            self.led_states[i] = state
        
        status = "ON" if state else "OFF"
        print(f"Robot {self.robot_id}: All LEDs turned {status}")
    
    def set_wheel_speeds(self, left_speed: float, right_speed: float):
        """
        Set the wheel speeds for differential drive.
        
        Args:
            left_speed (float): Left wheel speed (-1.0 to 1.0)
            right_speed (float): Right wheel speed (-1.0 to 1.0)
        """
        self.wheel_speeds["left"] = max(-1.0, min(1.0, left_speed))
        self.wheel_speeds["right"] = max(-1.0, min(1.0, right_speed))
        
        self.is_moving = (abs(left_speed) > 0 or abs(right_speed) > 0)
        
        print(f"Robot {self.robot_id}: Wheel speeds set - "
              f"Left: {self.wheel_speeds['left']:.2f}, Right: {self.wheel_speeds['right']:.2f}")
    
    def get_status(self) -> str:
        """
        Get comprehensive status including e-puck specific information.
        
        Returns:
            str: Detailed status string
        """
        base_status = super().get_status()
        
        # Add e-puck specific status
        led_status = "".join(["●" if led else "○" for led in self.led_states])
        epuck_info = f"\nLED States: {led_status}\n"
        epuck_info += f"Wheel Speeds: L={self.wheel_speeds['left']:.2f}, R={self.wheel_speeds['right']:.2f}\n"
        epuck_info += f"Sensors: {len(self.sensors)} proximity sensors available"
        
        # Insert e-puck info before the closing line
        status_lines = base_status.split('\n')
        status_lines.insert(-1, epuck_info)
        
        return '\n'.join(status_lines)


def demonstrate_all_classes():
    """
    Demonstration function showing all classes in action.
    """
    print("=== Session 4 Class Implementation Examples ===\n")
    
    # 1. Demonstrate IRSensor
    print("1. IR Sensor Demonstration:")
    sensors = []
    sensor_names = ["Front Left", "Front Center", "Front Right", "Back Left", "Back Right"]
    
    for name in sensor_names:
        sensor = IRSensor(name)
        sensors.append(sensor)
    
    print("\nSensor readings:")
    for sensor in sensors:
        sensor.get_reading()
    
    print("\n" + "-" * 50)
    
    # 2. Demonstrate LIDAR
    print("\n2. LIDAR Demonstration:")
    lidar = Lidar(12)  # Smaller scan for demo
    print(lidar.get_status())
    
    readings = lidar.scan()
    print(f"Scan complete. Sample readings: {readings[:5]}...")
    
    # Demonstrate filtering
    front_arc = lidar.scan_filtered(2, 8)
    print(f"Front arc readings: {front_arc}")
    
    print("\n" + "-" * 50)
    
    # 3. Demonstrate Robot classes
    print("\n3. Robot Class Demonstration:")
    
    # Basic robot
    basic_robot = Robot("R001", 85.0)
    print(basic_robot.get_status())
    
    basic_robot.move_to(10, 15)
    basic_robot.charge_battery(5.0)
    print(f"Distance from origin: {basic_robot.get_distance_from_origin():.2f}")
    
    print("\n" + "-" * 30)
    
    # E-puck robot
    print("\n4. E-puck Robot Demonstration:")
    epuck = EPuckRobot("EPuck_Alpha", 90.0)
    
    # LED control
    epuck.set_led_state(0, True)
    epuck.set_led_state(2, True)
    epuck.set_all_leds(False)
    
    # Sensor reading
    sensor_data = epuck.read_sensors()
    print(f"Sensor readings summary: Min={min(sensor_data)}, Max={max(sensor_data)}")
    
    # Movement
    epuck.set_wheel_speeds(0.5, 0.3)
    epuck.move_to(5, 8)
    
    print("\nFinal E-puck status:")
    print(epuck.get_status())


if __name__ == "__main__":
    demonstrate_all_classes()
