# File Manager Class
# Nathan North
# Handles all things to do with file management

import os
import pandas


class FileManager:
    def __init__(self):
        self.pwd = os.getcwd()
        self.dataDir = self.pwd + "/data/"

    def get_file_list(self):
        '''Returns a list of all files in the working directory'''
        response = []
        i = 0
        for name in os.listdir(self.dataDir):
            response.append({'name': name, 'id': i})
            i += 1
        return response

    def upload_file(self, requestObject):
        '''Uploads files from the users computer to the working directory of the app'''
        # TODO: Add 1 to file name if it already exists!
        rFiles = requestObject.files
        for rf in rFiles:
            rFiles[rf].save(os.path.join(self.dataDir, rFiles[rf].filename))
        return "success"

    def read_file(self, filename):
        '''Reads a file into memory'''
        data = pandas.read_csv(self.dataDir + filename, skipinitialspace=True)
        for item in data:
            try:
                data[item] = pandas.to_numeric(data[item])
            except ValueError:
                try:
                    data[item] = pandas.to_datetime(data[item])
                except ValueError:
                    pass
        return data

    def write_file(self, filename):
        pass
