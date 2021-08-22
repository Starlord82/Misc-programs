import os
import extract_msg
import re
import shutil
from tkinter import filedialog

input_path = filedialog.askdirectory(title = "Choose folder to search in")
output_path = filedialog.askdirectory(title = "Choose where to copy matches")

counter = 0
search_counter = 0

def find_word(file,word):
   global counter
   global search_counter
   msg = extract_msg.openMsg(file)
   text = msg.body
   print(f'opening msg {file}')
   if re.search(word, text):
      counter += 1
      shutil.copy(file, output_path)
      print('msg copied')
   search_counter += 1


for folder, subfolder, file in os.walk(input_path):
   for f in file:
      file_path = folder + "\\" + f
      if re.search(r'\w+.msg', file_path):
         find_word(file_path, "מגרסה")

print(f'{search_counter} files have been searched')
print(f'{counter} files have been copied')