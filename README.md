# joel-qs-api (joel_qs_api)

_REST API for "questions" application, using django-rest-framework_


## Overview

This project provides a Python REST API, consumed by the `[joel-qs](https://github.com/joel-s/joel-qs)` project. Most of the functionality is provided "out of the box" by `django-rest-framework`. The upload feature is "custom" but does not yet have much error handling.

There are two view classes, defined in `questions/views.py`:
- `QuestionViewSet`, based on `rest_framework.viewsets.ModelViewSet`. This provides all the standard REST endpoints (`/questions/...` GET, POST, etc.).
- QuestionsCsvView, based on `rest_frameworkviews.APIView`. This provides an endpoint for uploading a CSV file containing questions (`/questions-csv/`). The user has the option of appending to the existing list of questions or overwriting it.


## Platform Requirements

This project was tested using Python 3.5. (Specifically, it was tested on a Ubuntu 16.04 system using the standard version of Python 3 for that distribution.) The `pip` requirements file is `requirements.txt`.


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
