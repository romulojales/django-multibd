'''
Created on 05/08/2010

@author: romulo
'''
from django.db.models import sql
from django.db.models.sql.where import WhereNode
from utils import getConnection

class MultiBdQuery(sql.Query):
    def __init__(self, model, banco):
        self.banco = banco
        self.connection = getConnection(self.banco)
        super(MultiBdQuery, self).__init__(model, self.connection, WhereNode)
        
    def __setstate__(self, obj_dict):
        """
        Unpickling support.
        """
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