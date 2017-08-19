"""
WSGI config for hasker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

RUN_ENV = os.environ.get('HASKER_RUN_ENV', 'dev')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.{}".format(RUN_ENV))

application = get_wsgi_application()
