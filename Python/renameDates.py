#! python3

# Renaming Files with American-Style Dates to European-Style Dates

# 1. searches all the filenames in the current working directory for American-style dates.
# 2. When one is found, it renames the file with the month and day swapped to make it European-style.
#This means the code will need to do the following:
#1. Create a regex that can identify the text pattern of American-style dates.
#2. Call os.listdir() to find all the files in the working directory.
#3. Loop over each filename, using the regex to check whether it has a date.
#4. If it has a date, rename the file with shutil.move()

import shutil
import os
import re

# create a regex pattern that matches files with the American date

datePattern = re.compile(r"""^(.*?) # all the text before the date
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)

# loop over files in the working directory
for americanDateFilename in os.listdir('.'):
    match = datePattern.search(americanDateFilename)


    # skip files without a date
    if match == None:
        continue

    # Get the different parts of the filename
    beforePart = match.group(1)

    monthPart = match.group(2)
    dayPart = match.group(4)
    yearPart = match.group(6)
    afterPart = match.group(8)

    # Form the European-style filename.
    europeanFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absoluteWorkingDirectory = os.path.abspath('.')
    americanFilename = os.path.join(absoluteWorkingDirectory,americanFilename)
    europeanFilename = os.path.join(absoluteWorkingDirectory, europeanFilename)

    # rename the files
    print(f'Remaining "{americanFilename}" to "{europeanFilename}"...')
    #shutils.move(americanFilename,europeanFilename)


