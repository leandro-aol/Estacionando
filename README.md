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

## Fazendo deploy no Heroku
**[*Heroku*](https://www.heroku.com)**
**[*Django-Heroku*](https://github.com/gpzim98/django-heroku)**

## Escondendo algumas configurações
* pip install python-decouple
* Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
- `SECRET_KEY=[Your-Secret-Key-Here]`
_Pegue a SECRET_KEY do arquivo settings.py_
- `DEBUG=True`

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

## Arquivos Estáticos
pip install dj-static

### wsgi
* from dj_static import Cling
* application = Cling(get_wsgi_application())

### Settings.py
* STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
* STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

## Crie na raiz do projeto
1. requirements-dev.txt
* pip freeze > requirements-dev.txt

2. requirements.txt
* -r requirements-dev.txt
* gunicorn
* psycopg2

3. Procfile
* web: gunicorn website.wsgi --log-file -

4. runtime.txt
* python-3.7.0

## Criando o app no Heroku
* **[Instale o *Heroku CLI*](https://devcenter.heroku.com/articles/heroku-cli)**
* heroku apps:create [app-name]
_Nesta etapa, lembre-se de pegar o endereço da aplicação!_

## Configure o ALLOWED_HOSTS
Inclua o endereço do seu app no Heroku na variável *ALLOWED_HOSTS* no arquivo *settings.py*
Inclua *apenas o domínio*. Retire a parte do _protocolo_ e as _barras_

## Instale o plugin de configuração do Heroku
* heroku plugins:install heroku-config

### Enviando o arquivo `.env` para o Heroku
_Você deve estar dentro da pasta onde o arquivo *.env* está_
* heroku config:push -a

### Para ver as configurações do Heroku
* heroku config

## Publicando a aplicação no Heroku
* git add .
* git commit -m 'Configuring the app'
* git push heroku master --force

## Criando o Banco de Dados
* heroku run python manage.py migrate

## Criando o usuário admin do Django
* heroku run python manage.py createsuperuser

*******

# Lembretes!

## Você pode precisar de desabilitar o _collectstatic_
* heroku config:set DISABLE_COLLECTSTATIC=1

## Alterando uma configuração específica
* heroku config:set DEBUG=True

## Ferramenta para trabalhar com formulário Bootstrap/Django
pip install django-bootstrap-form

## CRUD
* Create
* Read
* Update
* Delete

## Caminho das requests
* URL
* View
    Models
    Response()

Para acessar alguma view, ela deve ser mapeada no urls.py

## Comandos Git
* `git remote -v` : para verificar os repositórios remotos atuais
* `git remote add [nome] [url]` : para adicionar um repositório remoto
* `git push [nome-remote] [branch]` : fazer um pushing para o remote/branch
* `git remote show _[nome-remote]_` : inspecionar um repositório
