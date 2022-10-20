# Teste GSpread

O GSpread é uma biblioteca para acessar a API do Google Sheets.
Para maiores detalhes, acesse a [documentação oficial](https://docs.gspread.org/)

Todas as informações contidas neste README estão presentes nesta documentação.

## Instalando o gspread

Para poder utilizar a biblioteca, você deve instalá-la rodando o comando:
```
pip install gspread
```

## Autenticação e Autorização com GSpread

O processo de autenticação e/ou autorização com o GSpread é bem simples, e pode ser feito de duas maneiras, via OAuth (autorização) ou via Service Account (autenticação.)

- Se você pretende acessar as planilhas em nome de um bot, utilize uma Conta de Serviço 
- Se você pretende acessar planilhas em nome de usuários (incluindo sua própria conta), utilize a autorização via OAuth

No caso do GSpread, a diferença entre os dois processos é que autorização (OAuth) acessa a planilha em nome do usuário utilizando a aplicação, e portanto este deverá autorizar o acesso da aplicação – através de uma janela que será aberta no navegador – aos arquivos armazenados na conta Google do usuário.

Já o processo de autenticação acontece através de um tipo especial de conta google (Conta de Serviço), e se dá em nome de um bot ou script, em suma, um agente não-humano. Como esta é uma conta separada, por padrão ela não tem acesso à nenhuma planilha até que você as compartilhe com a conta do Bot, como se fosse uma conta Google qualquer. Em contrapartida, scripts que usem o esta opção não requerem nenhuma interação do usuário para acessar as planilhas.

Caso tenha interesse, você pode ler mais sobre a diferença entre os processos de [Autorização]() e [Autenticação](). 

### Ativando as APIs do Google

Antes de fazer a autorização ou autenticação, você precisa acessar o [Console do Desenvolvedor do Google](https://console.developers.google.com/), criar um projeto e habilitar o uso das APIs do Google Drive e Google Planilhas neste projeto.

Para isso:
1. Acesse o [Console de Desenvolvedor do Google](https://console.developers.google.com/)
2. Crie um projeto, clicando no botão "Criar Projeto", ou clicando no dropdown `Selecione um projeto > Novo Projeto`
![Criando o projeto](img/1_cria_projeto.png)
3. Preencha o formulário e crie o projeto. Organização e local são campos opcionais
4. Após criado o projeto, selecione-o no dropdown mencionado.
5. No lado esquerdo da tela, clique em `APIs e serviços > APIs e serviços ativados`
![Dashboard de APIs](img/2_api_dashboard.png)
6. Clique em `Ativar APIs e Serviços`, selecione as APIs Google Drive API e Google Sheets API e ative-as.
![Ativando APIs](img/3_ativar_apis.png)

### Para bots e scripts automatizados: usando uma Conta de Serviço
A conta de serviço é um tipo especial de conta cujo propósito é representar um usuário não humano que precise autenticar e autorizar o acesso à dados nas APIs do Google.

Como esta é uma conta separada, por padrão ela não tem acesso à nenhuma planilhar até que você compartilhe-as com essa conta, como faria com qualquer outra conta Google.

Veja como adquirir uma:
1. [Ative o acesso da API no projeto](#ativando-as-apis-do-google) as APIs do Google)
2. Acesse a opção `APIs e Serviços > Credenciais`
![Menu credenciais](img/auth_sa/1_credenciais.png)`
3. Clique em `Criar Credenciais > Conta de serviço`
![Criar Credenciais](img/auth_sa/2_criar_credenciais.png)
4. Preencha o formulário e clique em concluir. O endereço do campo central será usado para compartilhar planilhas com a conta de serviço
![criando conta de serviço](img/auth_sa/3_form_cred_cs.png)
5. Clique em `Gerenciar contas de serviço` acima de Contas de Serviço.
6. No menu de ações, do lado direito do endereço da conta, clique em "Gerenciar chaves"
![gerenciar chaves](img/auth_sa/4_gerenciar_chaves.png)
7. Clique em `Adicionar chave > Criar nova Chave > JSON` e depois clique em `Criar`

Um prompt aparecerá para que você efetue o download das credenciais no formato JSON, com a seguinte estrutura:
```
{
    "type": "service_account",
    "project_id": "api-project-XXX",
    "private_key_id": "2cd … ba4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
    "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
    "client_id": "473 … hd.apps.googleusercontent.com",
    ...
}
```
Salve o arquivo em algum local seguro, você também precisará do endereço de email indicado no camo `client_email`. 

Para maior facilidade de uso é recomendável que você salve o arquivo com um nome diferente daquele gerado aleatóriamente no momento do download. Neste guia, usaremos o nome `service_account.json`

8. **Muito Importante!** Vá até sua planilha e compartilhe-a com o *client_email* do passo acima. Se você não fizer isso, receberá o erro `gspread.exceptions.SpreadsheetNotFound` quando tentar acessar a planilha no seu código
   
9.  Mova o arquivo baixado para `~/.config/gspread/service_account.json` (UNIX/Linux). Usuários do Windows devem utilizar `%APPDATA%\gspread\service_account.json` 
PS: estes são os caminhos nos quais o gspread busca as credenciais por padrão, mas você pode indicar um caminho de sua preferência no código.

10. Crie um arquivo Python com esse código:
```
import gspread

gc = gspread.service_account()

sh = gc.open("Example spreadsheet")

print(sh.sheet1.get('A1'))
```

Como uma curiosidade, esse é o código da função `service_account()`:
```
from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'path/to/the/downloaded/file.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)
```

Também há a possibilidade de passar as credenciais como um dicionário:
```
import gspread

credentials = {
    "type": "service_account",
    "project_id": "api-project-XXX",
    "private_key_id": "2cd … ba4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
    "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
    "client_id": "473 … hd.apps.googleusercontent.com",
    ...
}

gc = gspread.service_account_from_dict(credentials)

sh = gc.open("Example spreadsheet")

print(sh.sheet1.get('A1'))
```

### Para usuários finais: Usando OAuth Client ID

1. [Ative o acesso da API no projeto](#ativando-as-apis-do-google) as APIs do Google)
2. No lado esquerdo da tela, clique no menu e em seguida em `Tela de permissão OAuth`
3. Preencha o formulário OAuth
    1. **Tipo do app:**  leia a descrição do tipo de usuário do aplicativo (Interno ou Externo) e escolha uma das opções. Contas internas só estão disponíveis para usuários com assinatura/versão de testes do Google Workspace. Por padrão, este guia usa a opção de usuário **Externo**:
    ![selecionar tipo de usuário](img/oauth/1_user_type.png)
    2. **Descrição do App:** dê um nome para seu aplicativo, informe um email para suporte e um email para contato. Opcionalmente, nesta tela você pode adicionar um logotipo para o app e restringir o acesso ao app apenas para apenas alguns domínios. Por padrão, deixaremos todas estas opções em branco:
    ![informações do aplicativo](img/oauth/2_app_info.png)
    
    Estas informações serão visualizadas pelo usuário quando o script for rodado e o navegador for aberto para que o usuário autorize o acesso aos dados da conta google. Exemplo:
    ![exemplo tela oauth](img/oauth/3_oauth_app_example.png)
    3. **Escopos:** Não é necessário preencher esta tela, clique em "salvar e continuar"
    4. **Usuários de teste:** aqui você deve adicionar o endereço de email dos usuários finais que terão permissão acesso à aplicação durante a fase de teste. Normalmente, este será o seu proprio email. Após preencher esta tela, clique "Salvar e Continuar"
4. Acesse `APIs e Serviços > Credenciais`
5. Clique em `Criar credenciais > ID do cliente OAuth`
![autorização OAuth](img/oauth/4_oauth_creds.png)
6. Selecione a opção `App para computador` e digite um nome para o aplicativo. e clique em "Criar".
 É importante selecionar a opção correta, outros tipos de aplicativos requerem processos diferentes para autorização
![tipo de cliente](img/oauth/5_type_of_client.png)
7. Faça o download do arquivo JSON. Reomenda-se salvá-lo em `~/.config/gspread/service_account.json` (UNIX/Linux). Usuários do Windows devem utilizar `%APPDATA%\gspread\service_account.json`, pois por padrão o gspread procura as credenciais nestes caminhos.
8. Crie um arquivo Python com este código
```
import gspread

gc = gspread.oauth()

sh = gc.open("Example spreadsheet")

print(sh.sheet1.get('A1'))
```
Uma vez que você rodar o código, uma janela do navegador será aberta