# Helper for AVNGR
# Nathan North

import os
from app.FileManager import FileManager


class Helper:
    def __init__(self):
        self.pwd = os.getcwd()
        self.dataDir = self.pwd + '/data/'
        self.fm = FileManager()

    def handle_request(self, requestObject, rType):
        if rType == 'json':
            if requestObject['type'] == 'init':
                pass
            elif requestObject['type'] == 'file_list':
                return self.fm.get_file_list()
        elif rType == 'file':
            return self.fm.upload_file(requestObject)
