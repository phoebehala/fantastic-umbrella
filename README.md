# fantastic-umbrella
To create Docker Image for our project
docker-compose run web sh -c "django-admin startproject todolist ."

To run the web application
docker-compose up

To access admin panel, first migrate and create a user...
docker-compose run web sh -c "python manage.py makemigrations"

docker-compose run web sh -c "python manage.py migrate"

docker-compose run web sh -c "python manage.py createsuperuser"

To start a todo application
docker-compose run web sh -c "python manage.py startapp todo"


備註
startproject v.s startapp
project like an working environment, we can have multiple apps on it


UserCreationForm() 
from django.contrib.auth.forms import UserCreationForm

{% csrf_token %}
https://docs.djangoproject.com/en/3.2/ref/csrf/


 {{ form.as_p }} 
working-with-form-templates
https://docs.djangoproject.com/en/3.2/topics/forms/#working-with-form-templates
