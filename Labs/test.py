# Bonus uppgift, 3) EJ FÄRDIG! EJ labb inlämning endast sparad kod.
# Gå in i fil, open folder, välj den mapp som du vill öppna vs code med. (Python-programming-JENNY_SKOGLUND)
path = "Data/datapoints.txt" 

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

# skapat en list variabel med alla 150 pokemon.
pokemon_list = pichu + pikachu

# Tar ut 50 punkter(x,y) från pikachu och Pichu listan. 
import random

random.shuffle(pichu)
random.shuffle(pikachu)
pichu_50 = [p for p in pichu][:50]
pikachu_50 = [p for p in pikachu][:50]
pichu_25 = [p for p in pichu][:25]
pikachu_25 = [p for p in pikachu][:25]

# Ta bort len från printen om man vill printa hela listan. print(len(..)) gör så att man ser antalet av punkter som plockas ut från listan.
print(len(pichu_50))
print(len(pikachu_50))
print(len(pichu_25))
print(len(pikachu_25))

# Bonus uppgift, 4)
# Beräkna avståndet mellan testpunkterna till träningspunkterna alltså pichu_50 och pikachu_50 = träningsdata. pichu_25 och pikachu_25 = testpunkter.
import math
train_data = pichu_50 + pikachu_50
test_data = pichu_25 + pikachu_25
distances = []

for test_point in test_data:
    for train_point in train_data:
        distance = math.sqrt((test_point[0] - (train_point[0]))**2 + (test_point[1] - (train_point[1]))**2)
        distances.append(distance)
print(len(distances))

