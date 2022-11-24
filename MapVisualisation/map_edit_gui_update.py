import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import map_edit_gui
import map_edit_gui_support

def updateCanvWithMap(canv,map):
    #parent = canv.info()['in']
    #parent.taille.set(str(map.size_x) +"x" + str(map.size_y))
    canv.delete('ALL')
    for x in range(map.size_x):
        for y in range(map.size_y):
            entry = tk.Entry(canv,width=map_edit_gui.default_width_entry)
            entry["bg"] = "black" if map.array[x,y] == 1 else "white"
            entry.grid(row=x,column=y)
            entry.bind("<1>",setCell)


def setCell(event):
    global map
    widget = event.widget
    widget["bg"] = map_edit_gui.NoObstacleColour if widget["bg"] == map_edit_gui.ObstacleColour else map_edit_gui.ObstacleColour


def addRow(canv,map):
    map.addLine()
    updateCanvWithMap(canv,map)

def addColumn(canv,map):
    map.addColumn()
    updateCanvWithMap(canv,map)

