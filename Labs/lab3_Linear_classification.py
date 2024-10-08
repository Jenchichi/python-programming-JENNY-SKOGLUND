# Beräknar om punkten ligger ovanför/vänster om eller nedanför/höger om linjen    
# x = "Punktens x-värde"
# y = "punktens y-värde"    
# k = "Riktningskoefficient/ Linjens lutning"
# m = "Där linjen skär y-axeln/är en konstant som motsvarar y-värdet"

import csv
import matplotlib.pyplot as plt

x_point = []
y_point = []
k = 1
m = 1

with open('Data/unlabelled_data.csv') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        x_point.append((float(row[0])))
        y_point.append((float(row[1])))

def point_position_from_line(x_point, y_point, k, m):
    # Beräknar om punkten ligger ovanför/vänster om eller nedanför/höger om linjen
    above_line = []
    below_line = []
    on_line = []

    # Beräkna linjens y-värde vid punktens x-värde
    for x, y in zip(x_point, y_point):
        y_line = k * x + m
        if y > y_line:
            above_line.append((x,y))
        elif y < y_line:
            below_line.append((x,y))
        else:
            on_line.append((x,y))
    return above_line, below_line, on_line
above_line, below_line, on_line = point_position_from_line(x_point, y_point, k, m)

print(f"Test för att se om det fungerar ABOVE LINE!!!            {above_line}")
print(f"Test för att se om det fungerar BELOW LINE!!!            {below_line}")
print(f"Test för att se om det fungerar ON LINE!!!!              {on_line}")

