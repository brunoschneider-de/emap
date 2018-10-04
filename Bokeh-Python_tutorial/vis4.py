# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 09:50:01 2018

@author: bruno
"""

from bokeh.plotting import figure, output_file, show

output_file("vis4.html")

p = figure(plot_width=400, plot_height=400)

# add a steps renderer
p.step([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2, mode="center")

show(p)