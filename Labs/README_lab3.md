## Program - Lab 3
The program calculates whether the point is above/left of or below/right of the line.
This is done with linear algebra and the mathematical formula y = kx + m. The program imports the file unlabelled_data.csv where each line gets an x ​​and a y coordinate.
- The program goes through each line in the file and chooses that x always is the index value 0 and y always takes the index value 1.

#### Calculation y = kx + m
- The program calculates whether the point is above/below the line.
- If the point's y value is greater than the line's y value, then the point is classified as above the line (above_line)
- If the point's y value is less than the line's y value, then the point is classified as below the line (below_line)
- The program then prints in the terminal how many points are above and below the line. In this case, we have
determined the k- and m-value of the line.

### The program plots the graph.
- In the graph, all points from unlabelled_data.csv are plotted as well as the calculation of the line y = kx + m. All points that are above the line turns blue and the points below the line turns pink.

### Classification in a new file labelled_data.csv
- The program creates a new file and classifies the points in the new file where the classifier 0 is above the line and 1 is below the line.