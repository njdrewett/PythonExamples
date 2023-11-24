#! python3

#1. Find all the CSV files in the current working directory.
#2. Read in the full contents of each file.
#3. Write out the contents, skipping the first line, to a new CSV file.

import csv
import os

csvFiles = []
files = os.listdir('.')
for filename in files:
    if filename.endswith('.csv'):
        print(filename)
        csvFiles.append(filename)

#2. Call Python’s sort() list method to alphabetize the filenames.
csvFiles.sort(key = str.lower)


for csvFilename in csvFiles:
    print('Removing header from ' + csvFilename + '...')
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue # skip first row
        csvRows.append(row)
    csvFileObj.close()
#end forcsvFiles

# Write out the CSV file.
csvFileObj = open('headerRemoved_' + csvFilename, 'w', newline='')
csvWriter = csv.writer(csvFileObj)
for row in csvRows:
    csvWriter.writerow(row)
csvFileObj.close()


