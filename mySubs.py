import os
import os.path
import sys

try:                    ## Python 2
    from xmlrpclib import ServerProxy, Transport
    from settings import Settings
except ImportError:     ## Python 3
    from xmlrpc.client import ServerProxy, Transport
    from .settings import Settings

class OpenSubtitles(object): 
    
    def login(self, username, password):
        self.data = self.xmlrpc.LogIn(username, password, self.language, self.user_agent)
        token = self._get_from_data_or_none('token')
        if token:
            self.token = token
        return token

    def logout(self):
        '''Returns True is logout is ok, otherwise None.
        '''
        data = self.xmlrpc.LogOut(self.token)
        return '200' in data.get('status')

    def search_subtitles(self, params):
        '''Returns a list with the subtitles info.
        '''
        self.data = self.xmlrpc.SearchSubtitles(self.token, params)
        return self._get_from_data_or_none('data')
