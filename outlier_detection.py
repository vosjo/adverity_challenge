
import sys
import pandas as pd
import pylab as pl
import numpy as np

#--------------------------------------------------------------------

WINDOW = 5
DEV = 1.5

#--------------------------------------------------------------------

# read the user input
args = sys.argv
if len(args) == 3:
    try:
        WINDOW = int(args[1])
        DEV = float(args[2])
    except Exception:
        print("Can't read command line arguments. use as: \n\tpython outlier_detection.py WINDOW DEV")
else:
    print("no arguments or not enough arguments provided. use as:\n\tpython outlier_detection.py WINDOW DEV \n using default values.")

print("WINDOW: ", WINDOW)
print("DEV: ", DEV)

# calculate ctr and find outliers
ctr = pd.read_csv('agg_ctr.csv')

ctr['ctr'] = ctr['clicks'] / ctr['impressions']
ctr['date'] = pd.to_datetime(ctr['hour'], format="%y%m%d%H")

ctr['mean'] = ctr['ctr'].rolling(WINDOW, center=True).mean()
ctr['std'] = ctr['ctr'].rolling(WINDOW, center=True).std()

out = (ctr['ctr'] > ctr['mean'] + DEV * ctr['std']) | (ctr['ctr'] < ctr['mean'] -DEV * ctr['std'])

# plot
pl.figure(1, figsize=(10, 5))
pl.plot(ctr['date'], ctr['ctr'])

pl.xticks(rotation=-45)

pl.xlabel('Date')
pl.ylabel('CTR')
pl.title('Raw CTR')

pl.figure(2, figsize=(10, 5))
pl.plot(ctr['date'], ctr['ctr'], '-C0', label='CTR')
pl.plot(ctr['date'], ctr['mean'], '-C1', label='mean')

minc, maxc = ctr['mean']-DEV*ctr['std'], ctr['mean']+DEV*ctr['std']
s = ~ctr['mean'].isna()
pl.fill_between(ctr['date'][s], minc[s], maxc[s], color='C1', alpha=0.2, label='{} std'.format(DEV))
pl.plot(ctr['date'][out], ctr['ctr'][out], 'or', label='outliers')

pl.xticks(rotation=-45)

pl.xlabel('Date')
pl.ylabel('CTR')
pl.legend()
pl.title(r'CTR with outliers marked, window = {}, outlier: > {} $\sigma$'.format(WINDOW, DEV))

pl.show()
