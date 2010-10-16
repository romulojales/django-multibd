'''
Created on 05/08/2010

@author: romulo
'''
from django.db.models import sql
from django.db.models.sql.where import WhereNode
from utils import getConnection


class MultiBdQueryBase(sql.BaseQuery):
    
    def __init__(self, model, banco):
        self.banco = banco
        self.model = model
        self.connection = getConnection(self.banco)
        super(MultiBdQueryBase, self).__init__( self.model, self.connection, WhereNode)

    def __setstate__(self, obj_dict):
        """Unpickling support."""
        # Rebuild list of field instances
        obj_dict['select_fields'] = [
            name is not None and obj_dict['model']._meta.get_field(name) or None
            for name in obj_dict['select_fields']
        ]

        self.__dict__.update(obj_dict)
        # XXX: Need a better solution for this when multi-db stuff is
        # supported. It's the only class-reference to the module-level
        # connection variable.
        self.connection = getConnection(self.banco)

        
def get_query_class(banco):
    from django.conf import settings
    #import sql_server.pyodbc.query
    #if settings.SECONDARY_DB[banco]["DATABASE_ENGINE"] == "sql_server.pyodbc":
    #    MultiBdQuery = sql_server.pyodbc.query.query_class(MultiBdQueryBase)
    #else:
    MultiBdQuery = MultiBdQueryBase
    return MultiBdQueryBase
        
