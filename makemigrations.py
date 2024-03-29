""" to make migrations on this standalone app """
import sys
import django

from django.conf import settings
from django.core.management import call_command

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=(
        'django.contrib.contenttypes',
        'nhpgd_django',
    ),
)

django.setup()
call_command('makemigrations', 'nhpgd_django')