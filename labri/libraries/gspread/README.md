# Teste GSpread

O GSpread é uma biblioteca para acessar a API do Google Sheets.
Para maiores detalhes, acesse a [documentação oficial](https://docs.gspread.org/)

Todas as informações contidas neste README estão presentes nesta documentação.

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

### Para usuários finais: Usando OAuth Client ID


