#!/usr/bin/env python
#coding:utf-8
# Django settings for ws project.

import sys, os, time, random
reload(sys)
sys.setdefaultencoding('utf-8')
BASE_DIR = os.path.join(os.path.dirname(__file__), '../../')
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

SITE_DOMAIN = 'www.eya.cc'
PROJECT = 'www'

DEBUG = True
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('er1c0rz', '282852423@qq.com'),
)

MANAGERS = ADMINS

# PRODUCT DATABASE ENGINE : MYSQL
DATABASES = {
        'default': {
            #'ENGINE': 'lib.db.mysql_pool.mysql',
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': os.path.join(BASE_DIR, '../conf/mysql.ini'),
                # This sets the default storage engine upon connecting to the database.
                #After your tables have been created, you should remove this option.
                #"init_command": "SET storage_engine=INNODB",
            }
        },
    }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, '../public')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://static.eya.cc/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@6zg(p1%)xslqswt#3v(0s8$b=y+eenh$p8&amp;sd_!7yu23ic@(0'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '../public/templates'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    #'django.contrib.comments',
    #'django.contrib.flatpages',
    #'django.contrib.redirects',
    #'django.contrib.sitemaps',

    'captcha',
    #'app.user',
    'app.cms',
    'app.feedback',
    'app.danye',
    'app.stickers',
    'app.photos'
    )

################################################################################

####################################
# TEMPLATE CONTEXT PROCESSORS #
####################################

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    #    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'lib.context.processors.site_info'
    )


##################
# AUTHENTICATION #
##################
#AUTHENTICATION_BACKENDS = ('app.user.backends.UsernameBackend',
#                           'app.user.backends.EmailBackend',
#                           #'app.taobao.backends.TaobaoBackend',
#    )

AUTH_PROFILE_MODULE = 'user.Profile'
LOGIN_URL = 'http://%s/user/login/' % SITE_DOMAIN
LOGOUT_URL = 'http://%s/user/logout/' % SITE_DOMAIN
LOGIN_REDIRECT_URL = 'http://%s/user/' % SITE_DOMAIN

# Active user via email
AUTH_REGISTER_ACTIVE_EMAIL = False
AUTH_REGISTER_ACTIVE_EMAIL_SUBJECT = 'user/register/email/subject.txt'
AUTH_REGISTER_ACTIVE_EMAIL_BODY = 'user/register/email/body.html'
# The number of days a password reset link is valid for
PASSWORD_RESET_TIMEOUT_DAYS = 3
PASSWORD_RESET_EMAIL_SUBJECT = 'user/password/email/subject.txt'
PASSWORD_RESET_EMAIL_BODY = 'user/password/email/body.html'

############
# SESSIONS #
############
#SESSION_COOKIE_DOMAIN = '.%s' % SITE_DOMAIN
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

#########
# CACHE #
#########
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': ['127.0.0.1:11211',],
        'TIMEOUT': 60 * 10,
        'KEY_PREFIX': PROJECT,
        'OPTION': {},
        }
}

#########
# EMAIL #
#########
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'kefu@%s' % SITE_DOMAIN
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_SUBJECT_PREFIX = '[%s]' % SITE_DOMAIN

# E-mail address that error messages come from.
SERVER_EMAIL = EMAIL_HOST_USER
# Whether to send broken-link e-mails.
SEND_BROKEN_LINK_EMAILS = False

#############
# DATABASES #
#############
DATABASE_ROUTERS = []

###############
# DATE_FORMAT #
###############
DATE_FORMAT = "Y年m月d日"
DATETIME_FORMAT = "Y-m-d H:i:s"
TIME_FORMAT = "H:i:s"

URL_VALIDATOR_USER_AGENT = 'Er1c0rz Projects(1.4) (http://%s) Auth: Er1c0rz'  % SITE_DOMAIN

# ckeditor
ADMIN_JS = [
    #'%sjs/jquery-1.8.0.min.js' % MEDIA_URL,
    'http://code.jquery.com/jquery.min.js',
    '%sckeditor/ckeditor.js' % MEDIA_URL,
    '%sjs/ckeditor/admin.js' % MEDIA_URL,
    ]

###############
# UPLOAD FILE #
###############
UPLOAD_DIR = 'upload'
UPLOAD_IMAGE_THUMB_DIR = 'thumb'

def upload_to(instance, file):
    """yy-mm-dd as file folder, and HMS as file name"""
    path = "%s/%s" % (UPLOAD_DIR, time.strftime("%Y%m%d"))
    params = file.split('.')
    #add random int feed
    name = '%s%s.%s' % (time.strftime("%H%M%S"),
                        random.randint(100,1000),
                        params[-1].lower())
    return '%s/%s' % (path, name)
UPLOAD_TO = upload_to

#load and add customer template filter
from django import template
template.add_to_builtins('lib.template.filter.defaultfilters')
template.add_to_builtins('lib.template.filter.defaulttags')
template.add_to_builtins('lib.template.filter.default')
template.add_to_builtins('lib.template.filter.image')
template.add_to_builtins('lib.template.filter.cms')

################
# override url #
################

ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda u: "/user/%s/" % u.id
}


#########################
# Django simple captcha #
#########################
CAPTCHA_FONT_SIZE = 24
CAPTCHA_BACKGROUND_COLOR = "#fcfcfc"
CAPTCHA_FOREGROUND_COLOR = "#000000"
CAPTCHA_LETTER_ROTATION = (-20,20)
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots','captcha.helpers.noise_arcs',)
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots',)
#CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_OUTPUT_FORMAT = u'%(text_field)s %(image)s %(hidden_field)s'


#######
# LOG #
#######
#LOG_DIR = os.path.join(BASE_DIR, '../log')
#
#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': True,
#    'formatters': {
#        'standard': {
#            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
#        },
#        },
#    'filters': {},
#    'handlers': {
#        'mail_admins': {
#            'level': 'ERROR',
#            'class': 'django.utils.log.AdminEmailHandler',
#            'include_html': True,
#            #'filters': ['special'],
#        },
#        'default': {
#            'level':'DEBUG',
#            'class':'logging.handlers.RotatingFileHandler',
#            'filename': os.path.join(LOG_DIR, 'all.log'),
#            'maxBytes': 1024*1024*5, # 5 MB
#            'backupCount': 5,
#            'formatter':'standard',
#            },
#        'request_handler': {
#            'level':'DEBUG',
#            'class':'logging.handlers.RotatingFileHandler',
#            'filename': os.path.join(LOG_DIR, 'request.log'),
#            'maxBytes': 1024*1024*5, # 5 MB
#            'backupCount': 5,
#            'formatter':'standard',
#            },
#        'script_handler': {
#            'level':'DEBUG',
#            'class':'logging.handlers.RotatingFileHandler',
#            'filename': os.path.join(LOG_DIR, 'script.log'),
#            'maxBytes': 1024*1024*5, # 5 MB
#            'backupCount': 5,
#            'formatter':'standard',
#            },
#        },
#    'loggers': {
#        'django': {
#            'handlers': ['default'],
#            'level': 'INFO',
#            'propagate': True
#        },
#        'django.request': {
#            'handlers': ['request_handler'],
#            'level': 'DEBUG',
#            'propagate': False
#        },
#        'script': { # 脚本专用日志
#                    'handlers': ['script_handler'],
#                    'level': 'INFO',
#                    'propagate': False
#        },
#        }
#}
