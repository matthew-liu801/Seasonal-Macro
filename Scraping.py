import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import csv
import openpyxl
from pathlib import Path

df1 = pd.read_excel("/Users/matth/Downloads/CPIAUCNS.xlsx")
df2 = pd.read_excel("/Users/matth/Downloads/CPILFENS.xlsx")


hello=[1:13, 17:24]

for i in hello:
    print(i)

hello

"""
#All CPI data is NOT seasonally adjusted (NS)
data1 = Path('Downloads', 'CPIAUCNS.xls')
data2 = Path('Downloads', 'CPILFENS.xls')

#Data is labeled 'CPI_[first year]_[all or missing items]_[urban/not]' 
CPI_1913_all_urban = openpyxl.load_workbook(data1)
CPI_1957_FE_urban = openpyxl.load_workbook(data2)

ws1 = CPI_1913_all_urban.active
"""





