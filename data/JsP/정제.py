import pandas as pd
import xlrd

df =pd.read_excel('논문검색리스트 정제 (1).xls')
print(df['키워드(한국어)'][0])