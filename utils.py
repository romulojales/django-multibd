'''
Created on 05/08/2010

@author: romulo
'''
from sqlServerMultiBd.pyodbc import base
from django.conf import settings
from django.db import load_backend

def getConnection(banco):
    engine = settings.SECONDARY_DB[banco]['DATABASE_ENGINE']
    if engine == "sql_server.pyodbc":
        return base.DatabaseWrapper(settings.SECONDARY_DB[banco])
    else:
        bckend = load_backend(engine)
        return bckend.DatabaseWrapper(settings.SECONDARY_DB[banco])
