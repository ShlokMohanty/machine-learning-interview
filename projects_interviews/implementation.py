import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px 
import plotly.graph_objects as go

# Reading csv_files :

data = pd.read_csv("D://data_science/competitions/crime-against-women_2001-2014.csv")

# First few samples of teh dataset
df.head()

# Types of data of we have 
df.info()

# shape of the dataset 
df.shape

# Dropping the idex columns that is useless
