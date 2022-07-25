"""
WSGI config for pensatm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
#
# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pensatm.settings')
#
# application = get_wsgi_application()

import os, sys

from django.core.wsgi import get_wsgi_application

site_user_root_dir = '/home/a/alexad0p/test/public_html'
sys.path.insert(0, os.path.join(site_user_root_dir, 'garant'))
sys.path.insert(1, '//home/a/alexad0p/test/public_html/venv/lib/python3.6/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pensatm.settings')

application = get_wsgi_application()