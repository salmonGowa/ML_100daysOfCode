import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

#reading data from csv file
data=pd.read_csv('train.csv')
#defining variables
x=data['x'].tolist()
y=data['y'].tolist()
#adding the constant term
x=sm.add_constant()
#fitting the model
x=sm.OLS(y,x).fit()

#output of the summary table
print(result.summary())
