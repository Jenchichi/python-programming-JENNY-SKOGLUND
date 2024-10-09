import csv
import matplotlib.pyplot as plt

x_point = []
y_point = []

with open('Data/unlabelled_data.csv') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        x_point.append((float(row[0])))
        y_point.append((float(row[1])))

x_medium = sum(x_point)/len(x_point)
y_medium = sum(y_point)/len(y_point)
standardavvikelse = sum((x - x_medium) * (y - y_medium) for x, y in zip(x_point, y_point)) /len(x_point)
varians = sum((x - x_medium)**2 for x in x_point) / len(x_point)
k = standardavvikelse/varians
m = 0

plt.scatter(x_point, y_point, s=12, color = "blue")
line = [k * xi + m for xi in x_point]
plt.plot(x_point, line, color = "red")
plt.show()

