import sys
import os
sys.path.insert(0, r'C:\inetpub\wwwroot\test-3\educationpro>')

os.environ['DJANGO_SETTINGS_MODULE'] = 'educationpro.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
