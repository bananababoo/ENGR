"""
Course Number: ENGR 13100

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     9.1.3
    Author:         Oliver Remmler, oremmler@purdue.edu
    Section:        024
    Team:           07 

"""

def calc_power(voltage, resistance):
    return voltage ** 2 / resistance

def main():
    V = float(input("Enter voltage (V): "))
    R = float(input("Enter resistance (ohms): "))
    P = calc_power(V, R)
    print(f"Calculated power: {P:.2f} w")
    """Write your code here (and delete this line)."""


if __name__ == "__main__":
    main()
