'''
Created on 05/08/2010
.
@author: Romulo de Barros Correia Jales <romulo@romulojales.com>
'''
from django.db.models import sql
from django.db.models.manager import Manager
from django.db.models.query import QuerySet
from query import get_query_class
from utils import getConnection

class MultiBdManager(Manager):

    use_for_related_fields = True
    
    def __init__(self, banco, *args, **kwargs):
        super(MultiBdManager, self).__init__(*args, **kwargs)
        self.banco = banco
    
    def get_query_set(self):
        print "obtendo um novo query set"
        #Obtem um novo query a partir das configuracoes de banco
        classe = get_query_class(self.banco)
        query = classe(self.model, self.banco)
        print 'model',self.model
        print 'query',type(query)
        
        qs = QuerySet(self.model, query)
        print "qs",qs
        return qs

    def _insert(self, values, return_id=False, raw_values=False):
        query = sql.InsertQuery(self.model, getConnection(self.banco))
        query.insert_values(values, raw_values)
        ret = query.execute_sql(return_id)
        #O commit automatico so eh valido para a conexao padrao do banco
        query.connection._commit()
        return ret

