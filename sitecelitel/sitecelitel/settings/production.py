DEBUG = True           # DEBUG MODE

ALLOWED_HOSTS = ['*']    # your site domen_name

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # Backend for connection with Data Base
        'NAME': 'studio3f_test2',                          # Data Base name
        'USER': 'studio3f_test2',                          # Name user
        'PASSWORD': 'studio3f_test2',                      # User's password
        'HOST': 'localhost',                          # Host for connection to Data Base
    }
}
