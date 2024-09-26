import math
# Testdata: (25,32), (24.2,31.5), (22,34), (20.5,34)

point1 = [25, 32]
point2 = [24.2, 31.5]
point3 = [22, 34]
point4 = [20.5, 34]

distance = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
distance = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

import matplotlib.pyplot as plt

plt.title("The classification for the nearest point")
plt.scatter(pichu_x, pichu_y, marker="*", color="pink")
plt.scatter(pikachu_x, pikachu_y, marker="*", color="purple")
plt.scatter(point1, point2, marker="X", color="green")
plt.show()

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Test points

path_test = "Data/testpoints.txt" 

with open(path_test, "r") as f:
    test_points = f.read()

with open("Data/testpoints.txt", "r") as test_list:
    for line in test_list:
        line_separate_test = line.strip()
        if line_separate_test:
            text_split_test = line_separate_test.split(",")
        print(text_split_test)