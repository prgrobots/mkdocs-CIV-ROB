"""
Robot Class Starter Template
ICTPRG430 - Week 4: Object Model & Class Fundamentals

This template provides a starting point for creating robot classes.
Students should complete the implementation following OOP principles.
"""

class Robot:
    """
    A basic robot class template.
    
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
        # TODO: Initialize instance variables
        pass
    
    def move_to(self, x: int, y: int):
        """
        Move the robot to specified coordinates.
        
        Args:
            x (int): Target x coordinate
            y (int): Target y coordinate
        """
        # TODO: Implement movement logic
        pass
    
    def get_status(self) -> str:
        """
        Get current robot status information.
        
        Returns:
            str: Formatted status string
        """
        # TODO: Return status information
        pass
    
    def charge_battery(self, amount: float):
        """
        Charge the robot's battery.
        
        Args:
            amount (float): Amount to charge (percentage)
        """
        # TODO: Implement battery charging logic
        pass


class EPuckRobot(Robot):
    """
    E-puck robot specific implementation.
    
    Extends the base Robot class with e-puck specific features.
    """
    
    def __init__(self, robot_id: str, initial_battery: float):
        """
        Initialize an E-puck robot.
        
        Args:
            robot_id (str): Unique identifier for the robot
            initial_battery (float): Starting battery level (0.0-100.0)
        """
        super().__init__(robot_id, initial_battery)
        # TODO: Add e-puck specific initialization
        
    def read_sensors(self) -> list:
        """
        Read proximity sensor values.
        
        Returns:
            list: List of sensor readings
        """
        # TODO: Implement sensor reading logic
        pass
    
    def set_led_state(self, led_id: int, state: bool):
        """
        Control individual LEDs on the e-puck.
        
        Args:
            led_id (int): LED identifier (0-7)
            state (bool): True to turn on, False to turn off
        """
        # TODO: Implement LED control logic
        pass


if __name__ == "__main__":
    # Example usage
    robot = EPuckRobot("EPuck_001", 95.5)
    print(f"Created robot: {robot.get_status()}")
