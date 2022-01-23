import re
import pdfplumber
from collections import defaultdict, namedtuple
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

order_can1 = open("order_can1.txt", "r")
can1 = []
for line in order_can1 :
  stripped_line = line.strip()
  can1.append(stripped_line)
order_can1.close()

order_hydro = open("order_hydro.txt", "r")
hydro = []
for line in order_hydro:
  stripped_line = line.strip()
  hydro.append(stripped_line)
order_hydro.close()

order_line3 = open("order_line3.txt", "r")
line3 = []
for line in order_line3:
  stripped_line = line.strip()
  line3.append(stripped_line)
order_line3.close()

#regular expressions for
#plan number
plan_number_re = re.compile(r'^1\d{6}')
#page number
page_number_re = re.compile(r'(Page)\s\-\s([0-9]+)')

file1 = 'plan_weights2.pdf'
file2 = 'plan_batches2.pdf'
lines = {}
with pdfplumber.open(file1) as pdf:
    pages = pdf.pages
    for page in pdf.pages:
        text = page.extract_text()
        for line in text.split('\n'): 

            page = page_number_re.search(line)
           
            plan = plan_number_re.search(line)
           #initializes search for line criteria
            if page:
                foundpage = page.group(2)
                lines[foundpage] = {}
            elif plan:
                foundplan = plan.group()
                lines[foundpage] = foundplan
         
plan_number_re2 = re.compile(r'(Production Plan)\s\:\s([0-9]+)')
#page number
page_number_re2 = re.compile(r'(Page)\s\:\s([0-9]+)')
flex_list_re = re.compile(r'(Production Plan)(.*)(Pouch)')

flex_list = []

lines2 = {}
with pdfplumber.open(file2) as pdf:
    pages = pdf.pages
    for page in pdf.pages:
        text = page.extract_text()
        for line in text.split('\n'):        
            
            flex = flex_list_re.search(line)
            page = page_number_re2.search(line) 
            plan = plan_number_re2.search(line)
            if flex:
                flex_list.append(plan.group(2))
                continue   
            
            if page:
                foundpage = page.group(2)
                #find plannumber
                # lines2[foundpage] = {}
            elif plan:
                foundplan = plan.group(2)
                lines2[foundpage] = foundplan

#reorder from plannumber:pagenumber
newlines = {y:x for x,y in lines.items()}

newlines2 = {y:x for x,y in lines2.items()}
# print(len(newlines))
# print(len(newlines2))
# combines two dictionaries into one
finalline = defaultdict(list)
for d in (newlines,newlines2):
    for key, value in d.items():
        finalline[key].append(value) 
# print(finalline)

#combines all plannumbers in order
newcans=[]

#removes duplicates
for item in can1:
    if item not in newcans:
        newcans.append(item)
for item in hydro:
    if item not in newcans:
        newcans.append(item)
for item in line3:
    if item not in newcans:
        newcans.append(item)

pdf_path = file1
pdf_path2 = file2

input_pdf = PdfFileReader(pdf_path)
input_pdf2 = PdfFileReader(pdf_path2)

pdf_writer = PdfFileWriter()

for items in newcans:
 
        try:
            #starts at zero!
            findpage2 = int(finalline[items][1]) - 1
            findpage1 = int(finalline[items][0]) - 1
            page2 = input_pdf2.getPage(findpage2)
            pdf_writer.addPage(page2)
            page = input_pdf.getPage(findpage1)
            pdf_writer.addPage(page)
        
        except:
            continue
        
with Path("sample.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)