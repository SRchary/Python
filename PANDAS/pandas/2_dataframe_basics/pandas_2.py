import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading csv file

weather_df = pd.read_csv('c://weather_data.csv');
weather_df['temperature']
plt.plot(  weather_df['day'], weather_df['windspeed']  ,label="wind speed" ,alpha=0.2  )
plt.plot( weather_df['day'], weather_df['temperature'] ,label="temperature" ,alpha=0.8  )
plt.legend(loc="best")

weather_df['day']

plt.xticks([0,1,2,3,4,5] ,["1/1/2017" ,"1/2/2017" ,"1/3/2017" ,"1/4/2017" ,"1/5/2017"])
plt.bar([0,1,2,3,4,5] ,weather_df['windspeed'] , width =0.5)
plt.bar([0,1,2,3,4,5] ,weather_df['temperature'] , width =0.5)