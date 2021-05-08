#! /bin/sh
python -m venv virtualenv
. virtualenv/Scripts/activate
python -m pip install -r requirements.txt
python manage.py runserver localhost:8000