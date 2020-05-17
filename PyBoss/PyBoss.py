# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:10:27 2020

@author: theaddies
"""
output_file = './data/employee_data_corrected.csv'
csvpath = './data/employee_data.csv'
employeeData = []
employeeDataNew = []
splitName = []
ssn = []
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

import datetime
import csv
with open(csvpath, newline='') as f:
    reader = csv.reader(f, delimiter = ',')
    for row in reader:
        employeeData.append(row)

#let's split the names first

for i in range(2,len(employeeData)):
    row = employeeData[i]
    row[-1] = us_state_abbrev[row[-1]]
    ssn = str(row[3]).split("-")
    row[3] = "***-**-"+ssn[-1]
    row[2] = datetime.datetime.strptime(str(row[2]), '%Y-%m-%d').strftime('%d/%m/%Y')
    splitName = str(row[1]).split(" ")
    row[1] = splitName[-1]
    row.insert(1, splitName[0])
    #why does the code work with or wihtout the line below.
    employeeData[i] = row
    
employeeData[0][1] = "First Name"
employeeData[0][2] = "Last Name"


print (employeeData)

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerows(employeeData)

