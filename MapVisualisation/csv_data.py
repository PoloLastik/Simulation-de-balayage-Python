import Data
import csv
import sys
import numpy as np
from tkinter import filedialog
csv_types = [("CSV files", ".csv")]
def write(map):
    with filedialog.asksaveasfile(mode="w",filetypes=csv_types) as f:
        np.savetxt(f.name,map.array,delimiter=';')
        #writter = csv.writer(f)
        #for x in range(map.size_x):
         #   writter.writerow(map.getRow(x))

def read():
    array = Data.getEmptyArray(0,0)
    map = Data.Map(array)
    with filedialog.askopenfile(mode='r',filetypes=csv_types) as f:
        arr = np.loadtxt(f.name,delimiter=';')
        map.setArray(arr)
        #reader = csv.reader(f)
        #for row in reader:
        #    map.addLine(row)
    return map
