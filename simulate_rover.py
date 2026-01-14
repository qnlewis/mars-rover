import sys
import math

class Mars_Rover:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.orientation = 0
        
    def report_position(self):
        x = abs(self.x) if self.x == 0 else round (self.x, 2)
        y = abs(self.y) if self.y == 0 else round (self.y, 2)
        
        orientation = round(self.orientation, 2)
        print(f"I'm at ({x:.2f}, {y:.2f}) facing {orientation:.2f} degrees")

    def move_forward(self, distance):
        angle_rad = math.radians(self.orientation)
        self.x += distance * math.sin(angle_rad)
        self.y += distance * math.cos(angle_rad)
        self.x = round(self.x, 10)
        self.y = round(self.y, 10)

    def move_backward(self, distance):
        self.move_forward(-distance)

    def turn_clockwise(self, angle):
        self.orientation = (self.orientation + angle) % 360

    def turn_counterclockwise(self, angle):
        self.orientation = (self.orientation - angle) % 360

    def execute_instruction(self, instruction, instruction_num):
        instruction = instruction.strip().lower()
        if not instruction:
            return True
        print_instruction = f"(instruction {instruction_num})"
        
        try:
            parts = instruction.split()

            if len(parts) != 4:
                print(f"I've encountered an instruction I don't understand, aborting {print_instruction}")
                return False

            '''command = parts[0]
            value = parts[1]
            units = parts[2]
            direction = parts[3]'''
            command, value, units, direction = parts
            value = float(value)

            if command == "move" and units == "meters":
                if direction == "forward":
                    print(f"Moving {value} meters forward {print_instruction}")
                    self.move_forward(value)
                    
                elif direction == "backward":
                    print(f"Moving {value} meters backward {print_instruction}")
                    self.move_backward(value)
                    
                else:
                    print(f"I've encountered an instruction I don't understand, aborting {print_instruction}")
                    return False
                
            elif command == "turn" and units == "degrees":
                if direction == "clockwise":
                    print(f"Turning {value} degrees clockwise {print_instruction}")
                    self.turn_clockwise(value)
                    
                elif direction == "counterclockwise":
                    print(f"Turning {value} degrees counterclockwise {print_instruction}")
                    self.turn_counterclockwise(value)
                    
                else:
                    print(f"I've encountered an instruction I don't understand, aborting {print_instruction}")
                    return False
                
            else:
                print(f"I've encountered an instruction I don't understand, aborting {print_instruction}")
                return False

            self.report_position()
            return True
        
        except:
            print(f"I've encountered an instruction I don't understand, aborting {print_instruction}")
            return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python simulate_rover.py <instructions.txt>")
        sys.exit(1)

    rover = Mars_Rover()
    rover.report_position()

    try:
        with open(sys.argv[1], 'r') as f:
            instructions = f.readlines()
            
    except FileNotFoundError:
        print(f"Could not find instructions file: {sys.argv[1]}")
        sys.exit(1)
        
    except:
        print("Error reading instructions file")
        sys.exit(1)

    instruction_num = 1
    for instruction in instructions:
        if instruction.strip():
            if not rover.execute_instruction(instruction, instruction_num):
                break
            instruction_num += 1

if __name__ == "__main__":
    main()
