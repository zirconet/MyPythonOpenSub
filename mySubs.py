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
        data = self.xmlrpc.LogOut(self.token)
        return '200' in data.get('status')

    def search_subtitles(self, params):
        self.data = self.xmlrpc.SearchSubtitles(self.token, params)
        return self._get_from_data_or_none('data')

        def __init__(self, path):
        self.path = path
        self.size = str(os.path.getsize(path))

    def get_hash(self):
        longlongformat = 'q'  # long long
        bytesize = struct.calcsize(longlongformat)

        try:
            f = open(self.path, "rb")
        except(IOError):
            return "IOError"

        hash = int(self.size)

        if int(self.size) < 65536 * 2:
            return "SizeError"

        for x in range(65536 // bytesize):
            buffer = f.read(bytesize)
            (l_value, ) = struct.unpack(longlongformat, buffer)
            hash += l_value
            hash = hash & 0xFFFFFFFFFFFFFFFF  # to remain as 64bit number

        f.seek(max(0, int(self.size) - 65536), 0)
        for x in range(65536 // bytesize):
            buffer = f.read(bytesize)
            (l_value, ) = struct.unpack(longlongformat, buffer)
            hash += l_value
            hash = hash & 0xFFFFFFFFFFFFFFFF

        f.close()
        returnedhash = "%016x" % hash
        return str(returnedhash)
