
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading csv file

weather_df = df = pd.read_csv('c://weather_data.csv');
weather_df['temperature']


weather_df['day'] ## weather_df.day
weather_df[weather_df.temperature >= weather_df["temperature"].mean()]
weather_df.describe()

##Indexing
weather_df.index
df.set_index( "day" ,inplace=True)
df





plt.plot(  weather_df['day'], weather_df['windspeed']  ,label="wind speed" ,alpha=0.2  )
plt.plot( weather_df['day'], weather_df['temperature'] ,label="temperature" ,alpha=0.8  )
plt.legend(loc="best")

weather_df['day']

plt.xticks([0,1,2,3,4,5] ,["1/1/2017" ,"1/2/2017" ,"1/3/2017" ,"1/4/2017" ,"1/5/2017"])
plt.bar([0,1,2,3,4,5] ,weather_df['windspeed'] , width =0.5)
plt.bar([0,1,2,3,4,5] ,weather_df['temperature'] , width =0.5)



#####
weather_df.describe()

plt.xticks([0,1,2,3,4,5] ,["1/1/2017" ,"1/2/2017" ,"1/3/2017" ,"1/4/2017" ,"1/5/2017"])
plt.bar([0,1,2,3,4,5] ,weather_df['windspeed'] , width =0.5)
plt.bar([0,1,2,3,4,5] ,weather_df['temperature'] , width =0.5)

plt.plot(  weather_df['day'], weather_df['windspeed']  ,label="wind speed" ,alpha=1 )
plt.plot( weather_df['day'], weather_df['temperature'] ,label="temperature" ,alpha=0.3  )
plt.legend(loc="best")


