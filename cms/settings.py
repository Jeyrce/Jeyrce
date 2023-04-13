"""
Django settings for cms project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import \
    os, \
    re
from pathlib import \
    Path

import \
    pymysql

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
pymysql.install_as_MySQLdb()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ac0&5&4udu(c&ct7jybtz2$oq+qk4m+(qb++ab5zww&x4n4n)4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "lujianxin.com",
    "cms.lujianxin.com",
    "127.0.0.1",
]

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "cms",
    "django_celery_beat",
    "django_celery_results",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
if DEBUG: MIDDLEWARE.extend(
    (
        "cms.middlewares.TracebackMiddleware",
    )
)

ROOT_URLCONF = 'cms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "tmpl",
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.tz',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'cms.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    },
    'x': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('CMS_DB_NAME', 'cmdb'),
        'USER': os.getenv('CMS_DB_USERNAME', 'cms'),
        'PASSWORD': os.getenv('CMS_DB_PASSWORD', 'cms'),
        'HOST': os.getenv('CMS_DB_HOST', 'mysql'),
        'PORT': os.getenv('CMS_DB_PORT', '3306'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

MEDIA_URL = 'cc60670e74e943979cdef4838a2dac72/'
MEDIA_ROOT = BASE_DIR / "media"
# MEDIA_ROOT = "/var/lib/cms/"
STATIC_URL = 'b21f9c86fe9b4f95919db5e36e1cef3a/'
STATIC_ROOT = BASE_DIR / 'assets'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ADMINS = [
    (
        'jeyrce',
        'jeyrce@gmail.com',
    ),
]

# session

# server
SERVER_EMAIL = "jeyrce@163.com"
EMAIL_HOST = "smtp.163.com"
EMAIL_PORT = 25
EMAIL_USE_LOCALTIME = False
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None
EMAIL_TIMEOUT = None
DEFAULT_FROM_EMAIL = "jeyrce@163.com"
EMAIL_SUBJECT_PREFIX = "[CMS] "
DISALLOWED_USER_AGENTS = [
    re.compile(r"^Python*"),
]
# 0 means Sunday, 1 means Monday...
FIRST_DAY_OF_WEEK = 1
SESSION_COOKIE_AGE = 60 * 60 * 24 * 3
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# The cache backends to use.
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    },
    "redis": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.getenv("CMS_CACHE_CONN", "redis://redis:6379/7"),
    },
}
CACHE_MIDDLEWARE_KEY_PREFIX = "cache"
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_ALIAS = "default"

AUTH_USER_MODEL = "auth.User"
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]
LOGOUT_REDIRECT_URL = "/"

# simpleui
SIMPLEUI_HOME_TITLE = '管理后台'
SIMPLEUI_LOGIN_PARTICLES = False
SIMPLEUI_ANALYSIS = False
SIMPLEUI_HOME_ACTION = True
SIMPLEUI_HOME_QUICK = True
SIMPLEUI_HOME_INFO = False
SIMPLEUI_INDEX = 'https://lujianxin.com/'
SIMPLEUI_LOADING = True

# 自定义配置
ADMIN_SITE_URL = "8526c34da62c45f5820928c793b86163/"  # 采用重定向到这个地址，避免探测器很容易找到管理后台url

# celery
CELERY_BROKER_URL = os.getenv("CMS_CELERY_BROKER_URL", 'redis://:redis@redis:6379/8')
BROKER_URL = CELERY_BROKER_URL
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_TASK_RESULT_EXPIRES = 60 * 20
CELERY_ACCEPT_CONTENT = ["msgpack", "pickle"]
CELERY_ACKS_LATE = True
CELERY_MESSAGE_COMPRESSION = 'zlib'
CELERYD_TASK_TIME_LIMIT = 3600
CELERYD_CONCURRENCY = 4
CELERYD_PREFETCH_MULTIPLIER = 4
CELERYD_MAX_TASKS_PER_CHILD = 40
CELERY_DEFAULT_QUEUE = "default"
CELERY_QUEUES = {
    "default": {
        "exchange": "default",
        "exchange_type": "direct",
        "routing_key": "default"
    },
    "topicqueue": {
        "routing_key": "topic.#",
        "exchange": "topic_exchange",
        "exchange_type": "topic",
    },
    "task_eeg": {
        "exchange": "tasks",
        "exchange_type": "fanout",
        "binding_key": "tasks",
    },
}
