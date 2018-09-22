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
        # fileRequest = {'filename': 'test.csv', 'filters': [{'on': 'date', 'flt': '>', 'value': '2018-6-5'}], 'nrows': 1000, 'sep': ',', 'skipinitialspace': True}
        data = pandas.read_csv(self.dataDir + filename, skipinitialspace=True)
        return data

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
