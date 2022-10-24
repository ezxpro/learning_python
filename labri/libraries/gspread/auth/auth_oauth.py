import gspread
import os

os.chdir(os.path.dirname(__file__))

gc = gspread.oauth(credentials_filename='credentials_oauth.json')

sh = gc.open('Orçamento mensal - Agosto/2022')

print(sh.sheet1.get('B21'))
