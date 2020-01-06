command = '/home/projects/CelitelClinic/venv/bin/gunicorn'
pythonpath = '/home/projects/CelitelClinic/sitecelitel/'
bind = '127.0.0.1:8000'
workers = 5
user = 'mgdas'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=sitecelitel.settings.base'
