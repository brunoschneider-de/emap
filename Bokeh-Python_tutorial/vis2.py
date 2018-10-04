# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 09:50:01 2018

@author: bruno
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure

output_file("vis2.html")

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']

p = figure(x_range=fruits, plot_height=250, title="Fruit Counts",
           toolbar_location=None, tools="")

p.vbar(x=fruits, top=[5, 3, 4, 2, 4, 6], width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)