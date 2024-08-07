import fitz
import PyPDF2
import os
import shutil
from tkinter import filedialog
from docx import Document
import re

path = filedialog.askdirectory(title = "Choose folder to search in")
output_path = filedialog.askdirectory(title = "Choose where to copy matches")
keyword = input("Enter Keyword you want to search: ")
for folder, subfolder, file in os.walk(path):
    for f in file:
        if f.endswith('.pdf'): 
            with open(folder + "//" + f, 'rb') as file_name:
                print(f'openeing file {f}')
                reader = PyPDF2.PdfReader(file_name)
                for page in reader.pages:
                       if keyword in page.extract_text():
                            file_path = folder + "\\" + f
                            shutil.copy(file_path, output_path+"\\"+f)
                            print(file)
                            pass
            
        elif f.endswith('.docx'):
                print(f'openeing file {f}')
                document = Document(folder + "\\" + f)
                alltext = []
                for p in document.paragraphs:
                    alltext.append(p.text)
                t = " ".join(alltext)
                if re.search(keyword, t):
                    file_path = folder + "\\" + f
                    shutil.copy(file_path, output_path+"\\"+f)
                    print(file)
                    pass
        else:
            continue
            
os.startfile(output_path)