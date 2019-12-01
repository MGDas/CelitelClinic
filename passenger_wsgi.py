# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/s/studio3f/test2.studiovector.art//sitecelitel')
sys.path.insert(1, '/home/s/studio3f/.local/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'sitecelitel.settings.base'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
