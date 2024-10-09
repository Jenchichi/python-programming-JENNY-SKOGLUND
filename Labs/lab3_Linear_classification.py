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
m = 0

with open('Data/unlabelled_data.csv') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        x_point.append((float(row[0])))
        y_point.append((float(row[1])))

def point_position_from_line(x_point, y_point, k, m):
    # Beräknar om punkten ligger ovanför/vänster om eller nedanför/höger om linjen
    above_line = []
    below_line = []
    

    # Beräkna linjens y-värde vid punktens x-värde
    for x, y in zip(x_point, y_point):
        y_line = k * x + m
        if y > y_line:
            above_line.append((x,y))
        else:
            y < y_line
            below_line.append((x,y))
    return above_line, below_line
above_line, below_line = point_position_from_line(x_point, y_point, k, m)

print(f"Points above the line: {len(above_line)}")
print(f"Points below the line: {len(below_line)}")

with open("Data/labelled_data.csv", "w", newline='') as f_write:
    csv_writer = csv.writer(f_write)

    label = [0 if (xi, yi) in above_line else 1 for xi, yi in zip(x_point, y_point)]
    sorted_label = sorted(zip(x_point, y_point, label))
    for (x_point, y_point, label) in sorted_label:
        f_write.write(f"{x_point}, {y_point}, {label}" '\n')



#y_point = k * x_point + m

#plt.scatter(x_point, y_point, color=['blue' if (xi, yi) in above_line else 'red' for xi, yi in zip(x_point, y_point)])
#plt.show()