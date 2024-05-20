import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
import random

pd.set_option("display.max_columns",300)






data = pd.read_csv("pokemon_data.csv")
data2 = pd.read_csv("pokemon_extended.csv")

df = pd.DataFrame(data)


df2 = pd.DataFrame(data2)


df2 = df2.rename(columns={"Unnamed: 0":"#"})

pd.options.display.float_format = "{:.2f}".format

raport = df2.describe()

print(raport)

boxplot = raport.boxplot(column=["Attack","Defense","HP","Speed"],by=["Attack","Defense","HP","Speed"],layout=(5,1),fontsize=6)

