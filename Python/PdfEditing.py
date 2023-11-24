#PDF editing

# Read a pDF

import PyPDF2

pdfFileObj = open('meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print("number of pages:" + str(pdfReader.numPages))

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

pdfFileObj.close()

encryptedPdfReader = PyPDF2.PdfFileReader(open('encryptedminutes.pdf','rb'))
print("Encrypted : " + str(pdfReader.isEncrypted))
pdfReader.decrypt('rosebud')
pageObj = pdfReader.getPage(0)
