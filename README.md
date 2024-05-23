
## Índice  
1. [Banco de Dados](#banco-de-dados)  
2. [Back-end](#back-end)  
3. [Front-end](#front-end)  
4. [Passo a Passo - Compilar TailwindCSS](#passo-a-passo---compilar-tailwindcss)
5. [Implantação](#implantação)  
6. [Práticas de Desenvolvimento](#práticas-de-desenvolvimento)  
7. [CI/CD](#cicd)  
8. [Segurança](#segurança)  
9. [Passo a Passo - Subir local](#passo-a-passo---subir-local)  
10. [Aplicações e Módulos](#aplicações-e-módulos)  
  
  
## Banco de Dados  
O banco de dados preferencial para utilização em projetos é o PostgreSQL.  
  
## Back-end  
O back-end deve ser desenvolvido utilizando Python (3.11.0) com o framework Django (4.2.2).  
  
## Front-end  
O front-end deve ser desenvolvido utilizando Django. Para o estilo e interação do usuário, serão utilizadas as bibliotecas TailwindCSS e AlpineJS. Os http requests são feitos usando a biblioteca HTMX.  
Usa-se a biblioteca django-unfold==0.11.0 para sobrescrever o admin original do Django. Ao instalar essa biblioteca, o AlpineJS e HTMX também são instalados automaticamente.

## Passo a Passo - Compilar TailwindCSS
1. Instalar o [Node.js](https://nodejs.org/en/download)
2. Instalar o TailwindCSS utilizando o comando `npm install -D tailwindcss`
3. Instalar o plugin tw-colors utilizando o comando `npm i -D tw-colors`
4. Executar o código para compilação do CSS:
- 4.1. `npm run tailwind:build` analisa seus arquivos e compila o CSS uma única vez
- 4.2. `npm run tailwind:watch` analisa seus arquivos constantemente e recompila o CSS após cada mudança
  
## Implantação  
Para a implantação de projetos, está sendo utilizado um servidor windows (papocas) devido os projetos da inovação precisarem acessar funcionalidades de automação com utilização de navegadores e o uso do pjeoffice.  
  
## Práticas de Desenvolvimento  
As diretrizes gerais de metodologias ágeis serão seguidas ao longo do desenvolvimento de projetos.  
  
## CI/CD  
O GitLab deve ser usado como a ferramenta de CI/CD. O GitLab é uma plataforma completa de DevOps que cobre todo o ciclo de vida do software.  
  
## Segurança  
A autenticação será realizada preferencialmente via **Azure** no ambiente de produção e no ambiente local via autenticação do django  
  
No ambiente local pode-se utilizar a autenticação propria do django  
```  
AUTHENTICATION_BACKENDS = [  
'django.contrib.auth.backends.ModelBackend', # if you also want to use Django's authentication  
]  
```  
  
  
## Passo a Passo - Subir local  
1. `git clone https://gitlab.jfpb.jus.br/ei/inovacao.git`  
  
2. Atenção para o arquivo settings.py, verificar se está importando o settingslocal `from .settingslocal import *`  
- 2.1. Verificar dentro do arquivo settingslocal se está importando o arquivo config.ini ou outro *.ini qualquer  
- 2.2. Alterar ou criar o arquivo config.ini com as configurações necessárias  
  
  
```  
[postgresqlportallocal]  
ENGINE=django.db.backends.postgresql  
NAME=nome_banco  
USER=user_postgres  
PASSWORD=senha_postgres  
PORT=5432  
```  
  
  
3. Instalar o python 3.11, se não tiver instalado, depois criar ambiente virtual com a versão do python 3.11  
  
- 3.1. `virtualenv --p python311 dir_ambiente_virtual`  
  
4. Ativar o ambiente virtual (`ambiente_virtual/Scripts/activate` ou `ambiente_virtual/bin/activate`) e Instalar o requirements.txt dentro do ambiente virtual anterior criado e ativado. O nome do ambiente virtual ativado ficará entre parênteses.  
  
- 4.1. Por exemplo: (inovacao_3_11) `pip install -U -r requeriments.txt`  
  
5. Criar a base de dados no postgres cujo nome encontra-se no `config.ini` (ex. nome_banco)  
  
6. Se a base de dados for nova, executar a sequencia  
- 6.1. `manage.py migrate` (cria as tabelas)  
- 6.2. `manage.py loaddata user.json` (popula as tabelas com usuários iniciais)  
- 6.3. `manage.py loaddata gestao_pessoas.json` (popula as tabelas com dados referentes a setores e servidores)  
  
  
Obs. O repositório não contém os arquivos settingsprod, settings_ldap  
  
## Aplicações e Módulos  
1. Para criar aplicações novas usa-se  
`manage.py startapp nome_app`  
  
2. Para criar um novo módulo que faz parte dentro da app  
  
- 2.1 É necessário criar uma classe dentro do arquivo models.py, e registrá-lo no admin.py para aparecer no menu.
