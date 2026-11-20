"""
Course Number: ENGR 13100

Description:
    Given 2 inputted numbers, this program will output the sum, difference, product, quotient, and square root of the absolute value of each number.

Assignment Information:
    Assignment:     8.1.2
    Author:         Oliver Remmler, oremmler@purdue.edu
    Section:        024
    Team:           02
"""

def main():
    a = float(input("Enter a number between 1 and 10: "))
    b = float(input("Enter a number between 3 and 8: "))
    print("")
    print("--- Math Report ---")
    print(f"Number 1: {a:.2f}")
    print(f"Number 2: {b:.2f}")
    print(f"Sum: {a + b:.2f}")
    print(f"Difference: {a - b:.2f}")
    print(f"Product: {a * b:.2f}")
    print(f"Quotient: {a / b:.2f}")
    print(f"Power: {a ** b:.2f}")
    print(f"Sqrt(|Number 1|) : {abs(a) ** 0.5:.2f}")
    print(f"Sqrt(|Number 2|) : {abs(b) ** 0.5:.2f}")

if __name__ == "__main__":
    main()
