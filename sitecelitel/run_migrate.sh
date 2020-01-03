#!/bin/bash
python3.7 manage.py makemigrations article
python3.7 manage.py makemigrations doctor
python3.7 manage.py makemigrations faq
python3.7 manage.py makemigrations new
python3.7 manage.py makemigrations organization
python3.7 manage.py makemigrations promotion
python3.7 manage.py makemigrations rusdoc
python3.7 manage.py makemigrations service
python3.7 manage.py makemigrations tag
python3.7 manage.py makemigrations vacancy

python3.7 manage.py migrate article
python3.7 manage.py migrate doctor
python3.7 manage.py migrate faq
python3.7 manage.py migrate new
python3.7 manage.py migrate organization
python3.7 manage.py migrate promotion
python3.7 manage.py migrate rusdoc
python3.7 manage.py migrate service
python3.7 manage.py migrate tag
python3.7 manage.py migrate vacancy
