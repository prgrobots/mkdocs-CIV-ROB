# lidar_functional_start.py
import random

# TO DO: Create a function that generates a single LIDAR measurement

# TO DO: Create a function that performs a full 36-measurement scan

# TO DO: Call the scan function and print the results


# lidar_functional_finished.py
import random

def get_measurement():
    """Simulates one LIDAR measurement."""
    return random.randint(1, 1200)

def scan_lidar(num_measurements=36):
    """Performs a LIDAR scan and returns a list of measurements."""
    return [get_measurement() for _ in range(num_measurements)]

if __name__ == "__main__":
    readings = scan_lidar()
    print("LIDAR Scan (Functional):")
    print(readings)
