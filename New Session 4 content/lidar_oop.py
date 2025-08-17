# lidar_oop_start.py
import random

# TO DO: Create a Lidar class
#   - __init__: store number of measurements
#   - method: get_measurement() → returns random int between 1 and 1200
#   - method: scan() → returns list of measurements

# TO DO: Create an instance of the Lidar class

# TO DO: Call scan() and print results


# lidar_oop_finished.py
import random

class Lidar:
    def __init__(self, num_measurements=36):
        self.num_measurements = num_measurements

    def get_measurement(self):
        """Simulates a single LIDAR measurement."""
        return random.randint(1, 1200)

    def scan(self):
        """Performs a full scan and returns a list of measurements."""
        return [self.get_measurement() for _ in range(self.num_measurements)]

if __name__ == "__main__":
    lidar = Lidar()
    readings = lidar.scan()
    print("LIDAR Scan (OOP):")
    print(readings)
