'''
Created on 05/08/2010

@author: romulo
'''
from django.core.management.base import NoArgsCommand
from django.core.management import call_command
from django.conf import settings

class Command(NoArgsCommand):
    help = "Syncdb para as bases secundarias"

    def handle_noargs(self, **options):
        
        print "Sincronizando..."
        for name, database in settings.SECONDARY_DB.iteritems():
            print "Banco: ", name
            for key, value in database.iteritems():
                setattr(settings, key, value)
            call_command('syncdb')
