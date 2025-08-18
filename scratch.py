class EPuckRobot:
    """Enhanced EPuckRobot with string representations."""
    
    def __init__(self, robot_id: str, initial_battery_percentage: float):
        """Initialize a new EPuckRobot object."""
        self.robot_id = robot_id
        self.battery_percentage = initial_battery_percentage
        self.current_speed = 0.0
        self.is_moving = False
        print(f"EPuckRobot '{self.robot_id}' initialized with {self.battery_percentage}% battery")
    
    def __str__(self):
        """
        Return user-friendly string representation.
        
        Returns:
            str: Human-readable robot status
        """
        status = "MOVING" if self.is_moving else "STOPPED"
        return f"Robot {self.robot_id}: {self.battery_percentage}% battery, {status} (speed: {self.current_speed})"
    
    def __repr__(self):
        """
        Return developer-friendly string representation.
        
        Returns:
            str: Precise representation for debugging
        """
        return f"EPuckRobot(robot_id='{self.robot_id}', initial_battery_percentage={self.battery_percentage})"
    
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

r1 = EPuckRobot("trh", "dfdf")