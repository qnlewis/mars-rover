#🚀 Mars Rover Simulator
A Python-based simulation engine that navigates a rover across a planetary surface using vector mathematics. Unlike standard grid-based implementations, this solver handles arbitrary angles and floating-point coordinates.

###🎯 The Problem
The challenge was to build a control system that translates textual commands into physical movement. The system needed to parse input files, execute movements with high precision, and maintain the rover's state (position and orientation) while handling invalid or corrupt instructions gracefully.

###🛠 Tech Stack
* **Language:** Python 3.12
* **Testing:** unittest framework
* **Core Concepts:** Trigonometry (Vectors), File I/O, Command Pattern, Exception Handling

###✨ Key Features
Vector-Based Movement: Utilizes math.sin and math.cos to calculate movement, allowing the rover to move in any direction (e.g., 45° or 30°), not just the four cardinal directions.

* **Robust Parsing:** Reads instruction files (instructions.txt) and safely skips corrupt lines without crashing the simulation.

* **Precision Tracking:** Maintains coordinates as floating-point numbers to ensure accuracy over long travel distances.

###💡 Challenges & Learnings
* **Trigonometric Conversion:** Python's math functions expect radians, but the inputs are in degrees. I implemented a conversion layer to ensure the rover's orientation updates correctly.

* **Input Sanitization:** The simulator had to handle edge cases like mixed-case commands ("MOve") and invalid numeric values. I implemented a try-except block within the execution loop to report errors per line while keeping the system running.

###💻 How to Run
1. Clone the repository:
   
Bash:
git clone https://github.com/your-username/mars-rover.git
cd mars-rover

2. Run the simulation with an instruction file:
   
Bash:
python3 simulate_rover.py instructions_1.txt

Output:
I'm at (10.00, 0.00) facing 90.00 degrees

3. Run the test suite:

Bash
python3 -m unittest discover tests

