path = "Data/datapoints.txt" # Gå in i fil, open folder, välj den mapp som du vill öppna vs code med. (Python-programming-JENNY_SKOGLUND)

with open (path, "r") as f:
    text = f.read()

print(repr(text))

import re

quotes, i = [], 1

with open(path, "r") as f_read, open("Data/datapoints_new.txt", "w") as f_write:
    f_write.write("Pokemon list\n\n")
    for quote in f_read:
        quote = quote.strip(" \n")
        quote = re.sub(r" +", " ", quote)
        if quote != "":
            f_write.write(f"{i}. {quote}\n")
            i += 1

import matplotlib.pyplot as plt
import numpy as np

width1 = 
height1 =
width0 = 
height0 = 

plt.scatter(width1, height1, color = 'hotpink')
plt.scatter(width0, height0, color = 'blue')

