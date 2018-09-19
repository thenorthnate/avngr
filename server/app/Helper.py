# Helper for AVNGR
# Nathan North

import os
import pandas

from app.plotr import Plotr
from app.FileManager import FileManager


class Helper:
    def __init__(self):
        self.pwd = os.getcwd()
        self.dataDir = self.pwd + '/data/'
        self.fm = FileManager()

    def handle_request(self, requestObject, rType):
        if rType == 'json':
            if requestObject['type'] == 'file_list':
                return self.fm.get_file_list()
        elif rType == 'file':
            return self.fm.upload_file(requestObject)

    def load_data(self):
        data = pandas.read_csv(self.dataDir + 'test.csv')
        pltData = []
        for i in range(len(data['SCTG2'])):
            pltData.append([data['Total KTons in 2016'][i], data['Total Ton-Mile in 2016'][i]])
        return pltData

    def make_plot(self):
        plt = Plotr()
        option = plt.make_scatter(self.load_data())
        return option
