# -*- coding: utf-8 -*-
"""HW8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Va_9ftc8YkKCBvY1gsgLdRT2FMg9yIUy
"""

from google.colab import files
L =["吾輩は猫である。名前はまだ無い。",
"どこで生れたかとんと見当がつかぬ。",
"何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。",
"吾輩はここで始めて人間というものを見た。",
]
#ファイルに書き込む
with open('sample-wagahai.txt','w') as f:
 for l in L:
   f.write(l+'\n')
   print(l)
files.download('sample-wagahai.txt')

from google.colab import drive
drive.mount('/content/drive')
with open('/content/drive/My Drive/034.txt', 'w') as f:
 f.write('034のプログラムで、ファイルを1行書き込む。\n')
 f.write('034のプログラムで、ファイルを2行書き込む。\n')
 !cat /content/drive/My\ Drive/034.txt

with open('/content/drive/My Drive/034.txt', 'w') as f:
 f.write('034のプログラムで、ファイルを1行書き込む。\n')
 f.write('034のプログラムで、ファイルを2行書き込む。\n')

!cat /content/drive/My\ Drive/034.txt

from google.colab import drive
drive.mount('/content/drive')