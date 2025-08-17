# lidar_procedural.py
import random

# Procedural: all logic inline
measurements = []
for _ in range(36):
    measurement = random.randint(1, 1200)  # cm range
    measurements.append(measurement)

print("LIDAR Scan (Procedural):")
print(measurements)
