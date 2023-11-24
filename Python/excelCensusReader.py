#! python3

# Excel spreadhseet processing

#1. Reads the data from the Excel spreadsheet
#2. Counts the number of census tracts in each county
#3. Counts the total population of each county
#4. Prints the results

import openpyxl
import pprint

#1. Open and read the cells of an Excel document with the openpyxl module.
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}
#2. Calculate all the tract and population data and store it in a data structure.
# TODO: Fill in countyData with each county's population and tracts.
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    population = sheet['D' + str(row)].value

    countyData.setdefault(state, {})
    # Make sure the key for this county in this state exists.
    countyData[state].setdefault(county,{'tracts':0, 'population':0})

    # Each row represents one census tract, so increment by one.
    countyData[state][county]['tracts'] + 1

    #increase the county population from that in the spreadsheet
    countyData[state][county]['population'] += int(population)

#3. Write the data structure to a text file with the .py extension using the
#pprint module.
print('Writing results...')
resultFile = open("census2010.txt",'w')
resultFile.write('All Data = ' + pprint.pformat(countyData))
resultFile.close()
print('Done')

