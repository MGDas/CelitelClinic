#!/bin/bash
source /home/mgdas/projects/CelitelClinic/venv/bin/activate
exec gunicorn  -c "/home/mgdas/projects/CelitelClinic/sitecelitel/sitecelitel/gunicorn_config.py" sitecelitel.wsgi
