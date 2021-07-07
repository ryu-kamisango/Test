# -*- coding: utf-8 -*-
"""HW10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bEi5XrRJyFTgSJp4tALUYrv-PhRPGMFU
"""

! wget http://minna.ih.otaru-uc.ac.jp/data/sample-re.txt

! cat sample-re.txt

from google.colab import files
import re

with open("sample-re.txt",'r') as F:
 lines = F.readlines()
Strlines = "".join(lines)
m = re.findall("\d{4}年\d{1,2}月\d{1,2}日",Strlines)

with open('New_sample-number.txt','w') as f:
 for l in m:
   f.write(l+'\n')
 files.download('New_sample-number.txt')