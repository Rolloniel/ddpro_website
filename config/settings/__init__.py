import environ
from django.core.exceptions import ImproperlyConfigured


ROOT_DIR = (
    environ.Path(__file__) - 3
)  # (ddpro_website/config/settings/base.py - 3 = ddpro_website/)
APPS_DIR = ROOT_DIR.path("ddpro_website")

env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR.path(".env")))

SERVER_TYPE = env.str("ENV_TYPE")
if SERVER_TYPE == "local":
    from .local import *
elif SERVER_TYPE == "production":
    from .production import *
elif SERVER_TYPE == "test":
    from .test import *
else:
    raise ImproperlyConfigured("Set correct environment type. Possible options ENV_TYPE=local|production|test")
