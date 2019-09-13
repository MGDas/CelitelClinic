DEBUG = False           # DEBUG MODE

ALLOWED_HOSTS = ['*']    # your site domen_name

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # Backend for connection with Data Base
        'NAME': '',                          # Data Base name
        'USER': '',                          # Name user
        'PASSWORD': '',                      # User's password
        'HOST': '',                          # Host for connection to Data Base
        'PORT': '',                          # Port maybe not use
    }
}
