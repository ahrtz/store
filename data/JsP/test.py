import pandas as pd
import xlrd
from googletrans import Translator
# import sys
# print(sys.executable)

word='안녕'

trans = Translator()
result = trans.translate(word, dest='en')
print(result.text)