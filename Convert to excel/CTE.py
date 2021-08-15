# CTE - Convert pdf To Excel

# import PyPDF2
import tabula
from tkinter.filedialog import askopenfilename
import os
import camelot
import pandas as pd

filename = askopenfilename()
tables = tabula.io.read_pdf(filename, stream = True)

print(tables)