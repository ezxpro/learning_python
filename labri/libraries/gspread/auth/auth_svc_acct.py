import gspread
import os

os.chdir(os.path.dirname(__file__))
gc = gspread.service_account('credentials_svc.json')

sh = gc.open('Orçamento mensal - Agosto/2022')

print(sh.sheet1.get('B28'))
