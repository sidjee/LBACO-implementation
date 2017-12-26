import pandas as pd

df = pd.read_csv("graphdata.csv")
columns = ['tasks', 'averageTime']
xy = df[columns]

import matplotlib.pyplot as plt

width =6 
#plt.bar(x, y, width, color="blue")
plt.bar(xy['tasks'], xy['averageTime'],width,color="blue")
plt.xlabel('tasks')
plt.ylabel('averageTime')
plt.show()
