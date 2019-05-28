import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f8#(k1)9py0*)j6v92!w0fo0b!)v*%_c6&za&#7z(wv-r+e&(4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'suit',
    'smart_selects',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'common',
    'cmdb',
    'architecture',
    'bstype',
    'saltapi',
    'dashboard',
    'kunlun',
    'nested_inline',
    'suit_dashboard',
    'django.contrib.admin.apps.SimpleAdminConfig',
    'import_export',
    'django.contrib.admindocs',
]
# SITE_ID = 1
# IMPORT_EXPORT_USE_TRANSACTIONS = True
# JQUERY_URL = False
# USE_DJANGO_JQUERY = True
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
SUIT = True
ROOT_URLCONF = 'tabops.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tabops.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tabops_south',
        'USER': 'root',
        'PASSWORD': 'ysten',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

#  TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)
STATIC_ROOT = 'static/'
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

    # ('admin', os.path.join(STATIC_ROOT, 'admin').replace('\\', '/')),
    # ('jet', os.path.join(STATIC_ROOT, 'jet').replace('\\', '/')),
    # ('range_filter', os.path.join(STATIC_ROOT, 'range_filter').replace('\\', '/')),
    # ('fonts', os.path.join(STATIC_ROOT, 'fonts').replace('\\', '/')),
    # ('plugins', os.path.join(STATIC_ROOT, 'plugins').replace('\\', '/')),

)
SUIT_CONFIG = {
    'ADMIN_NAME': "TabOps|四川南区",
    'MENU': (
        {'app': 'cmdb', 'icon': 'icon-leaf',
         'models': ('IDCLevel', 'ISP', 'IDC', 'Cabinet', 'Rack', 'Host')},
        {'app': 'kunlun', 'icon': 'icon-th-list'},
        {'app': 'architecture', 'icon': 'icon-book',
         'models': ('wtv', 'bimsboot', 'bimspanel', 'tms', 'epg', 'tptopic', 'pic', 'ppl', 'cosepg', 'nginx', 'bigdata', 'product', 'unionpay', 'lbss', 'exchange', 'sms', 'dangj', 'ub', 'dms2', 'injection', 'ad', 'ndms')},
        {'app': 'bstype', 'icon': 'icon-tags',
         'models': ('bussiness_type', 'service_type',)},
        {'app': 'auth', 'icon': 'icon-lock', 'models': ('user', 'group')},
        {'app': 'admin', 'icon': 'icon-cog'},
    ),
    'LIST_PER_PAGE': 15
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'standard': {
            'format': '%(levelname)s [ %(message)s] %(asctime)s %(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'standard'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/tmp/django.log',
            'formatter': 'standard'
        },
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'default': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

# Log
DEFAULT_LOGGER = 'default'

# Salt
SALT_API_URL = 'https://10.3.32.69:1559/'
SALT_USER = 'tabops'
SALT_PASSWORD = 'tabops'
