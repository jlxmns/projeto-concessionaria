
## Índice  
1. [Banco de Dados](#banco-de-dados)  
2. [Back-end](#back-end)  
3. [Front-end](#front-end)  
4. [Passo a Passo - Compilar TailwindCSS](#passo-a-passo---compilar-tailwindcss)
5. [Práticas de Desenvolvimento](#práticas-de-desenvolvimento)  
6. [CI/CD](#cicd)   
7. [Passo a Passo](#passo-a-passo)  
8. [Aplicações e Módulos](#aplicações-e-módulos)  
  
  
## Banco de Dados  
O banco de dados preferencial para utilização em projetos é o [PostgreSQL](https://www.postgresql.org/download/windows/).
  
## Back-end  
O back-end deve ser desenvolvido utilizando [Python (3.11.0)](https://www.python.org/downloads/release/python-3110/) com o framework Django (4.2.2).
  
## Front-end  
O front-end deve ser desenvolvido utilizando Django. Para o estilo e interação do usuário, serão utilizadas as bibliotecas TailwindCSS e AlpineJS. Os AJAX requests podem ser feitos usando a biblioteca HTMX.  
Usa-se a biblioteca django-unfold==0.24.0 para sobrescrever o admin original do Django. Ao instalar essa biblioteca, o AlpineJS e HTMX também são incorporados automaticamente.

## Passo a Passo - Compilar TailwindCSS
1. Instalar o [Node.js](https://nodejs.org/en/download)
2. Instalar o TailwindCSS e dependências do projeto utilizando o comando `npm install` na pasta que contém o package.json.
3. Executar o código para compilação do CSS:
- 3.1. `npm run tailwind:build` analisa seus arquivos e compila o CSS uma única vez
- 3.2. `npm run tailwind:watch` analisa seus arquivos constantemente e recompila o CSS após cada mudança
  
## Práticas de Desenvolvimento  
As diretrizes gerais de metodologias ágeis serão seguidas ao longo do desenvolvimento de projetos.  
  
## CI/CD  
O GitHub deve ser usado como a ferramenta de CI/CD. O GitHub é uma plataforma completa de DevOps que cobre todo o ciclo de vida do software. 
  
  
## Passo a Passo
1. Instalar o [Python 3.11.0](https://www.python.org/downloads/release/python-3110/)
2. Instalar o [PostgreSQL](https://www.postgresql.org/download/windows/) e solicitar instalação do pgAdmin4 durante o setup
3. Git clone `https://github.com/jlxmns/projeto-concessionaria.git`
4. Setup do Banco de dados
- 4.1 Criar um usuário e senha no pgAdmin4 (pode deixar o padrão de usuário postgres e senha postgres se quiser)
- 4.2 Criar um banco de dados para ser utilizado no projeto
- 4.3 [Opcional] Importar dados de um backup do banco de dados
- 4.4 Modificar o arquivo database.ini conforme indicação abaixo:
  
  
```  
[postgresqlconcessionarialocal]
ENGINE=django.db.backends.postgresql  
NAME=nome_banco  
USER=user_postgres  
PASSWORD=senha_postgres  
PORT=5432  
```  
  
  
5. Criar ambiente virtual
  
- 5.1. `py -m venv venv`
- 5.2 Caso tenha mais de uma versão do Python, deverá especificar. Utilize `py --list` para checar as versões disponíveis e depois `py -X -m venv venv` onde X é a versão do Python. Ex: `py -3.11 -m venv venv`
  
4. Ativar o ambiente virtual (`venv/Scripts/activate` ou `venv/bin/activate.ps1` se estiver usando o PowerShell) e instalar o requirements.txt dentro do ambiente virtual anterior criado e ativado. O nome do ambiente virtual ativado ficará entre parênteses.  
  
- 4.1. Por exemplo: (venv) `pip install -U -r requirements.txt`  
  
5. Se o banco de dados for novo ou se houver novas migrações, realizar migrações: 
- 5.1. `py manage.py migrate` (cria as tabelas)
- 5.2. `py manage.py createsuperuser` (cria um superuser)
  
## Aplicações e Módulos  
1. Para criar aplicações novas usa-se  
`py manage.py startapp nome_app`  
  
2. Para criar um novo módulo que faz parte dentro da app  
  
- 2.1 É necessário criar uma classe dentro do arquivo models.py, e registrá-lo no admin.py para aparecer no menu.
- 2.2 O módulo onde a maior parte do código será desenvolvido deve ser o site_concessionaria.
