"""
Course Number: ENGR 13100

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     9.1.2
    Author:         Oliver Remmler, oremmler@purdue.edu
    Section:        024
    Team:           07 

"""

def main():
    A = int(input("Enter a integer value for A: "))
    if (A < 22 or A > 324):
        A -= 16
    elif (A > 102 and A < 157):
        A *= -5
    elif (A >= 241):
        A -= 98
    elif (A >= 51 and A <= 87):
        A -= 37
    else:
        print("A is invalid")
        return
    
    print("A = ", A)


if __name__ == "__main__":
    main()
