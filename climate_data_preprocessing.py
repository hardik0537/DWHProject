# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 17:19:58 2018

@author: Hardik Galiawala
"""
import pandas as pd



crime_data = pd.read_csv('Data/NYPD_Complaint_Data_Historic.csv', nrows = 1000)

del crime_data['CMPLNT_TO_DT']
del crime_data['CMPLNT_TO_TM']
del crime_data['CMPLNT_FR_TM']
print(crime_data.head())




