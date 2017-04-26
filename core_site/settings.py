import os

PRODUCTION = os.environ.get("PRODUCTION", "")
DOCKER = os.environ.get("DOCKER", "")

gettext = lambda s: s
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_ID = 1
SITE = "core"


ALLOWED_HOSTS = [
    "howtokillyourself.org",
    "dev.howtokillyourself.org",
    "localhost",
    "0.0.0.0",
]

# Application definition

INSTALLED_APPS = [
    #'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.sitemaps',
    'django.contrib.sites',

    # libraries
    'taggit',
    'modelcluster',

    # apps
    'suicide_site',
    'articles',

    # wagtail cms
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
]

WAGTAIL_SITE_NAME = 'How to Kill Yourself'

GEOIP_PATH = os.path.realpath(os.path.join(BASE_DIR, "geoip/GeoLiteCity.dat"))

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'core_site.urls'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

CMS_TEMPLATES = (
    ('djangocms/cms.html', 'CMS Template'),
    ('djangocms/cms2.html', 'CMS Template v2'),
)

LANGUAGES = [
    ('en-us', 'English'),
]

WSGI_APPLICATION = 'core_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'suicide_db',
        'USER': 'gregmccoy',
        'PASSWORD': 'Conestoga1',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'images')
MEDIA_URL = "/media/"

STATIC_ROOT = "/var/www/static/"
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "templates/static"),
]

if PRODUCTION:
    DEBUG = False
    from production_settings import *
else:
    DEBUG = True
    SECRET_KEY = '3$0+y($j4@22)e$3c=3j^!#pr&#mdc#%xvrp13b9$g4!kb*af8'

if DOCKER:
    DATABASES["default"]["HOST"] = "db"

