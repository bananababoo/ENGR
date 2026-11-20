"""
Course Number: ENGR 13100

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     12.1.2
    Author:         Oliver Remmler, oremmler@purdue.edu
    Section:        024
    Team:           02 

"""
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.array([1,2,3,4,5])
    y= np.array([2.1, 3.9, 6.2, 7.8, 10.1])
    
    plt.scatter(x, y, color='black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.title('Plot of x vs y')
    
    m, b = np.polyfit(x, y, 1)
    
    y_pred = m * x + b
    
    SSE = np.sum((y - y_pred) ** 2)
    SST = np.sum((y - np.mean(y)) ** 2)
    
    plt.plot(x, y_pred, color='red')
    
    plt.title('Linear Regression Fit.')
    
    print(f"Slope (m): {m:.3f}")
    print(f"Intercept (b): {b:.3f}")
    print(f"Model: y = {m:.3f}x + {b:.3f}")
    print(f"r^2: {1 - SSE / SST:.3f}")
    
    
    
    plt.show()


if __name__ == "__main__":
    
    main()
