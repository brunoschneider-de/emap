# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 12:05:52 2018

@author: bruno
"""

import pandas as pd

df = pd.read_csv("gapminder_fertility.csv")
df_no_missing = df.dropna()