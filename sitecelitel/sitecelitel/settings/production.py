DEBUG = False           # DEBUG MODE

ALLOWED_HOSTS = ['*']    # your site domen_name
SITE = ['*']

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # Backend for connection with Data Base
        'NAME': 'studio3f_cel2020',                          # Data Base name
        'USER': 'studio3f_cel2020',                          # Name user
        'PASSWORD': 'spR5v&FM',                      # User's password
        'HOST': 'localhost',                          # Host for connection to Data Base
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
