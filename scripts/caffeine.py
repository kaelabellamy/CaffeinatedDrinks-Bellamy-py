#%%
from matplotlib.colors import Normalize
import pandas as pd
import numpy as np
import altair as alt
from plotnine import *
import seaborn as sns

import matplotlib as mpl
import matplotlib.pyplot as plt
#%% Read in Data and rename columns, check for missing values
dat = pd.read_csv("C:/Users/kaela/Desktop/datascience/personal_project1_bellamy-2/data/caffeine.csv")
dat.head()
dat.columns = ['drink', 'volume', 'calories', 'caffeine', 'type']
dat.isnull().sum()
# %% Organize data by type of drink
dat.groupby('type')
#%% Create new data frames for each type of drink
dfcoffee = dat[(dat['type'] == 'Coffee')]
dfcoffee = dfcoffee[dfcoffee['calories'] <= 750]
dfeg = dat[(dat['type']) == 'Energy Drinks']
dfes = dat[(dat['type']) == 'Energy Shots']
dfsd = dat[(dat['type']) == 'Soft Drinks']
dftea = dat[(dat['type']) == 'Tea']
dfwater = dat[(dat['type']) == 'Water']
# %% From new data frames identify x, y and c values
X1 = dfcoffee['volume']
Y1 = dfcoffee['calories']
C1 = dfcoffee['caffeine']
X2 = dfeg['volume']
Y2 = dfeg['calories']
C2 = dfeg['caffeine']
X3 = dfes['volume']
Y3 = dfes['calories']
C3 = dfes['caffeine']
X5 = dfsd['volume']
Y5 = dfsd['calories']
C5 = dfsd['caffeine']
X6 = dftea['volume']
Y6 = dftea['calories']
C6 = dftea['caffeine']
X7 = dfwater['volume']
Y7 = dfwater['calories']
C7 = dfwater['caffeine']
# %%
#fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex=True, sharey=True)
fig, axs = plt.subplots(2, 3, sharex=True, sharey=True)
fig.suptitle('Is Your Drink What You Expected?', size='large', weight='demibold')
fig.text(0.5, 0.04, 'Volume(ml)', ha='center')
fig.text(0.04, 0.5, 'Calories', va='center', rotation='vertical')

#set the colorbar ticks and tick labels
cbar.set_ticks(np.arange(0, 1.1, 0.5))
cbar.set_ticklabels(['Low Caffeine', 'Medium Caffeine', 'High Caffeine'], size='small')


axs[0,0].hexbin(X1, Y1, C1, cmap = 'ocean', gridsize = 25)
axs[0,0].set_title('Coffee', size='small')

axs[0,1].hexbin(X2, Y2, C2, cmap = 'ocean', gridsize = 20)
axs[0,1].set_title('Energy Drinks', size='small')

axs[0,2].hexbin(X3, Y3, C3, cmap = 'ocean', gridsize = 20)
axs[0,2].set_title('Energy Shots', size='small')

axs[1,0].hexbin(X5, Y5, C5, cmap = 'ocean', gridsize = 20)
axs[1,0].set_title('Soft Drinks', size='small')

axs[1,1].hexbin(X6, Y6, C6, cmap = 'ocean', gridsize = 20)
axs[1,1].set_title('Tea', size='small')

axs[1,2].hexbin(X7, Y7, C7, cmap = 'ocean', gridsize = 20)
axs[1,2].set_title('Water', size='small')

fig.subplots_adjust(right=0.8,
                     wspace=0.2, hspace=0.2)

cb_ax = fig.add_axes([0.83, 0.1, 0.02, 0.8])
cbar = fig.colorbar(im, cax=cb_ax, cmap='ocean', label='Caffeine(mg)')

# %%
fig.savefig('Drink.pdf')
# %%
