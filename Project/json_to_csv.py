# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:50:23 2020

@author: HK
"""

import json 
import csv 
  
  
# Opening JSON file and loading the data 
# into the variable data 
with open('C:/Users/HK/Desktop/data/history.json') as json_file: 
    data = json.load(json_file) 
  
employee_data = data['data'] 
  
# now we will open a file for writing 
data_file = open('C:/Users/HK/Desktop/data/history_csv.csv', 'w') 
  
# create the csv writer object 
csv_writer = csv.writer(data_file) 
  
# Counter variable used for writing  
# headers to the CSV file 
count = 0
  
for emp in employee_data: 
    if count == 0: 
  
        # Writing headers of CSV file 
        header = emp.keys() 
        csv_writer.writerow(header) 
        count += 1
  
    # Writing data of CSV file 
    csv_writer.writerow(emp.values()) 
  
data_file.close() 