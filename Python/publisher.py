import pandas as pd
import numpy as np
import os
os.getcwd()
import plotly.express as px

# df = pd.read_csv('vgsales.csv')

os.chdir('C:\\Users\\uqba2\\OneDrive\\Documents\\Video Game Analysis\\Python')

df = pd.read_csv('vgsales.csv')

fig=px.histogram(df,x='Platform' ,template='plotly_dark')
fig.show()
# df.head(4)