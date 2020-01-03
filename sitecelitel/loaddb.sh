#!/bin/bash

echo Loaded fixture for organization!
python3.7 manage.py loaddata organization/fixtures/organization_data.json
echo Loaded fixture for doctor!
python3.7 manage.py loaddata doctor/fixtures/doctor_data.json
echo Loaded fixture for new!
python3.7 manage.py loaddata new/fixtures/new_data.json
echo Loaded fixture for promotion!
python3.7 manage.py loaddata promotion/fixtures/promotion_data.json
echo Loaded fixture for service!
python3.7 manage.py loaddata service/fixtures/service_data.json
echo Loaded fixture for article!
python3.7 manage.py loaddata article/fixtures/article_data.json
echo Loaded fixture for faq!
python3.7 manage.py loaddata faq/fixtures/faq_data.json
echo Loaded fixture for rusdoc!
python3.7 manage.py loaddata rusdoc/fixtures/rusdoc_data.json
echo Loaded fixture for tag!
python3.7 manage.py loaddata tag/fixtures/tag_data.json
echo Loaded fixture for vacancy!
python3.7 manage.py loaddata vacancy/fixtures/vacancy_data.json
