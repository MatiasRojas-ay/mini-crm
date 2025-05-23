"""
Django settings for mini_crm project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from dotenv import load_dotenv

load_dotenv()

from pathlib import Path
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-clave-por-defecto-para-dev")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # terceros
     "unfold",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #apps
    "clientes",
    "proyectos",
    "presupuestos",
]

UNFOLD = {

    "SITE_TITLE": "Mini-CRM",
    "SITE_HEADER": "Mini-CRM",

    "DARK_MODE": True,

    "COLORS": {
        "base": {
            "50":  "250 250 250",  # #fafafa
            "100": "244 244 245",  # #f4f4f5
            "200": "228 228 231",  # #e4e4e7
            "300": "212 212 216",  # #d4d4d8
            "400": "161 161 170",  # #a1a1aa
            "500": "113 113 122",  # #71717a
            "600": "82 82 91",     # #52525b
            "700": "63 63 70",     # #3f3f46
            "800": "39 39 42",     # #27272a
            "900": "24 24 27",     # #18181b
            "950": "15 15 15",     # #0f0f0f
        },       # base como arriba
        "primary": {
            "50":  "240 249 255",  # #f0f9ff
            "100": "224 242 254",  # #e0f2fe
            "200": "186 230 253",  # #bae6fd
            "300": "125 211 252",  # #7dd3fc
            "400": "56 189 248",   # #38bdf8
            "500": "14 165 233",   # #0ea5e9
            "600": "2 132 199",    # #0284c7
            "700": "3 105 161",    # #0369a1
            "800": "7 89 133",     # #075985
            "900": "12 74 110",    # #0c4a6e
        },
        "secondary": {
            "50":  "240 253 244",  # #f0fdf4
            "100": "220 252 231",  # #dcfce7
            "200": "187 247 208",  # #bbf7d0
            "300": "134 239 172",  # #86efac
            "400": "74 222 128",   # #4ade80
            "500": "34 197 94",    # #22c55e
            "600": "22 163 74",    # #16a34a
            "700": "21 128 61",    # #15803d
            "800": "22 101 52",    # #166534
            "900": "20 83 45",     # #14532d
        },
        "font": {
            "subtle-light": "var(--color-base-500)",
            "subtle-dark": "var(--color-base-400)",
            "default-light": "var(--color-primary-700)",
            "default-dark": "var(--color-primary-200)",
            "important-light": "var(--color-primary-900)",
            "important-dark": "var(--color-primary-100)",
        },
    },

    "DASHBOARD_CALLBACK": "mini_crm.admin.dashboard_callback",

    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": _("Menú Principal"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                    },
                ],
            },
            {
                "title": _("Gestión"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Clientes"),
                        "icon": "group",
                        "link": reverse_lazy("admin:clientes_cliente_changelist"),
                    },
                    {
                        "title": _("Proyectos"),
                        "icon": "work",
                        "link": reverse_lazy("admin:proyectos_proyecto_changelist"),
                    },
                    {
                        "title": _("Tareas"),
                        "icon": "check_circle",
                        "link": reverse_lazy("admin:proyectos_tarea_changelist"),
                    },
                    {
                        "title": _("Responsables"),
                        "icon": "person",
                        "link": reverse_lazy("admin:proyectos_responsable_changelist"),
                    },
                ],
            },
            {
                "title": _("Finanzas"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Presupuestos"),
                        "icon": "attach_money",
                        "link": reverse_lazy("admin:presupuestos_presupuesto_changelist"),
                    },
                    {
                        "title": _("Pagos"),
                        "icon": "credit_score",
                        "link": reverse_lazy("admin:presupuestos_pago_changelist"),
                    },
                ],
            },
        ],
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mini_crm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "mini_crm/templates"],
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

WSGI_APPLICATION = 'mini_crm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Asuncion'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
