import gspread
import os

# muda diretório de trabalho atual (cwd) para o mesmo
# do script. Necessário (pelo menos no Windows) para
# evitar que o Python abra em diretórios arbitrários
os.chdir(os.path.dirname(__file__))

# concatena o caminho atual com o das credenciais na subpasta "auth/"
path_sc_cred = os.path.join(os.getcwd(), "auth/", "credentials_svc.json")

# autentica usando a conta de serviços definida nas credenciais
gc = gspread.service_account(path_sc_cred)

# É possível abrir a planilha por nome
sh = gc.open("Teste GSpread")

# armazena a primeira planilha do arquivo
worksheet = sh.get_worksheet(0)

# Imprimindo valor de uma célula
print("Imprimindo o valor de uma célula pelo nome da célula")
val = worksheet.acell("A2").value
print(val)

# Imprimir valor passando coordenadas na planilha
print("\nImprimindo o valor de uma célula por coordenada")
val = worksheet.cell(2, 2).value
print(val)

# Imprimindo todos valores de uma coluna/linha
print("\nImprimir todos os valores de uma coluna")
val_list = worksheet.col_values(1)
for v in val_list:
    print(str(v))

# Também é possível abrir uma planilha por link ou por ID. 
# Segue um exemplo utilizando o ID
print("A próxima planilha será aberta usando seu ID")
sh = gc.open_by_key("1ZXcy16kY7LrR7A4on0refgbR3ldyoeT9S_xzLj5c7Dk")
worksheet = sh.get_worksheet(1)
val_list = worksheet.col_values(1)
for v in val_list:
    print(str(v))


