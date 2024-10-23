# Gå in i fil, open folder, välj mapp: (Python-programming-JENNY_SKOGLUND)
# Datapoints
path = "Data/datapoints.txt" 

with open(path, "r") as f:
    next(f) # Hoppar över första raden i datapoints filen
    data = f.readlines()
#print(repr(open(path)))

# funktion som gör en lista av alla rader i Data/datapoints.txt
def clean_data(data): 
    clean_data = []
    for line in data:
        clean_line = line.strip().split(",")
        clean_data.append(clean_line)
    return clean_data
#print(clean_data(open(path)))

# Raphael says: Det vore nog enklare att inte separera datan....

# funktion som hämtar värdena från clean_data och appendar pichus x, y värde från label 0. samt pikachus x,y värde från label 1.
def separate_clean_data(data): 
    pichu = []
    pikachu = []
    for row in data:
        width,hight,label = row
        if label == " 0":
            pichu.append((float(width), float(hight)))
        elif label == " 1":
            pikachu.append((float(width), float(hight)))
    return pichu, pikachu
#print(separate_clean_data(clean_data(data)))

# Raphael says: I python kod skall helst alla importer ske överst i filen. Anledningen är att även när denna fil importeras från någon annanstans
# körs filen ändå i ordning från början av filen. Så om något går fel med importerna, så har fortfarande koden ovanför körts.
# I detta fall gör det ingen skillnad.

import matplotlib.pyplot as plt
import numpy as np
import math
# KNN algoritm som tar 10 närmsta punkterna samt beräknar och klassificerar dessa. Koden är inspiration från källor från Stack Overflow, GeeksforGeeks, W3Schools och Real Python. samt gjort felsökning med chatgpt.
def knn_equation(pichu, pikachu, user_input, k=10): 
    classification = []
    for point in user_input:
        # intressant approach att inte spara avstånden, utan bara använda dem som sorteringsfunktion. Blir faktiskt ganska så effektivt!
        closest_points = sorted(pichu + pikachu, key=lambda x: math.sqrt((point[0] - float(x[0]))**2 + (point[1] - float(x[1]))**2))[:k]
        labels = [0 if point in pichu else 1 for point in closest_points]
        classify = 0 if labels.count(0) > labels.count(1) else 1
        classification.append(classify)
    return classification

# Klassificerar datapointsen till Pichu eller Pikachu
def plott_classify_pokemon(pichu, pikachu, user_input, k=10): 
    plott_new_classify_pokemon = knn_equation(pichu, pikachu, user_input)
    plt.scatter(*zip(*pichu), color= 'hotpink', label= 'Pichu', marker='*')
    plt.scatter(*zip(*pikachu), color= 'purple', label = 'Pikachu', marker='*')
    plt.title("Classification for the nearest point")
    plt.xlabel("X = Lenght")
    plt.ylabel("Y = Height")

    # Plottar ny data via user_input och klassificerar dessa som Pichu eller Pikachu. Koden är inspiration från Real Python, Stack Overflow, GeeksforGeeks. samt gjort felsökning med chatgpt.
    for i, classifikation in enumerate(plott_new_classify_pokemon): 
        if classifikation == 0:
            plt.scatter(user_input[i][0], user_input[i][1], color= 'aqua', label= 'New Pichu Point', marker= "X")
        else:
            plt.scatter(user_input[i][0], user_input[i][1], color= 'deepskyblue', label= 'New Pikachu Point', marker= "X")
    plt.legend()
    plt.show()

# Låter användaren välja x och y koordinat, endast positiva nummer. (funktionen loopar om man skriver bokstäver eller negativa nummer)
def user_input():
    while True:
        try:
            x = float(input("Please enter an x-coordinate: "))
            y = float(input("Please enter an y-coordinate: "))
 
            if x < 0 or y < 0:
                print(f"Coordinates can't be negative. Please select new coordinates for X and Y.")
               
            else:
                print(f"The coordinate you choosed are: ({x}, {y}) and the classifikation is in the Plot.")
                return [(x, y)]
        except ValueError:
            print("Invalid. You can only choose numeric inputs. Please choose positiv input for X and Y.")

pichu, pikachu = separate_clean_data(clean_data(data))
user_inputs = user_input()
input = user_inputs
plott_classify_pokemon(pichu, pikachu, input, k=10)


# Klassificering av testdata och koordinatern defineras som Pichu eller Pikachu och printar ut detta i terminalen.
path_test = "Data/testpoints.txt" 
with open(path_test, "r") as t:  # Gör en lista från testpoints som printas i terminalen.
    next(t)
    test_points = []
    for line in t:
            koordinats = line.split('(')[1].split(')')[0].split(',')
            x = float(koordinats[0])
            y = float(koordinats[1])
            test_points.append((x,y))
classifikation = knn_equation(pichu, pikachu, test_points) # Kallar på KNN funktionen för att klassificera Pichu och Pikachu till testpoint.
for point, label in zip(test_points, classifikation):
    print(f"Testpoint for width and height are: ({point[0]}, {point[1]}) and classified as: {'Pikachu' if label == 1 else 'Pichu'}")
