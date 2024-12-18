#Authored by: Jacob Long
#"The smell of coffee brewing over a fire pit, a chestnut-flavored morning.
#Welcome to Astra Country."

import matplotlib.pyplot as plt
import csv
from math import radians
import numpy as np

def main():
    
    #define axes
    x = []
    y = []

    #open up the file, read each entry.
    #TODO: come up with a way to put this as a relative path, so it's independent of filename
    with open('L-2 Temp Data.csv', 'r') as csvfile:
        plot = csv.reader(csvfile, delimiter = ',')
        # add info to axes (TODO: Add correct info to axes)
        for row in plot:
            x.append(row[0])
            y.append(row[2])

    #Define labels and graph information. plt.show() opens a dialogue with plotted data
    #TODO: make it work with actual data, below is a test
    plt.bar(x, y, color = 'g', width = 0.7, label = "Test")
    plt.xlabel('X test')
    plt.ylabel('Y test')
    plt.title('Title Test')
    plt.legend()
    plt.show()

# Test block to show that matplotlib works as advertised
# def main():
#     x = np.arange(0, radians(1800), radians(12))
#     plt.plot(x, np.cos(x), 'b')
#     plt.show()

#PULL THE LEVER, KRONK
main()

