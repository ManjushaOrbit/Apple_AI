"""
WSGI config for EligibilityCheck project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
# import sys

# # assuming your Django settings file is at '/home/myusername/mysite/mysite/settings.py'
# path = "D:/tool/EligibilityCheckForm/EligibilityCheck"
# if path not in sys.path:
#     sys.path.insert(0, path)

# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EligibilityCheck.settings')

application = get_wsgi_application()
