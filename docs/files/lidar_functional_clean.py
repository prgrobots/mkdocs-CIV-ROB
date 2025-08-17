# lidar_functional.py
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
