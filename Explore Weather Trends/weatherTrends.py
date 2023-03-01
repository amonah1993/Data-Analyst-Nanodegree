import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


data= pd.read_csv("results-f.csv")

def moving_average(Moving_Avg_range,data_input):
    output=data_input.rolling(window=Moving_Avg_range, on="cd")
    output=output.mean()
    
    return output

Moving_Average_Chart=moving_average(140,data)

plt.plot(Moving_Average_Chart['year'],Moving_Average_Chart['gd'],label='Global')
plt.plot(Moving_Average_Chart['year'],Moving_Average_Chart['cd'],label='Mecca')

plt.xlabel("YEARS")
plt.ylabel("TEMPERATURE")
plt.title("GLOPAL AVERAGE TEMPREATURE VS MECCA CITY")

plt.show()

