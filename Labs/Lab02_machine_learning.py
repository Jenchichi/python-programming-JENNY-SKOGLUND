# Datapoints
path = "Data/datapoints.txt" # Gå in i fil, open folder, välj den mapp som du vill öppna vs code med. (Python-programming-JENNY_SKOGLUND)
def open_text(path):
    with open(path, "r") as f:
        next(f)
        return f.readlines()
#print(repr(text))

def clean_data(data): # funktion som gör en lista av alla rader i Data/datapoints.txt
    clean_data = []
    for line in data:
        clean_line = line.strip().split(",")
        clean_data.append(clean_line)
    return clean_data
# print(clean_data(open_text(path)))

def separate_clean_data(data): # funktion som hämtar värderna från clean_data och appendar pichus x, y värde från label 0. samt pikachus x,y värde fråm label 1.
    pichu = []
    pikachu = []
    for row in data:
        width,hight,label = row
        if label == " 0":
            pichu.append((float(width), float(hight)))
        elif label == " 1":
            pikachu.append((float(width), float(hight)))
    return pichu, pikachu
#print(separate_clean_data(clean_data(open_text(path))))

path_test = "Data/testpoints.txt" 

def open_test(path_test):
    with open(path_test, "r") as t:
        return t.read()

def new_test_points(): # Gör en lista från testpoints som printas i terminalen.
    new_koordinats = []
    with open("Data/testpoints.txt", "r") as test_list:
        next(test_list)
        for line in test_list:
            koordinats = line.split('(')[1].split(')')[0].split(',')
            x = float(koordinats[0])
            y = float(koordinats[1])
            new_koordinats.append((x,y))
    return new_koordinats
print(new_test_points())

#distance = math.sqrt((pointx - pointy)**2 + (pointx - pointy)**2)

def knn_equation(pichu, pikachu, nearest_point):
    classifikation = []
    for point in nearest_point:
        minimum_distance = float('inf') # letar efter minsta distansen
        closest_point = None
        for data_point in pichu + pikachu:
            distance = math.sqrt((point[0] - float(data_point[0]))**2 + (point[1] - float(data_point[1]))**2)
            if distance < minimum_distance:
                minimum_distance = distance
                closest_point = data_point
        classify = 0 if closest_point in pichu else 1
        classifikation.append(classify)
    return classifikation
print(knn_equation(*separate_clean_data(clean_data(open_text(path))), new_test_points()))

import matplotlib.pyplot as plt
import numpy as np
import math

def plott_classify_pokemon(new_point, pichu, pikachu): # Klassificerar ny data
    plott_new_classify_pokemon = knn_equation(pichu, pikachu, new_point)

    plt.scatter(*zip(*pichu), color= 'hotpink', label= 'Pichu', marker='*')
    plt.scatter(*zip(*pikachu), color= 'purple', label = 'Pikachu', marker='*')
    plt.title("Classification for the nearest point")
    plt.xlabel("X = Lenght")
    plt.ylabel("Y = Height")

    pichu_new_class = [point for point, classifikation in zip(new_point, plott_new_classify_pokemon) if classifikation == 0]
    pikachu_new_class = [point for point, classifikation in zip(new_point, plott_new_classify_pokemon) if classifikation == 1]
    plt.scatter([point[0] for point in pichu_new_class], [point[1] for point in pichu_new_class], color= 'aqua', label= 'New Pichu Point', marker= "X")
    plt.scatter([point[0] for point in pikachu_new_class], [point[1] for point in pikachu_new_class], color= 'deepskyblue', label= 'New Pikachu Point', marker= "X")
    plt.legend()
    plt.show()
plott_classify_pokemon(new_test_points(), *separate_clean_data(clean_data(open_text(path))))
