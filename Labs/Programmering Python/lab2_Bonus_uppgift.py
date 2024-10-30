# Bonus uppgift, 3 & 4)
# Gå in i fil, open folder, välj den mapp som du vill öppna vs code med. (Python-programming-JENNY_SKOGLUND)
import math
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import random

path = "Data/datapoints.txt"
accuracy_medel_list = []

for _ in range(11):
    with open(path, "r") as f:
        next(f) # Hoppar över första raden i datapoints filen
        data = f.readlines()
        data_points = []
        for line in data:
            width, hight, label = line.strip().split(",")
            data_points.append((width, hight, label))
 
# Separerar datan och skapar två listor med Pichu och Pikachus punkter. Där Pichus label== 0 och Pikachus label==1
    def separate_clean_data(data):
        pichu = []
        pikachu = []
        for row in data:
            width, hight, label = row
            if label == " 0":
                pichu.append((float(width), float(hight)))
            elif label == " 1":
                pikachu.append((float(width), float(hight)))
        return pichu, pikachu
 
    pichu, pikachu = separate_clean_data(data_points)
 
# Blandar listorna och tar ut 50 random punkter(x,y) från pikachu och Pichu listan samt 25 punkter(x,y) från pikachu och pichu listan. Koden är inspiration från w3schools, stackoverflow.
    random.shuffle(pichu)
    random.shuffle(pikachu)
    pichu_50 = [p for p in pichu][:50]
    pikachu_50 = [p for p in pikachu][:50]
    pichu_25 = [p for p in pichu][:25]
    pikachu_25 = [p for p in pikachu][:25]

# Bonus uppgift, 4)
# Klassificerar Pichu och Pikachu: pichu_50 och pikachu_50 = träningsdata. pichu_25 och pikachu_25 = testpunkter.
    train_data = pichu_50 + pikachu_50
    test_data = pichu_25 + pikachu_25

    # Skapa en lista med etiketter för testpunkterna. Koden är inspiration från kodrummet.se
    test_labels = [0] * len(pichu_25) + [1] * len(pikachu_25)
    
    # Skapa en lista med etiketter för träningspunkterna
    train_labels = [0] * len(pichu_50) + [1] * len(pikachu_50)

    # Använd KNN-klassificerare. Koden är inspiration från en dokumentation på denna hemsidan: https://scikit-learn.org/stable/modules/neighbors.html
    knn = KNeighborsClassifier(10)
    knn.fit(train_data, train_labels)
    predictions = knn.predict(test_data)
    # Beräkna TP, TN, FP och FN. Koden är inspiration från stackoverflow, github. samt felsökning via chatgpt.
    TP = 0
    TN = 0
    FP = 0
    FN = 0

    for i in range(len(test_labels)):
        if test_labels[i] == 1 and  predictions[i] == 1:
            TP += 1
        elif test_labels[i] == 1 and  predictions[i] == 0:
            FP += 1
        elif test_labels[i] == 0 and  predictions[i] == 0:
            TN += 1
        elif test_labels[i] == 0 and  predictions[i] == 1:
            FN += 1

    accuracy = (TP + TN) / (TP + TN + FP + FN)
    accuracy_medel_list.append(accuracy)

# Beräknar medelaccuracy:
accuracy_medel = sum(accuracy_medel_list) / len(accuracy_medel_list)
# Printar 
print("TP:", TP)
print("TN:", TN)
print("FP:", FP)
print("FN:", FN)
print(f"accuracy: {accuracy*100}%")
print(f"Medelaccuracy: {round(accuracy_medel*100, 2)}%")

# Plotta resultaten
plt.figure(figsize=(9, 6))
plt.plot(range(len(accuracy_medel_list)), accuracy_medel_list)
plt.title("Calculation of the accuracy for TP, TN, FP, FN over 10 measurment")
plt.xlabel("Number of Measurment")
plt.ylabel("Accuracy")
plt.show()