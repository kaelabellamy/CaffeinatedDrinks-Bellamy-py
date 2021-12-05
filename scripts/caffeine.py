#%%
import pandas as pd
import numpy as np
import altair as alt
from plotnine import *

#%%
dat = pd.read_csv("C:/Users/kaela/Desktop/datascience/personal_project1_bellamy-1/data/caffeine.csv")
dat.head()
dat.isnull().sum()

# %%
