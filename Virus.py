import pandas as pd
import statistics
import plotly.express as px
import plotly.figure_factory as ff
import random
import csv
import numpy as np 


y = []

# x = 180
# y = m*x+c
# print("¬_¬ :->", y)
 
df = pd.read_csv("/content/main.csv")

GRE_Score = df['GRE Score'].tolist()
Chance_of_Admit = df['Chance of Admit '].tolist()

height_array = np.array(GRE_Score)
weight_array = np.array(Chance_of_Admit)

m, c = np.polyfit(height_array, weight_array, 1)

for x in GRE_Score:
   y_value = m*x+c
   y.append(y_value)

fig = px.scatter(df, y=weight_array, x=height_array, color="GRE Score")

fig.update_layout(shapes = [dict(type="line", y0=min(y),  y1=max(y),  x0=min(height_array), x1=max(height_array)  )])

fig.show()
