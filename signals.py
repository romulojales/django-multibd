'''
Created on 09/08/2010

@author: romulo
'''
from django.dispatch.dispatcher import Signal

class_multibd_prepared = Signal(providing_args=["class"])
