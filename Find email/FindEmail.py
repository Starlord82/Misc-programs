import os
import extract_msg
import re
import shutil

os.chdir('C:\\Users\\asafd\\Desktop\\Dropbox\\דרך הנדסה\\הנדסה\\27_00\\2714\\2714-1\\תכתובת')

output_path = 'C:\\Users\\asafd\\Desktop\\Results'

counter = 0

def find_word(file,word):
   global counter
   msg = extract_msg.openMsg(file)
   text = msg.body
   print(f'opening msg {file}')
   if re.search(word, text):
      counter += 1
      shutil.copy(file, output_path)
      print('msg copied')


for folder, subfolder, file in os.walk(os.getcwd()):
   for f in file:
      file_path = folder + "\\" + f
      if re.search(r'\w+.msg', file_path):
         find_word(file_path, "מגרסה")

print(f'{counter} files have been copied')