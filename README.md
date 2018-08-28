# ProjetoFinal
Projeto final do curso de Django e Python (Programe Fácil / Udemy)

## [1] Clonar um projeto Git
* Ctrl + Shift + P
* clone
* "url do diretório"
* Escolha a pasta para o projeto

## Criar o diretório do projeto
* mkdir "nome da pasta"
* cd "nome da pasta"

## Habilitar a execução de scripts no processo atual
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

## Criar e ativar um Ambiente Virtual
* python -m venv "nome do ambiente virtual"
    (ex: python -m venv venv)
* .\venv\Scripts\activate

## Atualizando o pip
python -m pip install --upgrade pip

## Instalando o Django
pip install django

## Criar o projeto Django
django-admin startproject "nome do projeto" .
    (O ponto no final da linha é para impedir a criação de uma subpasta com o nome do projeto)

## [2] Criando o repositório Git
* git init
* Crie o arquivo `.gitignore` com o seguinte conteúdo:
```
# See the name for you IDE
.vscode

# If you are using sqlite3
*.sqlite3

# Name of your virtuan env
venv
*pyc
```
* git add .
* git commit -m 'Primeiro commit'

## Escondendo algumas configurações
* pip install python-decouple
* Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
- SECRET_KEY=Your$eCretKeyHere
    (Pegue a SECRET_KEY do arquivo settings.py)
- DEBUG=True

### Settings.py
* from decouple import config
* SECRET_KEY = config('SECRET_KEY')
* DEBUG = config('DEBUG', default=False, cast=bool)

## Configurando o Banco de Dados
* pip install dj-database-url

### Settings.py
* from dj_database_url import parse as dburl

- default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
- DATABASES = {'default': config('DATABASE_URL', default=default_dburl, cast=dburl),}
