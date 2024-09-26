# Datapoints
path = "Data/datapoints.txt" # Gå in i fil, open folder, välj den mapp som du vill öppna vs code med. (Python-programming-JENNY_SKOGLUND)

with open(path, "r") as f:
    text = f.read()

# print(repr(text))

import re

quotes = []

with open(path, "r") as f_read, open("Data/datapoints_new.txt", "w") as f_write:
    f_write.write("Pokemon list\n\n")
    for quote in f_read:
        #quote = quote.strip(" \n")
        #quote = re.sub(r" +", " ", quote)
        if quote != "":
            f_write.write(f"{quote}\n")
            #i += 1
# nedan sorterar listan i datapoints, för att få ut 0 = pichu och 1 = pikachu.
pichu = []
pikachu = []

with open("Data/datapoints_new.txt", "r") as list:
    for line in list:
        line_separate = line.strip()
        if line_separate:
            text_split = line_separate.split(",")

            try:
                width = round(float(text_split[0].strip()), 2)
                hight = round(float(text_split[1].strip()), 2)
                label = int(text_split[2].strip())

                if label == 0:
                    pichu.append([width, hight])
                elif label == 1:
                    pikachu.append([width, hight])
            except ValueError:
                print(f"Wrong in lines in the loop 'try' for float and int.")
                
import matplotlib.pyplot as plt
pichu_x = [x[0] for x in pichu]
pichu_y = [y[1] for y in pichu]
pikachu_x = [x[0] for x in pikachu]
pikachu_y = [y[1] for y in pikachu]

plt.title("Pikachu and Pichus width and hight. Pikachu as Purple, Pichu as pink")
plt.xlabel("Pikachu and Pichus X variable")
plt.ylabel("Pikachu and Pichus Y variable")
plt.scatter(pichu_x, pichu_y, marker="*", color="pink")
plt.scatter(pikachu_x, pikachu_y, marker="*", color="purple")
plt.show()

import math
from collections import Counter
import numpy as np

points = {'blue': pichu, 'orange': pikachu}

# Function to calculate Euclidean distance between two points
def euclidean_distance(p, q):
    return np.linalg.norm(np.array(p) - np.array(q))

def classify_and_plot(test_points, k=1):  # Set k=1 for nearest neighbor classification
    plt.title("Pikachu vs Pichu Classification")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
 
    # Calculate distances and classify for each test point
    for new_point in test_points:
        distance = [(euclidean_distance(p, new_point), color) for color in points for p in points[color]]
        nearest_point = [cls for cls in sorted(distance)[:k]]
        new_class = Counter(nearest_point).most_common(1)[0][0]
       
        # Plot the data points and the new point
        for color in points:
            for p in points[color]:
                plt.scatter(*p, color=[])
        plt.scatter(*new_point, color=new_class, marker='*', s=200)  # New point with larger size
        print(f"The new point {new_point} is classified as: {new_class}")
 
    plt.show()

# List of points (x, y)
test_points = [(25, 32), (24.2, 31.5), (22, 34), (20.5, 34)]

classify_and_plot(test_points, k=1)