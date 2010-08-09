'''
Created on 05/08/2010

@author: romulo
'''

from django.conf import settings
from django.db import load_backend

def getConnection(banco):
    engine = settings.SECONDARY_DB[banco]['DATABASE_ENGINE']
    if engine == "sql_server.pyodbc":
        backend = __import__(engine+'.base', {}, {}, ['base'])
    else:
        backend = load_backend(engine)
    return backend.DatabaseWrapper(settings.SECONDARY_DB[banco])
