# PINFOOD SERVER

API que fornece endpoints para os serviços da pinfood

## Environment:
- Python version: 3.7
- Django version: 3.0.6
- Django REST framework version: 3.11.0

##Configurações Iniciais

* Iniciar ambiente

```shell script
$ python -m venv .venv
$ source .venv/bin/activate (linux) ou .venv/Scripts/activate.bat (windows)
$ pip install -r requirements.txt
```

* Executar Migrations

```shell script
$ python manage.py migrate
```

* Criar arquivo de migração com django

```shell script
$ python manage.py makemigrations
```

---
##Banco De Dados: MYSQL

Nós indicamos utilizar o docker nas configurações de banco de dados do projeto local.

```dockerfile
docker run -p 3306:3306 --name pinfood -e MYSQL_ROOT_PASSWORD=123 -d mysql
```

As configurações ficam no arquivo settings.py, seguindo o seguinte dicionário:

```python
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'pinfood',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
```
---
