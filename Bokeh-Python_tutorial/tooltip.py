# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 11:36:20 2018

@author: bruno
"""

from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool

output_file("toolbar.html")

hover = HoverTool()

source = ColumnDataSource(data=dict(
    x=[1, 2, 3, 4, 5],
    y=[2, 5, 8, 2, 7],
    desc=['A', 'b', 'C', 'd', 'E'],
))

hover.tooltips = [
    ("index", "$index"),
    ("(x,y)", "($x, $y)"),
    ("desc", "@desc"),
]

p = figure(plot_width=400, plot_height=400,
           title="Mouse over the dots")

p.circle('x', 'y', size=20, source=source)
p.tools.append(hover)

show(p)