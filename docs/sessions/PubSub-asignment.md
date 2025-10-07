# ROS2 Publisher/Subscriber Assignment

## Overview
In this assignment, you will create a ROS2 package with a publisher node that publishes your student ID and a random number. Then you'll verify it works by subscribing to the topic.

**Your Unique Student ID:** `STUD_[last 4 digits of your student number]`
Example: If your student number is 12345678, use `STUD_5678`

---

## Part 1: Create Your ROS2 Package

### 1.1 Navigate to your workspace and create a package
```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python student_publisher --dependencies rclpy std_msgs
```

### 1.2 Navigate to your package directory
```bash
cd student_publisher/student_publisher
```

---

## Part 2: Create the Publisher Node

### 2.1 Create a new Python file
```bash
nano student_id_publisher.py
```

### 2.2 Write your publisher code
Create a publisher that:
- Publishes to a topic called `/student_data`
- Uses `std_msgs/String` message type
- Publishes a message containing your student ID and a random integer (1-1000)
- Message format: `"STUD_XXXX:random_number"` (e.g., `"STUD_5678:742"`)
- Publishes every 1 second
- Generates a NEW random number each time it publishes

**Hints:**
- Use `import random` for random numbers
- Use `random.randint(1, 1000)` to generate random integers
- Follow the structure from the ROS2 Foxy tutorials on creating publishers
- Remember to import: `rclpy`, `Node` from `rclpy.node`, and `String` from `std_msgs.msg`

**📝 Submission Item 1:** Your complete `student_id_publisher.py` code file

---

## Part 3: Configure the Package

### 3.1 Edit setup.py
Add your node to the entry_points so ROS2 can run it:

```bash
cd ~/ros2_ws/src/student_publisher
nano setup.py
```

In the `entry_points` section, add:
```python
entry_points={
    'console_scripts': [
        'student_publisher = student_publisher.student_id_publisher:main',
    ],
},
```

### 3.2 Make your script executable
```bash
chmod +x ~/ros2_ws/src/student_publisher/student_publisher/student_id_publisher.py
```

---

## Part 4: Build and Source

### 4.1 Build your package
```bash
cd ~/ros2_ws
colcon build --packages-select student_publisher
```

```

**📝 Submission Item 2:** Screenshot of successful build output (showing "Finished <<< student_publisher")

---

## Part 5: Run and Test Your Publisher

### 5.1 Run your publisher node
```bash
ros2 run student_publisher student_publisher
```

You should see log messages showing your node is running.

**📝 Submission Item 3:** Screenshot showing your publisher running with any logger messages

### 5.2 In a NEW terminal, list the active topics
```bash
source ~/ros2_ws/install/setup.bash
ros2 topic list
```

You should see `/student_data` in the list.

**📝 Submission Item 4:** Screenshot of `ros2 topic list` output showing `/student_data`

### 5.3 Echo your topic to see the published messages
```bash
ros2 topic echo /student_data
```

Let it display at least 5 messages to show the random numbers are changing.

**📝 Submission Item 5:** Screenshot of `ros2 topic echo` showing at least 5 messages with your student ID and DIFFERENT random numbers

### 5.4 Check the publishing rate
```bash
ros2 topic hz /student_data
```

**📝 Submission Item 6:** Screenshot showing the average publishing rate (should be approximately 1 Hz)

---

## Part 6: Create a Subscriber 

Create a subscriber node called `student_id_subscriber.py` in the same package that:
- Subscribes to `/student_data`
- Prints out each message it receives
- Keeps a count of total messages received
- Calculates and prints the average of all random numbers received

**📝 Submission Item 7:** 
- Your `student_id_subscriber.py` code
- Updated `setup.py` with the subscriber entry point
- Screenshot showing both publisher and subscriber running in separate terminals
- Screenshot showing the subscriber's message count and average calculation

---

## Submission Checklist

Submit a single PDF containing:

1. ✅ Your `student_id_publisher.py` code (formatted and readable)
2. ✅ Screenshot of successful `colcon build`
3. ✅ Screenshot of publisher running
4. ✅ Screenshot of `ros2 topic list`
5. ✅ Screenshot of `ros2 topic echo` with 5+ messages showing different random numbers
6. ✅ Screenshot of `ros2 topic hz` output
7. ✅ Subscriber code, setup.py, and screenshots

**Important:** Your student ID must be visible in ALL screenshots showing message data. Each student will have different random numbers, ensuring unique submissions.

---


## Troubleshooting Tips

- **Build errors?** Check your `setup.py` entry_points syntax
- **Can't find node?** Make sure you sourced: `source ~/ros2_ws/install/setup.bash`
- **No messages appearing?** Check if your publisher is actually running
- **Topic not listed?** Verify your publisher created the topic with the exact name `/student_data`

## Resources
- ROS2 Foxy Documentation: https://docs.ros.org/en/foxy/
- Writing a simple publisher (Python): https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html