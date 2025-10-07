# Session 11: ROS2 Fundamentals & Publisher/Subscriber Development

**Week:** 11 **Element:** ICTPRG439 Element 2.3 **Duration:** 4 hours **Phase:** ROS2 Core Concepts

---

## Session Introduction

This session provides **hands-on experience with ROS2 fundamentals** through a combination of live robot demonstration, interactive tutorials, and practical development. You'll observe ROS concepts operating on the physical ARI robot, then immediately apply that knowledge by working through ROS2 CLI tools and building your own publisher/subscriber nodes.

The session begins with a **30-minute ARI robot demonstration** showing real-world ROS architecture in action. While ARI operates on ROS1, the fundamental concepts of **nodes and topics** remain consistent with ROS2, providing valuable context for understanding distributed robotics systems.

You'll then engage in **hands-on ROS2 tutorials** using turtlesim to master essential CLI tools for inspecting and interacting with nodes and topics. The session concludes with **developing your own ROS2 package** that implements publisher/subscriber communication patterns.

## Learning Objectives

By the end of this session, you will have:

- **Observed ROS architecture** operating on a physical robot platform
- **Mastered ROS2 CLI tools** for node and topic inspection
- **Understood publisher/subscriber** communication patterns
- **Created a ROS2 package** with custom publisher and subscriber nodes
- **Published and received messages** using standard ROS2 message types
- **Debugged ROS2 communication** using command-line inspection tools

---

## Session Structure

1. **ARI Robot Demonstration (30 mins)** - Live system architecture observation
2. **ROS2 Fundamentals Tutorial (90 mins)** - Interactive CLI tools and concepts
3. **Break (15 mins)**
4. **Publisher/Subscriber Development (120 mins)** - Building custom ROS2 nodes

---

## Part 1: ARI Robot Live Demonstration (30 mins)

### 1.1 ARI Platform Overview

**Hardware Capabilities:**

- **Mobile Base** - Differential drive navigation platform
- **Torso & Arms** - Upper body manipulation capabilities  
- **Head & Sensors** - Vision system, microphones, speakers
- **Computing** - Onboard computer running ROS1 Noetic

!!! warning "Robot Safety Requirements"
    - **Maintain safe distance** from robot during operation
    - **Emergency stop awareness** - Know location of e-stop button
    - **No sudden movements** near robot workspace
    - **Follow instructor directions** during demonstration

### 1.2 Live Demonstration Focus

**What We Will Observe:**

**System Architecture:**

- Multiple nodes running simultaneously
- Topic-based communication between components
- Real-time data flow from sensors to actuators

**Node Identification:**

- **Sensor nodes** - Camera drivers, laser scanners, IMU
- **Processing nodes** - Navigation, localization, perception
- **Control nodes** - Motor controllers, base controller, gripper

**Topic Communication:**

- `/camera/image_raw` - Image data streaming
- `/scan` - Laser range measurements
- `/cmd_vel` - Velocity commands for movement
- `/joint_states` - Robot joint positions

**Key Observations:**
```bash
# Commands demonstrated (ROS1 syntax shown for reference)
rosnode list              # View all running nodes
rostopic list             # See all active topics
rostopic echo /scan       # Monitor sensor data
rostopic info /cmd_vel    # Inspect topic details
```

### 1.3 ROS1 vs ROS2 Conceptual Consistency

!!! info "Understanding Across ROS Versions"
    While ARI uses ROS1, the **fundamental concepts transfer directly to ROS2**:
    
    - **Nodes** - Independent computation units (same concept)
    - **Topics** - Asynchronous message passing (same pattern)
    - **Messages** - Typed data structures (similar types)
    - **CLI tools** - Inspection and debugging (analogous commands)
    
    The syntax differs slightly, but the **architecture and thinking remain consistent**.

**Comparison Table:**

| Concept | ROS1 Command | ROS2 Command |
|---------|--------------|--------------|
| List nodes | `rosnode list` | `ros2 node list` |
| List topics | `rostopic list` | `ros2 topic list` |
| Echo topic | `rostopic echo /topic` | `ros2 topic echo /topic` |
| Topic info | `rostopic info /topic` | `ros2 topic info /topic` |

---

## Part 2: ROS2 Fundamentals Tutorial (90 mins)

### 2.1 Environment Setup

**Verify ROS2 Installation:**
```bash
# Source ROS2 environment (add to ~/.bashrc for persistence)
source /opt/ros/foxy/setup.bash

# Verify installation
ros2 --version

# Set unique domain ID to avoid cross-talk with other students
export ROS_DOMAIN_ID=<your_student_number_last_two_digits>
echo $ROS_DOMAIN_ID
```

!!! tip "ROS_DOMAIN_ID Best Practice"
    Each student should use a **unique domain ID** (0-232) to prevent interference. Use the last two digits of your student ID for consistency.

### 2.2 Understanding ROS2 Nodes

**Tutorial Reference:** [Understanding ROS2 Nodes](https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)

**Core Concept:**
Nodes are the **fundamental building blocks** of ROS2 applications. Each node is an independent process responsible for a specific task (sensor reading, motor control, path planning, etc.).

**Hands-On Exploration:**

```bash
# Terminal 1: Start turtlesim node
ros2 run turtlesim turtlesim_node

# Terminal 2: Start teleop node
ros2 run turtlesim turtle_teleop_key

# Terminal 3: Inspect the system
ros2 node list
ros2 node info /turtlesim
```

**What You'll See:**
- `/turtlesim` node handles turtle simulation and visualization
- `/teleop_turtle` node captures keyboard input
- Nodes communicate via topics (visible in node info output)

**Key Commands:**
```bash
ros2 node list              # Show all active nodes
ros2 node info /node_name   # Detailed node information
ros2 run package node       # Run a node from a package
```

**Practical Exercise:**
1. Launch turtlesim and teleop nodes
2. Use `ros2 node list` to identify running nodes
3. Use `ros2 node info /turtlesim` to see its topics and services
4. Drive the turtle and observe real-time behavior

### 2.3 Understanding ROS2 Topics

**Tutorial Reference:** [Understanding ROS2 Topics](https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)

**Core Concept:**
Topics implement the **publisher/subscriber pattern** - nodes publish data to topics, other nodes subscribe to receive that data. This enables **asynchronous, many-to-many communication**.

**Hands-On Exploration:**

```bash
# Discover topics
ros2 topic list
ros2 topic list -t  # Include message types

# Inspect specific topic
ros2 topic info /turtle1/cmd_vel
ros2 topic echo /turtle1/cmd_vel  # Watch live data

# Check message structure
ros2 interface show geometry_msgs/msg/Twist
```

**Publishing from Command Line:**
```bash
# Publish once to move turtle
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist \
  "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"

# Publish continuously at 1 Hz
ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist \
  "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```

**Key Commands:**
```bash
ros2 topic list                    # List all topics
ros2 topic list -t                 # List with message types
ros2 topic echo /topic_name        # Monitor topic data
ros2 topic info /topic_name        # Show publishers/subscribers
ros2 topic hz /topic_name          # Measure publishing rate
ros2 topic pub /topic_name type    # Publish to topic
ros2 interface show msg_type       # Show message structure
```

**Practical Exercise:**
1. Identify the topic used for turtle movement (`/turtle1/cmd_vel`)
2. Echo the topic while driving with teleop to see message structure
3. Publish your own commands to move the turtle programmatically
4. Check the publishing frequency with `ros2 topic hz`
5. Examine different message types used in turtlesim

### 2.4 RQT Graph Visualization

**Launch RQT Graph:**
```bash
rqt_graph
```

**What You'll Observe:**
- Visual representation of node connections
- Topics linking publishers to subscribers
- System architecture at a glance

**Practical Activity:**
- Launch turtlesim and teleop
- Open rqt_graph
- Observe how nodes connect through topics
- Identify publisher/subscriber relationships

---

## Part 3: Publisher/Subscriber Development (120 mins)

### 3.1 Creating Your First ROS2 Package

**Package Structure:**
A ROS2 package contains your code, configuration files, and dependency information organized in a standard structure.

**Create Package with Dependencies:**
```bash
# Navigate to workspace src directory
cd ~/ros2_ws/src

# Create Python package with required dependencies
ros2 pkg create --build-type ament_python my_publisher_subscriber \
  --dependencies rclpy std_msgs

# Examine created structure
cd my_publisher_subscriber
ls -la
```

**Package Structure Explained:**
```
my_publisher_subscriber/
├── package.xml           # Package metadata and dependencies
├── setup.py             # Python package configuration
├── setup.cfg            # Python installation configuration
├── resource/            # Package marker files
├── test/                # Unit tests
└── my_publisher_subscriber/  # Python module directory
    └── __init__.py
```

### 3.2 Building Your Workspace

**Colcon Build System:**
```bash
# Build from workspace root
cd ~/ros2_ws
colcon build --packages-select my_publisher_subscriber

# Source the workspace overlay
source install/local_setup.bash

# Verify package is recognized
ros2 pkg list | grep my_publisher_subscriber
```

!!! info "Source vs Install Space"
    - **Source space** (`src/`) contains your source code
    - **Build space** (`build/`) contains intermediate build files
    - **Install space** (`install/`) contains built executables
    - You normally always **source install/local_setup.bash** before running nodes, the VM has this sourced automaticly in the .bashrc

### 3.3 Understanding the Assignment

**Assignment Overview:**
You will create a **publisher node** that publishes your student ID and a random number to a topic, then verify it works by subscribing to that topic.

**Reference:** See the [ROS2 Publisher/Subscriber Assignment](docs/sessions/PubSub-asignment.md) page for complete details.

**Key Requirements:**
- Create a publisher node in Python
- Publish to a custom topic
- Use appropriate ROS2 message types
- Verify communication using CLI tools
- Document your implementation

**Skills Applied:**
- Creating ROS2 Python nodes
- Implementing publisher patterns
- Working with ROS2 message types
- Using colcon build system
- Testing with ros2 topic commands

### 3.4 Development Workflow

**Iterative Development Process:**

1. **Write Code** - Implement publisher node logic
2. **Build Package** - Use colcon to compile
3. **Source Workspace** - Update environment
4. **Test Node** - Run and verify behavior
5. **Debug Issues** - Use CLI tools to troubleshoot
6. **Refine Code** - Improve and iterate

**Essential Development Commands:**
```bash
# Build specific package
colcon build --packages-select my_publisher_subscriber

# Build with symbolic links (for faster Python iteration)
colcon build --symlink-install --packages-select my_publisher_subscriber

# Source environment
source install/local_setup.bash

# Run your node
ros2 run my_publisher_subscriber publisher_node

# Debug in another terminal
ros2 topic list
ros2 topic echo /your_topic_name
ros2 node info /your_node_name
```

### 3.5 Testing and Verification

**Verification Steps:**

**1. Check Node is Running:**
```bash
ros2 node list
# Should show your publisher node
```

**2. Verify Topic Publication:**
```bash
ros2 topic list
# Should show your custom topic

ros2 topic echo /your_topic_name
# Should display published messages
```

**3. Inspect Topic Details:**
```bash
ros2 topic info /your_topic_name
# Shows publisher count and message type

ros2 topic hz /your_topic_name
# Measures publishing frequency
```

**4. Examine Message Structure:**
```bash
ros2 interface show std_msgs/msg/String
# Shows message field definitions
```

**Common Issues and Solutions:**

| Issue | Likely Cause | Solution |
|-------|--------------|----------|
| Node not in `ros2 node list` | Entry point not configured | Check `setup.py` entry_points |
| Topic not appearing | Node not publishing | Verify publisher initialization |
| No messages received | Wrong topic name | Check topic spelling/namespacing |
| Build errors | Missing dependencies | Update `package.xml` |

---

## Session Summary

This session provided comprehensive hands-on experience with ROS2 fundamentals:

1. **Observed real-world ROS architecture** through ARI robot demonstration
2. **Mastered essential CLI tools** for inspecting nodes and topics
3. **Understood publisher/subscriber patterns** through turtlesim examples
4. **Created custom ROS2 package** using proper workspace structure
5. **Developed and tested** publisher nodes using standard workflows

**Key Takeaways:**
- **Nodes** are independent processes that perform specific tasks
- **Topics** enable asynchronous communication between nodes
- **CLI tools** are essential for debugging and system inspection
- **Colcon build system** manages ROS2 package compilation
- **Publisher/subscriber pattern** is fundamental to ROS2 architecture

---

## Preparation for Next Session

For Session 12 on advanced ROS2 concepts:

- **Complete the publisher/subscriber assignment** (see assignment page)
- **Experiment with different publishing rates** in your node
- **Try creating a subscriber node** to receive your published messages
- **Review ROS2 services and parameters** documentation for next week
- **Practice using rqt_graph** to visualize your system architecture

---

!!! question "Question 1: What is the fundamental difference between nodes and topics in ROS2?"
        
    ??? tip "Click to reveal answer"
        **Answer**: 
        
        **Nodes** are independent processes that execute computation (like programs), while **topics** are named channels through which nodes communicate by publishing and subscribing to messages. Nodes are the "actors" that do work, topics are the "communication pathways" between them.

---

!!! question "Question 2: Why do we use `ros2 topic echo` during development and debugging?"
        
    ??? tip "Click to reveal answer"
        **Answer**: 
        
        `ros2 topic echo` allows us to **monitor live data** being published to a topic, which is essential for:
        - Verifying that publishers are working correctly
        - Checking message content and format
        - Debugging communication issues
        - Understanding data flow in the system
        It's like having a "window" into the data stream without writing a subscriber node.

---

!!! question "Question 3: What happens if you forget to source your workspace after building?"
        
    ??? tip "Click to reveal answer"
        **Answer**: 
        
        If you don't source the workspace (`source install/local_setup.bash`), ROS2 won't know about your newly built packages or nodes. When you try to run them with `ros2 run`, you'll get an error saying the package or executable cannot be found. Sourcing updates your environment variables to include your workspace's install directory.

---

**Navigation:** ← Week 10 | Learning Plan | Week 12 →