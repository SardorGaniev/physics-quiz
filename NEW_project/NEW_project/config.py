from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# База данных postgresql (SERVER)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'phyiscs',
#         'USER': 'kamol',
#         'PASSWORD': '123654qaz',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }