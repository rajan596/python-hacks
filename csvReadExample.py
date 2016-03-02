# python 3
# CSV File Handeling

import csv

with open('csvFile.csv') as csvFile:
    # simple file read
    #print(csvFile.read())

    # row stored in tuple
    readCSV=csv.reader(csvFile,delimiter=',')

    for row in readCSV:
        print(row)


# Exception Handeling
try:
    with open('example.scv') as file:
        print("Successfully opened file")
except Exception as e:
    print(e)
