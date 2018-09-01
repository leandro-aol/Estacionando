# ProjetoFinal
Projeto final do curso de Django e Python (Programe Fácil / Udemy)

## Criar o diretório do projeto
* mkdir [nome-da-pasta]
* cd [nome-da-pasta]

## Git
### [1] Clonar um projeto Git
* Ctrl + Shift + P
* clone
* "url do diretório"
* Escolha a pasta para o projeto

### [2] Criando o repositório Git
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

## Habilitar a execução de scripts no processo atual
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

## Criar e ativar um Ambiente Virtual
* `python -m venv [nome-do-ambiente-virtual]` : _python -m venv venv_
* `.\venv\Scripts\activate`

## Atualizando o pip
python -m pip install --upgrade pip

## Instalando o Django
pip install django

### Criar o projeto Django
`django-admin startproject [nome-do-projeto] .`
_O ponto no final da linha é para impedir a criação de uma subpasta com o nome do projeto_

### Comandos em manage.py
* `python manage.py createsuperuser` : para criar um super usuário

* `python manage.py startapp [nome-do-app]` : criar uma app

* `python manage.py makemigrations` : identifica as alterações a serem feitas no banco
* `python manage.py migrate` : realiza estas alterações
* `python manage.py runserver` : executa o servidor da aplicação

## Instalando o PyLint
* pip install pylint-django
* Adicione nas configurações de usuário do VSCode
```
"python.linting.pylintArgs": [
    "--load-plugins=pylint_django"
],
```

*******

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

## Fazendo deploy no Heroku
**[*Heroku*](https://www.heroku.com)**
**[*Django-Heroku*](https://github.com/gpzim98/django-heroku)**

### Enviar através do Git
git push heroku master

### Adicionar em ALLOWED_HOSTS
estacionando.herokuapp.com

## Ferramenta para trabalhar com formulário Bootstrap/Django
pip install django-bootstrap-form

*******

# Lembretes!

## CRUD
* Create
* Read
* Update
* Delete

## Caminho das requests
1. urls.py
2. views.py
Para acessar alguma view, ela deve ser mapeada no urls.py

## Comandos Git
* `git remote -v` : para verificar os repositórios remotos atuais
* `git remote add [nome] [url]` : para adicionar um repositório remoto
* `git push [nome-remote] [branch]` : fazer um pushing para o remote/branch
* `git remote show _[nome-remote]_` : inspecionar um repositório