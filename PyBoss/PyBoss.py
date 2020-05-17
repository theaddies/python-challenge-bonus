# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:10:27 2020

@author: theaddies
"""
csvpath = './data/employee_data.csv'
employeeData = {}

import csv
with open(csvpath, newline='') as f:
    reader = csv.DictReader(f, delimiter = ',')
    for row in reader:
        employeeData.update(row)

print(employeeData)
