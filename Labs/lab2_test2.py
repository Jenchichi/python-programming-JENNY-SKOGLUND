import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

class KNNClassifier:
    """Class to implement k-Nearest Neighbors classification."""
    def __init__(self, k=3):
        self.k = k
        self.data_points = []

    def fit(self, data_points):
        """Fit the model with labeled data points."""
        self.data_points = data_points

    def predict(self, new_point):
        """Predict the label of a new point using k-NN."""
        distances = [(self.calculate_distance(new_point, dp), dp[2]) for dp in self.data_points]
        # Get the k nearest neighbors
        k_nearest_labels = [label for _, label in sorted(distances)[:self.k]]
        return Counter(k_nearest_labels).most_common(1)[0][0]

    @staticmethod
    def calculate_distance(point1, point2):
        """Calculate Euclidean distance between two points."""
        return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def load_data(file_path):
    """Load labeled data points from a file."""
    data_points = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            try:
                width = float(parts[0])
                height = float(parts[1])
                label = int(parts[2])
                data_points.append((width, height, label))
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
    return data_points

def plot_points(data_points, classified_points=None):
    """Plot the training data and optionally classified points."""
    pichu = [dp for dp in data_points if dp[2] == 0]
    pikachu = [dp for dp in data_points if dp[2] == 1]

    plt.scatter([dp[0] for dp in pichu], [dp[1] for dp in pichu], color="pink", marker="*", label="Pichu")
    plt.scatter([dp[0] for dp in pikachu], [dp[1] for dp in pikachu], color="purple", marker="*", label="Pikachu")

    if classified_points:
        for point, label in classified_points:
            color = "pink" if label == 0 else "purple"
            plt.scatter(point[0], point[1], color=color, marker="X", s=200, label=f"Test Point {point[0]},{point[1]}")

    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.title("Pichu and Pikachu Classification")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Load data
    data_points = load_data("Data/datapoints_new.txt")
    
    # Initialize KNN classifier
    knn = KNNClassifier(k=3)
    knn.fit(data_points)

    # Input new points
    classified_points = []
    while True:
        user_input = input("Enter a new point (x,y) or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            break
        try:
            x, y = map(float, user_input.split(","))
            label = knn.predict((x, y))
            classified_points.append(((x, y), label))
            print(f"The new point ({x}, {y}) is classified as: {label}")
        except ValueError:
            print("Invalid input. Please enter in the format 'x,y'.")

    # Plot results
    plot_points(data_points, classified_points)

# Execute the main function
if __name__ == "__main__":
    main()
