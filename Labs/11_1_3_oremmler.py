"""
Course Number: ENGR 13100

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     11.1.3
    Author:         Oliver Remmler, oremmler@purdue.edu
    Section:        024
    Team:           02 

"""

import matplotlib.pyplot as plt
import pandas as pd

def main():
    df = pd.read_csv("mild_steel_stress_strain.csv")
    
    print("--- Mild Steel Stress-Strain Data ---\n")
    print(df.head())
    
    stress_mean = df["stress_MPa"].mean()
    strain_mean = df["strain_percent"].mean()
    stress_median = df["stress_MPa"].median()
    strain_median = df["strain_percent"].median()
    stress_std = df["stress_MPa"].std()
    strain_std = df["strain_percent"].std()
    stress_min = df["stress_MPa"].min()
    strain_min = df["strain_percent"].min()
    stress_max = df["stress_MPa"].max()
    strain_max = df["strain_percent"].max()
    
    print("")
    print(f"Mean stress: {stress_mean:.2f} MPa")
    print(f"Median stress: {stress_median:.2f} MPa")
    print(f"Standard deviation of stress: {stress_std:.2f} MPa")
    print(f"Min stress: {stress_min:.2f} MPa")
    print(f"Max stress: {stress_max:.2f} MPa")
    print("")
    
    print(f"Mean strain: {strain_mean:.2f} %")
    print(f"Median strain: {strain_median:.2f} %")
    print(f"Standard deviation of strain: {strain_std:.2f} %")
    print(f"Min strain: {strain_min:.2f} %")
    print(f"Max strain: {strain_max:.2f} %")
    
    plt.plot(df["strain_percent"], df["stress_MPa"], color="blue", linewidth=2, marker="o")
    plt.xlabel("Strain (%)", labelpad=10, fontsize=12)
    plt.ylabel("Stress (MPa)", labelpad=10, fontsize=12)
    plt.title("Mild Steel Stress-Strain Curve", pad=15, fontsize=14)
    plt.xlim(0, 45)
    plt.ylim(0, 500)
    plt.grid(True)
    plt.minorticks_on()
    plt.show()

if __name__ == "__main__":
    main()
