# lidar_oop.py
import random

class Lidar:
    """Simulates a LIDAR sensor with configurable parameters."""
    
    def __init__(self, num_measurements=36):
        """Initialize LIDAR with specified number of measurements."""
        self.num_measurements = num_measurements
        print(f"LIDAR initialized with {self.num_measurements} measurement points")

    def get_measurement(self):
        """Simulates a single LIDAR measurement."""
        return random.randint(1, 1200)  # Distance in cm

    def scan(self):
        """Performs a full scan and returns a list of measurements."""
        readings = []
        for _ in range(self.num_measurements):
            readings.append(self.get_measurement())
        return readings
    
    def get_status(self):
        """Returns the current status of the LIDAR sensor."""
        return f"LIDAR Status: {self.num_measurements} measurement points configured"

if __name__ == "__main__":
    # Create LIDAR instance
    lidar = Lidar()
    print(lidar.get_status())
    
    # Perform scan
    readings = lidar.scan()
    print("LIDAR Scan (OOP):")
    print(f"Collected {len(readings)} measurements")
    print(f"Sample readings: {readings[:5]}...")  # Show first 5 readings
