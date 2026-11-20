"""
Course Number: ENGR 13100

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     10.3.1
    Author:         Oliver Remmler, oremmler@purdue.edu
    Section:        024
    Team:           07 

"""


def main():
    errors = 0
    messages = input("Enter items separated by commas (no spaces): ").split(",")
    for msg in messages:
        if msg == "normal":
            print("Moving item to standard bin")
        elif msg == "fragile":
            print("Handling fragile item with care")
        elif msg == "heavy":
            print("Activating lift assist for heavy item")
        elif msg == "error":
            print("ALERT: Item error detected - robot needs help!")
            errors += 1
            if(errors >= 3):
                print("ALERT: Too many errors - sending robot to inspection")
                break

if __name__ == "__main__":
    main()
