from pypdf import PdfReader

reader=PdfReader(r'C:\Resume.pdf')
text=""

for page in reader.pages:
    text=text+page.extract_text()

print(text)


import pdfplumber

with pdfplumber.open(r'C:\Resume.pdf') as pdf:
    text=''
    for page in pdf.pages:
        text=text+page.extract_text()
    print(text)