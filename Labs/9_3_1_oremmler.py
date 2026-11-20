"""
Course Number: ENGR 13100

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     9.3.1
    Author:         Oliver Remmler, oremmler@purdue.edu
    Section:        024
    Team:           07 

"""

import math

# Gravitational Constant g
G = 6.6743e-11

def main():
    print("Select a tool:")
    print("  1) Irrigation System Check")
    print("  2) Escape Velocity Calculator")
    choice = int(input("Enter choice (1 or 2): "))
    if(choice == 1):
        irrigation_system()
    elif(choice == 2):
        escape_velocity()
    else:
        print("Invalid choice.")
        main()
    


def irrigation_system():
    soil_moisture = int(input("Enter soil moisture (%, 0-60): "))
    if(soil_moisture < 0 or soil_moisture > 60):
        print("Invalid soil moisture value.")
        return;
    forecasted_rain = int(input("Enter forecasted rain (mm, 0-50): "))
    if(forecasted_rain < 0 or forecasted_rain > 50):
        print("Invalid forecasted rain value.")
        return
    low_pressure: bool = isYes(input("Is the system experiencing low pressure? (yes/no): "))
    maintenance_needed: bool = isYes(input("Is maintenance needed? (yes/no): "))
    
    print("")
    
    if(maintenance_needed):
        print("DO NOT IRRIGATE - maintenance required.")
    elif(low_pressure):
        print("DO NOT IRRIGATE - low pressure condition.")
    elif(soil_moisture < 10):
        print("DELAY - significant rainfall expected.")
    elif(soil_moisture < 20):
        print("RUN FULL")
    elif(soil_moisture < 25):
        print("RUN REDUCED")
    else:
        print("SKIP - soil moisture is adequate.")

def escape_velocity():
    density = float(input("Enter the density of the planet (kg/m^3): "))
    radius = float(input("Enter the radius of the planet (m): "))
    
    volume = calculateVolume(radius)
    mass = calculateMass(density, volume)
    escape_velocity = calculate_escape_velocity(mass, radius)
    radius_km = meters_to_kilometers(radius)
    
    print("")
    print("---Calculator Results---")
    print(f"Planet radius: {radius_km:.2f} km")
    print(f"Escape velocity: {escape_velocity:.2f} m/s")
    
    
def calculateVolume(radius):
    return (4/3) * math.pi * radius ** 3

def calculateMass(density, volume):
    return density * volume

def meters_to_kilometers(meters):
    return meters / 1000.0

def calculate_escape_velocity(mass, radius):
    """Calculates the escape velocity in meters

    Args:
        mass (float): The mass in kg
        radius (float): The radius in meters

    Returns:
        float: The escape velocity in m/s
    """
    return math.sqrt(2 * G * mass / radius)

def isYes(answer):
    if(answer.lower() == "yes"):
        return True
    elif(answer.lower() == "no"):
        return False
    else:
        print("Invalid Input, expected yes or no.")
        exit(1) # Invalid Input

if __name__ == "__main__":
    main()
