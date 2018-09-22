# Helper for AVNGR
# Nathan North

import os
import json
from app.FileManager import FileManager


class Helper:
    def __init__(self):
        # Settings
        self.pwd = os.getcwd()
        self.settingsDir = self.pwd + '/settings/'
        self.settings = {}
        self.read_settings()
        # Data
        self.dataDir = self.pwd + '/data/'
        # Subclasses
        self.fm = FileManager(self.settings)

    def read_settings(self):
        with open(self.settingsDir + 'settings.json', 'r') as inputFile:
            self.settings = json.load(inputFile)

    def update_settings(self):
        self.read_settings()
        self.fm.settings = self.settings

    def handle_request(self, requestObject, rType):
        if rType == 'json':
            if requestObject['type'] == 'load':
                data = self.fm.handle_load_request(requestObject)
                print(data)
                return data
        elif rType == 'file':
            return self.fm.upload_file(requestObject)

    def init_request(self):
        '''Generates reply json for init request from UI'''
        # {'fileList': [...], 'settings': {...}}
        self.update_settings()
        initData = {'settings': self.settings}
        initData['fileList'] = self.fm.get_file_list()
        return initData
