"""
Course Number: ENGR 13100

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     12.3.1
    Author:         Oliver Remmler, oremmler@purdue.edu
    Section:        024
    Team:           02

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('river_data.csv')
    
    print("--- WABASH RIVER AUTHORITY: Water Quality Dataset ---\n")
    
    print(df)
    print("\n--- SUMMARY STATISTICS ---\n")
    print(df.filter(items=['temp_c', 'do_mg_l',  'ph']).describe())
    print("\n--- LINEAR REGRESSION RESULTS ---\n")
    
    site_A = df[df['site'] == 'A']
    site_B = df[df['site'] == 'B']
    site_C = df[df['site'] == 'C']
    
    plt.scatter(site_A['temp_c'], site_A['do_mg_l'], color='blue',marker='o' ,  label='Site A')
    plt.scatter(site_B['temp_c'], site_B['do_mg_l'], color='green', marker='s', label='Site B')
    plt.scatter(site_C['temp_c'], site_C['do_mg_l'], color='red', marker='^', label='Site C')

    plt.xlabel('Temperature (°C)')
    plt.ylabel('Dissolved Oxygen (mg/L)')
    plt.title('Water Quality Data by Site')
    plt.legend()
    
    x = df['temp_c']
    y = df['do_mg_l']
    m, b = np.polyfit(x, y, 1)
    
    df_pred = m * x + b
    SSE = np.sum((y - df_pred) ** 2)
    SST = np.sum((y - np.mean(y)) ** 2)
    R_squared = 1 - SSE / SST
    
    print(f"Slope: {m:.3f} ml/L per deg C")
    print(f"Intercept: {b:.3f}")
    print(f"SSE: {SSE:.3f} (mg/L)^2")
    print(f"SST: {SST:.3f} (mg/L)^2")
    print(f"r^2: {R_squared:.3f}")
    
    plt.plot(x, df_pred, color='black', label='Linear Regression Fit')
    plt.text(24, 9.75, f'y = {m:.3f}x + {b:.3f}\n$r^2$ = {R_squared:.3f}', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))
    plt.show()

if __name__ == "__main__":
    main()
