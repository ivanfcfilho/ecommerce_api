# e-commerce api

An open source project to build a ecommerce

## Dependencies
  - Python 3.8
  - git
  - rabbitmq (celery broker)

## Build and Run

Create a venv and run

```sh
https://github.com/ZXVentures/cbe_django_ecommerce
cd cbe_django_ecommerce
python manage.py makemigrations
python manage.py migrate
```

### Create a super user with email and password

```sh
python manage.py createsuper
```

### Run development server

```sh
python manage.py runserver
```

## Tests
TODO
