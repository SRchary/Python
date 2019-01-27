import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading csv file 

weather_df = pd.read_csv('weather_data.csv');
print(weather_df['temperature'])

plt.plot( weather_df['day'], weather_df['temperature']  )


