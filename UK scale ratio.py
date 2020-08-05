import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
#import time
#from tqdm.notebook import tqdm
#import pickle

from IPython.core.display import display, HTML
display(HTML("<style>.container { width:95% !important; }</style>"))

t1 = pd.read_csv('companies_03_08_20_1596482618.csv', low_memory=False)
t1['HQ COUNTRY'].value_counts()

t2 = t1[t1['HQ COUNTRY']=='United Kingdom']

t2['GROWTH STAGE'].value_counts()
t2 = t2[t2['GROWTH STAGE']!= 'not meaningful']

growth_stage = t2.loc[tindex, 'GROWTH STAGE'].apply(lambda x: x[:-6])
t2['GROWTH STAGE'] = growth_stage

tt = t2[t2['GROWTH STAGE'].notnull()].groupby(['HQ CITY', 'GROWTH STAGE'])['GROWTH STAGE'].count().to_frame()

topcities_hq_num = t2[t2['GROWTH STAGE'].notnull()]['HQ CITY'].value_counts().index.tolist()
#ordered_index = ['seed', 'early growth', 'late growth']

cdict = {'seed': 'green', 'early growth': 'orange', 'late growth': 'red'}

fig,ax = plt.subplots(5,5, figsize = (40,40))
counter = 0
for i1 in range(5):
    for i2 in range(5):
        labels = tt.loc[topcities_hq_num[counter]].index.tolist()
        sizes = tt.loc[topcities_hq_num[counter]].values.flatten()
        colors = [cdict[x] for x in labels]
        ax[i1,i2].pie(sizes, labels = labels, autopct = '%.0f%%', shadow = False, radius = 1, colors = colors, textprops={'fontsize': 14})
        ax[i1,i2].set_title('{} ({:,})'.format(topcities_hq_num[counter], sum(sizes)), fontsize = 14)
        counter +=1
plt.savefig('top25cities2.png', dpi = 200, bbox_inches = 'tight')
plt.show()

fig,ax = plt.subplots(5,5, figsize = (40,40))
counter = 25
for i1 in range(5):
    for i2 in range(5):
        labels = tt.loc[topcities_hq_num[counter]].index.tolist()
        sizes = tt.loc[topcities_hq_num[counter]].values.flatten()
        colors = [cdict[x] for x in labels]
        ax[i1,i2].pie(sizes, labels = labels, autopct = '%.0f%%', shadow = False, radius = 1, colors = colors, textprops={'fontsize': 14})
        ax[i1,i2].set_title('{} ({:,})'.format(topcities_hq_num[counter], sum(sizes)), fontsize = 14)
        counter +=1
plt.savefig('top25cities26_50.png', dpi = 200, bbox_inches = 'tight')
plt.show()


ind_list = t2.loc[t2.INDUSTRIES.notnull(), 'INDUSTRIES'].apply(lambda x: x.replace(';', '&'))
t2.loc[t2.INDUSTRIES.notnull(), 'INDUSTRIES'] = ind_list

ttt = t2[(t2['GROWTH STAGE'].notnull()) & (t2.INDUSTRIES.notnull())].groupby(['INDUSTRIES', 'GROWTH STAGE'])['GROWTH STAGE'].count().to_frame()
top_ind = t2[(t2['GROWTH STAGE'].notnull()) & (t2.INDUSTRIES.notnull())]['INDUSTRIES'].value_counts().index.tolist()

fig,ax = plt.subplots(5,5, figsize = (40,40))
counter = 0
for i1 in range(5):
    for i2 in range(5):
        labels = ttt.loc[top_ind[counter]].index.tolist()
        sizes = ttt.loc[top_ind[counter]].values.flatten()
        colors = [cdict[x] for x in labels]
        ax[i1,i2].pie(sizes, labels = labels, autopct = '%.0f%%', shadow = False, radius = 1, colors = colors, textprops={'fontsize': 14})
        ax[i1,i2].set_title('{} ({:,})'.format(top_ind[counter], sum(sizes)), fontsize = 14)
        counter +=1
plt.savefig('top25industries.png', dpi = 200, bbox_inches = 'tight')
plt.show()

fig,ax = plt.subplots(5,5, figsize = (40,40))
counter = 25
for i1 in range(5):
    for i2 in range(5):
        labels = ttt.loc[top_ind[counter]].index.tolist()
        sizes = ttt.loc[top_ind[counter]].values.flatten()
        colors = [cdict[x] for x in labels]
        ax[i1,i2].pie(sizes, labels = labels, autopct = '%.0f%%', shadow = False, radius = 1, colors = colors, textprops={'fontsize': 14})
        ax[i1,i2].set_title('{} ({:,})'.format(top_ind[counter], sum(sizes)), fontsize = 14)
        counter +=1
plt.savefig('top25_50_industries.png', dpi = 200, bbox_inches = 'tight')
plt.show()
