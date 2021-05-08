#!/bin/sh
python3 -m venv env
. env/bin/activate
python3 -m pip install -r requirements.txt
python3 manage.py runserver localhost:8000
