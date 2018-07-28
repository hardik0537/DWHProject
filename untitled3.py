# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 14:10:54 2018

@author: Hardik Galiawala
"""

import pandas as pd
import datetime
import numpy 
numpy.set_printoptions(threshold=numpy.nan)
#raw_data = pd.read_csv('Data/NYPD_Complaint_Data_Historic.csv', nrows = 1000)
#print(raw_data.head())
 
def read_concat_df():
    climate_new_york_df = pd.read_csv('Data/humidity.csv')
    climate_new_york_df = pd.concat([climate_new_york_df['datetime'], climate_new_york_df['New York']], axis = 1)
    climate_new_york_df = climate_new_york_df.rename(columns={'New York': 'humidity'})
    for i in ['pressure', 'temperature', 'weather_description', 'wind_direction', 'wind_speed']:
        df = pd.read_csv('Data/'+ i+'.csv')
        print(df.shape)
        print(i)
        climate_new_york_df = pd.concat([climate_new_york_df , df['New York']], axis = 1)
        climate_new_york_df = climate_new_york_df.rename(columns={'New York': i})
    
    return climate_new_york_df

#humidity_nyc = pd.concat(humidity['datetime'] , humidity['New York'], axis = 1)
climate_new_york_df = read_concat_df().fillna(method='ffill')
temp = pd.DatetimeIndex(climate_new_york_df['datetime'])
climate_new_york_df['Date'] = temp.date
climate_new_york_df['Time'] = temp.time
climate_new_york_df['weather_desc_cat_var'] = -99
#df['Age_Group'][df['Age'] > 40] = '>40'

print("before:")
climate_new_york_df.loc[((climate_new_york_df['weather_description'] == 'few clouds')
                            | (climate_new_york_df['weather_description'] == 'scattered clouds')
                            | (climate_new_york_df['weather_description'] == 'broken clouds')
                            | (climate_new_york_df['weather_description'] == 'overcast clouds')), 'weather_desc_cat_var'] = 1
climate_new_york_df.loc[(climate_new_york_df['weather_description'] == 'sky is clear'), 'weather_desc_cat_var'] = 2
climate_new_york_df.loc[(climate_new_york_df['weather_description'] == 'mist')
                            | (climate_new_york_df['weather_description'] == 'haze')
                            | (climate_new_york_df['weather_description'] == 'squalls')
                            | (climate_new_york_df['weather_description'] == 'dust')
                            | (climate_new_york_df['weather_description'] == 'sand/dust whirls'), 'weather_desc_cat_var'] = 3
climate_new_york_df.loc[(climate_new_york_df['weather_description'] == 'drizzle')
                            | (climate_new_york_df['weather_description'] == 'moderate rain')
                            | (climate_new_york_df['weather_description'] == 'light intensity drizzle')
                            | (climate_new_york_df['weather_description'] == 'light rain')
                            | (climate_new_york_df['weather_description'] == 'heavy intensity drizzle')
                            | (climate_new_york_df['weather_description'] == 'heavy intensity rain')
                            | (climate_new_york_df['weather_description'] == 'very heavy rain')
                            | (climate_new_york_df['weather_description'] == 'shower rain')
                            | (climate_new_york_df['weather_description'] == 'light intensity shower rain'), 'weather_desc_cat_var'] = 4




climate_new_york_df.loc[(climate_new_york_df['weather_description'] == 'heavy snow')
                            | (climate_new_york_df['weather_description'] == 'light rain and snow')
                            | (climate_new_york_df['weather_description'] == 'snow')
                            | (climate_new_york_df['weather_description'] == 'light snow')
                            | (climate_new_york_df['weather_description'] == 'freezing rain'), 'weather_desc_cat_var'] = 5


climate_new_york_df.loc[(climate_new_york_df['weather_description'] == 'proximity thunderstorm')
                            | (climate_new_york_df['weather_description'] == 'thunderstorm')
                            | (climate_new_york_df['weather_description'] == 'thunderstorm with rain')
                            | (climate_new_york_df['weather_description'] == 'thunderstorm with heavy rain')
                            | (climate_new_york_df['weather_description'] == 'thunderstorm with light rain')
                            | (climate_new_york_df['weather_description'] == 'proximity thunderstorm with rain')
                            | (climate_new_york_df['weather_description'] == 'thunderstorm with light drizzle')
                            | (climate_new_york_df['weather_description'] == 'heavy thunderstorm'), 'weather_desc_cat_var'] = 6

#print(climate_new_york_df.dropna().head())
climate_new_york_df = climate_new_york_df.dropna()
del climate_new_york_df['datetime']
del climate_new_york_df['weather_description']
del climate_new_york_df['Time']

climate_per_day = climate_new_york_df.groupby(['Date']).median()
print(climate_per_day)
climate_per_day.to_csv("aggregated_climate_per_day.csv", header = True, index = True)
'''
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'few clouds'] = 1
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'sky is clear'] = 2
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'scattered clouds'] = 1
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'broken clouds'] = 1
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'overcast clouds'] = 1
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'mist'] = 3
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'drizzle'] = 4
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'moderate rain'] = 4
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'light intensity drizzle'] = 4
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'light rain'] = 4
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'haze'] = 3
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'heavy snow'] = 5
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'heavy intensity drizzle'] = 4
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'heavy intensity rain'] = 4
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'light rain and snow'] = 5
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'snow'] = 5
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'light snow'] = 5
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'freezing rain'] = 5
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'proximity thunderstorm'] = 6
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'thunderstorm'] = 6
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'thunderstorm with rain'] = 6
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'very heavy rain'] = 4
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'thunderstorm with heavy rain'] = 6
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'thunderstorm with light rain'] = 6
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'squalls'] = 3
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'dust'] = 3
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'proximity thunderstorm with rain'] = 6
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'thunderstorm with light drizzle' ] = 4
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'shower rain'] = 4
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'proximity thunderstorm with drizzle'] = 6
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'light intensity shower rain'] = 4
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'sand/dust whirls' ] = 3
climate_new_york_df['weather_desc_cat_var'][climate_new_york_df['weather_description'] == 'heavy thunderstorm'] = 6
'''









#climate_new_york_df.to_csv("newyork_climate.csv", index = False)
#unique_val = pd.unique(climate_new_york_df['weather_description'])
#np.savetxt('test.txt', unique_val.T, fmt='%-7.2f')
#print(unique_val.T)