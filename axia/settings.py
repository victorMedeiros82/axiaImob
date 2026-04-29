from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-(#nr0(6kvpoa$z10izxi09@-+d!7k71$&-k8*vo^#=sbwo6fb*"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = [".onrender.com"]


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "core",
    "users",
    "leiloes",
    "imoveis",
    "custos",
    "financeiro",
    "documentos",
    "relatorios",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "axia.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "axia.wsgi.application"


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "axia_db",
#         "USER": "postgres",
#         "PASSWORD": "123456",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

DATABASES = {
    "default": dj_database_url.config(
        default=None,
        conn_max_age=600,
        ssl_require=not os.getenv("DEBUG", "True") == "True",
    )
}

# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "users.User"

# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

JAZZMIN_SETTINGS = {
    "site_title": "Axia Invest",
    "site_header": "Axia Negócios Imobiliários",
    "site_brand": "Axia",
    "welcome_sign": "Painel Estratégico de Investimentos",
    "theme": "darkly",
    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index"},
        {"app": "imoveis"},
        {"app": "financeiro"},
        {"app": "leiloes"},
    ],
    "icons": {
        "imoveis.Imovel": "fas fa-building",
        "leiloes.Leilao": "fas fa-gavel",
        "financeiro.Faturamento": "fas fa-dollar-sign",
        "custos.CustoAquisicao": "fas fa-file-invoice-dollar",
        "documentos.Documento": "fas fa-file-alt",
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "core.Corretor": "fas fa-user-tie",
        "core.Cliente": "fas fa-user-friends",
        "relatorios.Relatorio": "fas fa-chart-line",
    },
    "order_with_respect_to": [
        "leiloes",
        "imoveis",
        "custos",
        "financeiro",
        "documentos",
    ],
    "Sidebar": {"user_avatar": None},
}
