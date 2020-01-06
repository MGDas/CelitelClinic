#!/bin/bash

python3.7 manage.py dumpdata --format=json --indent=4 --natural-primary article > article/fixtures/article_data.json
echo Create fixture for article!
python3.7 manage.py dumpdata --format=json --indent=4 --natural-primary doctor > doctor/fixtures/doctor_data.json
echo Create fixture for doctor!
python3.7 manage.py dumpdata --format=json --indent=4 --natural-primary faq > faq/fixtures/faq_data.json
echo Create fixture for faq!
python3.7 manage.py dumpdata --format=json --indent=4 --natural-primary new > new/fixtures/new_data.json
echo Create fixture for new!
python3.7 manage.py dumpdata --format=json --indent=4 --natural-primary organization > organization/fixtures/organization_data.json
echo Create fixture for organization!
python3.7 manage.py dumpdata --format=json --indent=4 --natural-primary promotion > promotion/fixtures/promotion_data.json
echo Create fixture for promotion!
python3.7 manage.py dumpdata --format=json --indent=4 --natural-primary rusdoc > rusdoc/fixtures/rusdoc_data.json
echo Create fixture for rusdoc!
python3.7 manage.py dumpdata --format=json --indent=4 --natural-primary service > service/fixtures/service_data.json
echo Create fixture for service!
python3.7 manage.py dumpdata --format=json --indent=4 --natural-primary tag > tag/fixtures/tag_data.json
echo Create fixture for tag!
python3.7 manage.py dumpdata --format=json --indent=4 --natural-primary vacancy > vacancy/fixtures/vacancy_data.json
echo Create fixture for vacancy!
