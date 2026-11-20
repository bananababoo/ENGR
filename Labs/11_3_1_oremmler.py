"""
Course Number: ENGR 13100

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     11.3.1
    Author:         Oliver Remmler, oremmler@purdue.edu
    Section:        024
    Team:           02 

"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    elev_df = pd.read_csv("data_NYC_elevators.csv")
    print("NYC Elevator Data (First 10 rows):")
    elev_df_copy = elev_df.copy()
    #elev_df_copy.drop(columns=["ZIP_CODE", "LATITUDE (decimal degrees)"], inplace=True)
    print(elev_df_copy.head(10).to_string())
    print("\nColumn names:")
    print(elev_df.columns.astype(object))
    print(f"\nShape (rows, columns): {elev_df.shape}\n")
    
    elev_df.rename(columns={"LATITUDE (decimal degrees)": "Latitude", "LONGITUDE (decimal degrees)": "Longitude"}, inplace=True)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(elev_df["Longitude"], elev_df["Latitude"], color="blue", s=10, marker="o")
    plt.xlabel("Longitude")
    plt.axis('equal')
    plt.ylabel("Latitude")
    plt.title("NYC Elevator Locations")
    #plt.savefig("11_3_1_nyc_elevator_map_oremmler.png")
    #plt.show()

    
    filtered_df = elev_df[(elev_df["Longitude"] > -75.5) & (elev_df["Latitude"] > 40.3)]
    
    plt.figure(figsize=(8, 10))
    plt.scatter(filtered_df["Longitude"], filtered_df["Latitude"], color="green", s=1, marker="o")
    plt.xlabel("Longitude")
    plt.axis('equal')
    plt.ylabel("Latitude")
    plt.title("NYC Revised Elevator Locations")
    #plt.savefig("11_3_1_nyc_elevator_map_revised_oremmler.png")
    #plt.show()
    
    man_elev_df = elev_df[elev_df["Borough"] == "Manhattan"]
    
    print("First 5 rows (Manhattan)")
    print(man_elev_df.head(5).to_string())
    print(f"\nThe number of elevators in manhattan is {len(man_elev_df)}.")
    
    plt.figure(figsize=(10, 8))
    plt.scatter(man_elev_df["Longitude"], man_elev_df["Latitude"], color="purple", s=1, marker="o")
    plt.xlabel("Longitude")
    plt.axis('equal')
    plt.ylabel("Latitude")
    plt.title("Manhattan Elevator Locations")
    #plt.savefig("11_3_1_manhattan_elevator_map_oremmler.png")
    #plt.show()



if __name__ == "__main__":
    main()
