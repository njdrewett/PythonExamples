# PDF Combining pages

# This program will do the following
# 1. Find all PDF files in the current working directory.
# 2. Sort the filenames so the PDFs are added in order.
# 3. Write each page, excluding the first page, of each PDF to the output file


import PyPDF2
import os

#1. Call os.listdir() to find all the files in the working directory and remove any non-PDF files.
pdfFiles = []
files = os.listdir('.')
for filename in files:
    if filename.endswith('.pdf'):
        print(filename)
        pdfFiles.append(filename)
#2. Call Python’s sort() list method to alphabetize the filenames.
pdfFiles.sort(key = str.lower)

#3. Create a PdfFileWriter object for the output PDF.
pdfWriter = PyPDF2.PdfFileWriter()

#4. Loop over each PDF file, creating a PdfFileReader object for it.
for pdfFile in pdfFiles:
    print("pdfFile" + pdfFile)
    pdfFileObj = open(pdfFile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    #5. Loop over each page (except the first) in each PDF file.
    for pageNum in range(1, pdfReader.numPages):
        pageObject = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObject)


# TODO: Save the resulting PDF to a file.

#6. Add the pages to the output PDF.
pdfOutputFile = open('combined.pdf','wb')

#7. Write the output PDF to a file named
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()



