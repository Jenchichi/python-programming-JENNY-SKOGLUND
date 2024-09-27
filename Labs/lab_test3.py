# Datapoints
path = "Data/datapoints.txt" # Gå in i fil, open folder, välj den mapp som du vill öppna vs code med. (Python-programming-JENNY_SKOGLUND)

with open(path, "r") as f:
    text = f.read()
# print(repr(text))

quotes = []

with open(path, "r") as f_read, open("Data/datapoints_new.txt", "w") as f_write:
    f_write.write("Pokemon list\n\n")
    for quote in f_read:
        if quote != "":
            f_write.write(f"{quote}\n")
            
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
                    pichu.append([width, hight, label])
                elif label == 1:
                    pikachu.append([width, hight, label])
            except ValueError:
                print(f"Wrong in lines in the loop 'try' for float and int.")
def making_float(file):
    points = []
    for line in open(file, "r"):
        try:
            map(float, line.split(","))
        except ValueError:
            print(f"file is not defined")
    return points

points = making_float(path)


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

# Test points

path_test = "Data/testpoints.txt" 

with open(path_test, "r") as f:
    test_points = f.read()

with open("Data/testpoints.txt", "r") as test_list:
    for line in test_list:
        line_separate_test = line.strip()
        if line_separate_test:
            text_split_test = line_separate_test.split(",")
        # print(text_split_test)

import math
import numpy as np
from collections import Counter
# Function to calculate Euclidean distance between two points
#def euclidean_distance(point1, point2):
#   return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# List of points (x, y)
# test_points = [(25, 32), (24.2, 31.5), (22, 34), (20.5, 34)]

# Loop to calculate distances between consecutive points

point1 = np.array((25, 24.2, 22, 20.5))
point2 = np.array((32, 31.5, 34, 34))
calculate_distance = np.linalg.norm(point1 - point2)
data_points = {'Pichu': pichu, 'Pikachu': pikachu}

def classify(test_points, k=1):
    for new_point in test_points:
        distance = [(calculate_distance(p, new_point), pokemon) for pokemon in points for p in points[pokemon]]
        new_class = set([cls for _, cls in sorted(distance)[:k]]), key=[cls for _, cls in sorted(distance)[:k]].count

        for pokemon in points:
            color = '#FFCC00' if pokemon == 'Pikachu' else '#00CCCC'
            for p in points[pokemon]:
                plt.scatter(*p, color=color, label=pokemon if pokemon not in plt.gca().get_legend_handles_labels()[1] else "")
        plt.scatter(*new_point, color='#FFAA00' if new_class == 'Pikachu' else '#00FFAA', marker='*', s=200, label=f'New Point: {new_class}')
       
        print(f"The new point {new_point} is classified as: {new_class}")
    plt.legend()
    plt.show()
classify(test_points, k=1)