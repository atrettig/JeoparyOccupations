from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np
from sqlalchemy import asc, true
import seaborn as sns

# df = pd.read_csv('dictOutput2.csv')

# df.columns = ['Occupation', 'Count']
# df.sort_values(by='Count', inplace=True, ascending=False)
# # print(df)
# df.astype({"Count" : "int32"}).dtypes

# yellow_color = matplotlib.colors.hex2color('#FFCC00')
# blue_color = matplotlib.colors.hex2color('#4968C7')
# sns.set_style("darkgrid")
# sns.barplot(x = 'Count', y = 'Occupation', data = df, color = yellow_color)


data = [307,203,116,47]
labels = ['Senior', 'Junior', 'Sophomore', 'Freshman']
colors = sns.color_palette('pastel')[0:5]

fig = plt.figure()
fig.patch.set_facecolor('#010a78')


# Change color of text
plt.rcParams['text.color'] = 'white'
 
# Create a circle at the center of the plot
my_circle=plt.Circle( (0,0), 0.7, color='#010a78')
 
# Pieplot + circle on it
plt.pie(data, colors=colors)
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.show()



# for row in df:
#     if row['Occupation'].str.contains('attorney'):
#         print("Occupation: ", row['Occupation'], "Count: ", row['Count'])
# # print(df['Occupation'].str.contains('attorney').sum())

