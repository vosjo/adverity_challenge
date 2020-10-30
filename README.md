# Adverity Data Science Challenge:
## Outlier detection

The task is to compute and visualize outliers in a time series, where you need to prepare and aggregate
the underlying raw data upfront. 

### Installation
The python scripts are written in python 3, and require numpy, pandas and matplotlib to be installed. You 
can easily install all dependencies with pip:

    pip install -r requirements.txt

### Obtain the data
Download the train data from:
https://www.kaggle.com/c/avazu-ctr-prediction
And unpack it in the same directory as the python scripts. This should give you a file called "train"

### Aggregate click through rate per hour
Run the python script get_agg_ctr.py. This will calculate the click through rate per hour and save that 
data to a csv file called: "agg_ctr.csv". This script can take a little while to run as it needs to process
nearly 6 Gb of data.

    python get_agg_ctr.py
    
### Find the outliers
To find the outliers using a running average, use the python script outlier_detection.py. It will automatically
read the output from the previous script, calculate a running average and mark the outliers. You can specify the
window size of the running average and the required deviation to be marked as an outlier.

    python outlier_detection.py <WINDOW> <DEV>
    
Where WINDOW is an integer indicating the window size of the rolling average and rolling standard deviation. DEV
is a float indicating the number of standard deviations from the mean are necessary to be marked as an outlier.
If no values are provided, default values of WINDOW=5 and DEV=1.5 are used.

Example use:

    python outlier_detection.py 5 1.5

### Jupiter notebook
There is also a jupyter notebook included that does exacly the same as the two python scripts. For this the 
jupyter notebook environment needs to be installed.