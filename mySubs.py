import os
import os.path
import sys

try:                    #Python 2
    from xmlrpclib import ServerProxy, Transport
    from settings import Settings
except ImportError:     #Python 3
    from xmlrpc.client import ServerProxy, Transport
    from .settings import Settings
