"""
Course Number: ENGR 13100

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     #.#.#
    Author:         Name, login@purdue.edu
    Section:        ###
    Team:           ## 

"""

import random
import time

PASSING_THRESHOLD = 50

def main():
    seed = int(input("Enter random seed (integer): "))
    device_name = input("Enter medical device name: ")
    prototype_id_number = int(input("Enter prototype ID number: "))
    last_name = input("Enter researcher's last name: ").capitalize() # Capitalize the first letter of the word
    title = input("Enter researcher's title: ").title() # Capitalize the first letter of each word in the title
    print("")
    print("==================================================")
    print("MEDICAL DEVICE PROTOTYPE TEST REPORT")
    print("==================================================")
    print("Device Name      :", device_name)
    print("Prototype ID     :", str(prototype_id_number))
    print("Researcher      :", title, last_name)
    print("Test Timestamp: " + time.strftime("%Y-%m-%d %H:%M:%S"))
    print("==================================================")
    
    random.seed(seed)
    random_values = [random.randint(5, 100) for _ in range(5)] # Fun list generation syntax
    average = sum(random_values) / len(random_values)
    sqrt_of_average = average ** 0.5 # same as to the power of 1/2
    passingTable = { True: "PASS", False: "FAIL" }
    passing = passingTable[sqrt_of_average >= PASSING_THRESHOLD] # Why are python ternaries like this what
    split_title_sequence = title.split(" ") # Split when we hit a space character
    
    print("")
    print("Test Values:", random_values)
    print(f"First Test Value: {random_values[0]}")
    print(f"Test Value Slice (3 values): {random_values[1:4]}")
    print("")
    print("Average of Test Values:", average)
    print(f"Square Root of Average: {sqrt_of_average:.2f}")
    print("Passing Threshold:", PASSING_THRESHOLD)
    print("Final Device Status:", passing)
    print(" ")
    print(f"Formatted Researcher Tag: {last_name}_{last_name}_")
    print(f"Split Researcher title sequence: {split_title_sequence}")


if __name__ == "__main__":
    main()

