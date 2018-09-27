# File Manager for AVNGR
# Nathan North
# Handles all things to do with file management

import os
import pandas
import json


class FileManager:
    def __init__(self, settings):
        self.settings = settings
        self.pwd = os.getcwd()
        self.dataDir = self.pwd + "/data/"
        self.settingsDir = self.pwd + "/settings/"

    def get_file_list(self):
        '''Returns a list of all files in the working directory'''
        response = []
        i = 0
        for name in os.listdir(self.dataDir):
            if self.check_support(name):
                response.append({'name': name, 'id': i})
                i += 1
        return response

    def check_support(self, fileName):
        for fileType in self.settings['FileManager']['SupportedFileTypes']:
            if fileName.endswith(fileType):
                return True
        return False

    def upload_file(self, requestObject):
        '''Uploads files from the users computer to the working directory of the app'''
        print(requestObject.form)
        rFiles = requestObject.files
        i = 0
        for rf in rFiles:
            fileName = self.make_no_conflict_filename(requestObject.form['names' + str(i)])
            rFiles[rf].save(os.path.join(self.dataDir, fileName))
            i += 1
        return "success"

    def check_filename(self, proposedName):
        '''Checks if file name is already in existance'''
        for name in os.listdir(self.dataDir):
            if name == proposedName:
                return False
        return True

    def make_no_conflict_filename(self, proposedName):
        '''Appends # to the filename to avoid naming conflicts'''
        if self.check_filename(proposedName):
            return proposedName

        nameComponents = proposedName.split('.')
        i = 0
        while True:
            tmpName = ''
            for j in range(len(nameComponents) - 1):
                tmpName += nameComponents[j]
            newName = tmpName + '_' + str(i) + '.' + nameComponents[-1]
            if self.check_filename(newName):
                return newName
            i += 1

    def handle_load_request(self, requestObject):
        fileRequest = {
            'fileName': requestObject['params']['name'],
            'filters': '',
            'nrows': self.settings['FileManager']['PreviewFileLineCount'],
            'sep': ',',
            'skipinitialspace': True,
            'usecols': ''
        }
        data = []
        if requestObject['params']['type'] == 'init':
            tmpData = self.read_file(fileRequest).to_dict(orient='list')
            print('made it')
            i = 0
            for item in tmpData:
                data.append({'name': item, 'data': tmpData[item]})
                i += 1
            data = json.dumps(data)

        return data

    def read_file(self, fileRequest):
        '''Reads a file into memory'''
        # fileRequest = {'filename': 'test.csv', 'filters': [{'on': 'date', 'flt': '>', 'value': '2018-6-5'}], 'nrows': 1000, 'sep': ',', 'skipinitialspace': True, 'usecols': ['a', 'b']}
        # fileRequest
        if len(fileRequest['filters']) > 0:
            pass
        else:
            data = pandas.read_csv(self.dataDir + fileRequest['fileName'],
                nrows=fileRequest['nrows'],
                sep=fileRequest['sep'],
                skipinitialspace=fileRequest['skipinitialspace']
            )
        return data

    def build_file_read_filter(self, filters):
        pass

    def write_file(self, filename):
        pass

    def save_for_later(self):
        '''
        Pandas functions that I don't want to forget about!

        # data = pandas.read_csv(fileName, sep='\t', skipinitialspace=True, nrows=1000, usecols=useCols, parse_dates={'START_TRIP_PARSED': ['START_TRIP']})
        # mask = (data['START_TRIP_PARSED'] >= '2018-6-5') & (data['START_TRIP_PARSED'] < '2018-6-6')
        iter_csv = pandas.read_csv(fileName, sep='\t', skipinitialspace=True, iterator=True, usecols=useCols, chunksize=1000, parse_dates={'START_TRIP_PARSED': ['START_TRIP']})
        data = pandas.concat([chunk.loc[(chunk['START_TRIP_PARSED'] >= '2018-6-5') & (chunk['START_TRIP_PARSED'] < '2018-6-6') & (chunk['TRIP_MILES'] > 0) & (chunk['ORIGIN_NAME'] == 'NEW CASTLE PA')] for chunk in iter_csv])
        # data = data.loc[mask]
        print(data)
        # data.index = data['START_TRIP_PARSED']
        # grouped = data.groupby([pandas.Grouper(freq='A'), pandas.Grouper(freq='M'), pandas.Grouper(freq='D')])
        # print(grouped.groups)
        data.to_csv('NEWCASTLEPA2018-6-5.csv')

        '''
        pass
