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

import csv
import time
import numpy as np
import pandas as pd
        
def main():
    CSV_PATH = "metal_mass_volume.csv"
    with open(CSV_PATH, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
        print("Original Data - For Loop:")
        print(f"\n{rows}")
        
        start = time.perf_counter()
        density_loop = [float(row['Mass_g']) / float(row['Volume_cm3']) for row in rows]
        end = time.perf_counter()
        execution_time = end - start
        
        print(f"\nDensity (Loop): \n\n{[round(d, 1) for d in density_loop]}") # round to 1 decimal
        print(f"\nLoop Execution Time: {execution_time:.6f}\n\n")
        
    pandas_df = pd.read_csv("metal_mass_volume.csv")
            
    print("Original Data - Numpy:\n")
    print(f"{pandas_df}\n")
    
    mass_np = pandas_df['Mass_g'].to_numpy().copy()
    volume_np = pandas_df['Volume_cm3'].to_numpy().copy()
    start = time.perf_counter()
    density_np = mass_np / volume_np
    end = time.perf_counter()
    execution_time = end - start
    
    print(f"Density (Numpy): \n\n{np.round(density_np, 1)}")
    print(f"\nNumpy Execution Time: {execution_time:.6f}\n\n")
    
    pandas_df = pd.read_csv("metal_mass_volume.csv")
    print("Original Data - Pandas:\n")
    print(f"{pandas_df}\n")
    
    start = time.perf_counter()
    pandas_df["Density_g/cm3"] = round(pandas_df['Mass_g'] / pandas_df['Volume_cm3'], 1)
    end = time.perf_counter()
    execution_time = end - start
    
    print(f"Density (Pandas): \n\n{pandas_df}")
    print(f"\npandas Execution Time: {execution_time:.6f}\n")
        
    print("Equivalence Checks:\n")
    print(f"type(mass_np): {type(mass_np)}")
    print(f"mass.dtype(): {mass_np.dtype}")
    print(f"type(pandas_df['Mass_g'].values): {type(pandas_df['Mass_g'].values)}\n")
    print(f"mass arrays equal (Numpy vs pandas): {np.array_equal(mass_np, pandas_df['Mass_g'].values)}")
    print(f"dtype match (pandas vs Numpy): {mass_np.dtype == pandas_df['Mass_g'].values.dtype}")
    print(f"density values allclose (Numpy vs pandas): {np.allclose(density_np, pandas_df['Density_g/cm3'].values)}\n")
    
    print("Sorted by Density (Pandas):\n")
    pandas_df.sort_values(by="Density_g/cm3", inplace=True)
    print(f"{pandas_df}\n")
    print("Sorted Density (Numpy array):\n")
    density_np_sorted = np.sort(density_np)
    print(f"{np.round(density_np_sorted, 1)}\n")
    
    mass_np[0] = np.nan
    pandas_df.loc[0, 'Mass_g'] = np.nan
    print("Density with Missing Mass (NumPy):\n")
    density_np_missing = mass_np / volume_np
    print(f"{density_np_missing}\n")
    print("Density with Missing Mass (pandas):\n")
    pandas_df["Density_g/cm3"] = pandas_df['Mass_g'] / pandas_df['Volume_cm3']
    print(f"{pandas_df}\n")
    
    print(f"NaN detected via pandas .isna(): {pandas_df['Density_g/cm3'].isna().any()}")

if __name__ == "__main__":
    main()
