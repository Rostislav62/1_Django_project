import os
from pathlib import Path

# Путь к корневой директории проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'pages', 'templates', 'flatpages')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # Добавлено для медиа-файлов
            ],
        },
    },
]


# Безопасный ключ (не используйте его в реальных проектах)
SECRET_KEY = 'django-insecure-...'

# Режим отладки
DEBUG = True

# Допустимые хосты
ALLOWED_HOSTS = []

# Установленные приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',  # Приложение для статических страниц
    'django.contrib.sites',
    'django.contrib.flatpages'
]

# Средства промежуточного программного обеспечения
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Настройки URL
ROOT_URLCONF = 'my_site.urls'


# Настройки WSGI
WSGI_APPLICATION = 'my_site.wsgi.application'

# Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Настройки паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Язык и временная зона
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# URL для статических файлов
STATIC_URL = '/static/'


# Путь до директории, содержащей ваши статические файлы
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'my_site', 'pages', 'static')]


LOGIN_URL = '/admin/login/'  # Ссылка на страницу логина