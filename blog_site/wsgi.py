"""
WSGI config for blog_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
project_folder = os.path.expanduser('/Users/andre22/Documents/Dev/BEW-1.2/blog_site') 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_site.settings')

application = get_wsgi_application()
