import random

class IRSensor:
    """Enhanced infrared distance sensor with string representations."""

    def __init__(self, name: str):
        """
        Initialize the IR sensor with a position name.

        Args:
            name (str): Position identifier for the sensor
        """
        self.name = name
        self.last_reading = None  # Track the most recent reading
        print(f"IR Sensor '{self.name}' initialized")

    def __str__(self):
        """
        Return user-friendly string representation.

        Returns:
            str: Human-readable sensor status
        """
        if self.last_reading is None:
            return f"{self.name} Sensor: No readings taken"
        else:
            return f"{self.name} Sensor: {self.last_reading} cm"

    def __repr__(self):
        """
        Return developer-friendly string representation.

        Returns:
            str: Precise representation for debugging
        """
        return f"IRSensor(name='{self.name}')"

    def get_reading(self):
        """
        Simulate getting a distance measurement from the IR sensor.

        Returns:
            int: Distance measurement in centimeters (1-100)
        """
        self.last_reading = random.randint(1, 100)
        print(f"{self.name} sensor reading: {self.last_reading} cm")
        return self.last_reading

    def get_status(self):
        """
        Get detailed status information about the sensor.

        Returns:
            str: Detailed sensor status
        """
        if self.last_reading is None:
            return f"Sensor '{self.name}': Ready (no readings yet)"
        else:
            return f"Sensor '{self.name}': Active (last reading: {self.last_reading} cm)"

if __name__ == "__main__":
    # Create sensor instances
    sensors = [
        IRSensor("Front Left"),
        IRSensor("Front Center"),
        IRSensor("Front Right"),
        IRSensor("Back Left"),
        IRSensor("Back Right")
    ]

    print("\n=== Initial Sensor Status ===")
    for sensor in sensors:
        print(sensor)  # Uses __str__

    print("\n=== After Taking Readings ===")
    for sensor in sensors:
        sensor.get_reading()

    print("\n=== Updated Sensor Display ===")
    for sensor in sensors:
        print(sensor)  # Shows readings now

    print("\n=== Debugging View ===")
    print("Sensor list:", sensors)  # Uses __repr__ for each sensor

    print("\n=== Detailed Status ===")
    for sensor in sensors:
        print(sensor.get_status())