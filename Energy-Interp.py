from scipy.interpolate import interp1d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import statsmodels.api as sm
import pickle
from scipy import arange, array, exp

#Import libraries for data manipulation, interpolation, and graphing

df = pd.read_csv(
    "C:\\Projects\\IMMC Math Mod\\Ecological Footprint\\Work\\Simple-Energy.csv")
y2 = df['Natural Gas'].values
y = df['Wind'].values
x = df['Year'].values

#Read data into pandas dataframe and assign cost and years to variables

fG = interp1d(x, y2)
f2G = interp1d(x, y2, kind='cubic', fill_value='extrapolate')
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic', fill_value='extrapolate')

#interpolate data

xnew = np.linspace(min(x), max(x), num=41, endpoint=True)
plt.style.use('seaborn')
plt.title('The Effect of Time on the Cost of Wind and Natural Gas Power')
plt.xlabel('Year')
plt.ylabel('Cost ($/mWh)')
plt.plot(x, y2, 'x', xnew, fG(xnew), '-', xnew, f2G(xnew), '--')
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['Gas data', 'Gas linear', 'Gas cubic', 'Wind data',
            'Wind linear', 'Wind cubic'], loc='best')
plt.show()

#graph interpolation of data
