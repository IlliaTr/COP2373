# Hypotenuse of a right angle calculator

import math

def get_user_input():    
    # Prompts the user to input the nearest angle in degrees and the length of the adjacent side.
    angle_degrees = float(input("Enter the nearest angle in degrees: "))
    adjacent_length = float(input("Enter the length of the adjacent side: "))
    
    # Returns a tuple containing the angle in degrees and the length of the adjacent side.
    return angle_degrees, adjacent_length

def calculate_hypotenuse(angle_degrees, adjacent_length):
    # Calculates the hypotenuse length of a right triangle
    angle_radians = math.radians(angle_degrees)
    hypotenuse_length = adjacent_length / math.cos(angle_radians)

    # Return the length of the hypotenuse.
    return hypotenuse_length

def main():
    # Main function to execute the program logic.
    angle_degrees, adjacent_length = get_user_input()
    hypotenuse_length = calculate_hypotenuse(angle_degrees, adjacent_length)
    print(f"\nThe length of the hypotenuse is: {hypotenuse_length}")

if __name__ == "__main__":
    main()
