# CTE - Convert pdf To Excel

# import PyPDF2
import tabula
from tkinter.filedialog import askopenfilename
import os
import camelot
import pandas as pd

filename = askopenfilename()

join duplicate #df.groupby('value')['tempx'].apply(' '.join).reset_index()

df = pd.read_csv(filename)

print(df)