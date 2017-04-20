"""
WSGI config for cmpe239 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#import django.core.handlers.wsgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmpe239.settings")

application = get_wsgi_application()
#application = DjangoWhiteNoise(application)

