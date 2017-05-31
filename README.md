# joel-qs-api (joel_qs_api)

_REST API for "questions" application, using django-rest-framework_


## Basic Requirements

This project was tested using Python 3.5. (Specifically, it was tested on a Ubuntu 16.04 system using the standard version of Python 3.) The `pip` requirements file is requirements.txt.


## Created from a template

Using a Heroku template to create a new Django app was easy:

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld


## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ heroku rename
    $ git push heroku master

    $ heroku run python manage.py migrate


## License: MIT


## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
