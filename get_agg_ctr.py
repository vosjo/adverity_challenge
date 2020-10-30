"""
Python script that reads the large training set to a pandas data frame, aggregates 
the clicks per hour and saves the much smaller data frame back to csv.
"""

import pandas as pd
import numpy as np

data = pd.read_csv('train', usecols=["click", "hour"])

ctr = data.groupby('hour').agg({'click':[np.sum, 'count']})

ctr.columns = ctr.columns.to_flat_index()
ctr.rename(columns = {('click',   'sum'): 'clicks', ('click',   'count'): 'impressions'}, inplace=True)
ctr.reset_index(drop=False, inplace=True)

ctr.to_csv('agg_ctr.csv')
