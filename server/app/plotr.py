# Plotr for AVNGR
# Builds the plot json data
# Nathan North


class Plotr:
    def __init__(self):
        self.option = {}
        self.series = []
        self.xAxis = {}
        self.yAxis = {}
        self.tooltip = {
            'trigger': 'axis',
            'axisPointer': {
                'type': 'cross'
            }
        }

        # scatter plots
        self.scType = 'scatter'
        self.scSymbolSize = 20

    def make_scatter(self, xyPairs):
        '''make_scatter expects xyPairs to be a list of lists [[x, y], [x, y]]'''
        self.series = [{
            'symbolSize': self.scSymbolSize,
            'data': xyPairs,
            'type': self.scType
        }]
        self.compile_plot()
        return self.option

    def compile_plot(self):
        self.option = {
            'xAxis': self.xAxis,
            'yAxis': self.yAxis,
            'series': self.series,
            'tooltip': self.tooltip
        }



option = {
    title: {
        text: 'Example Chart',
        left: 'center',
        textStyle: {
            fontSize: 20,
        },
    },
    toolbox: {
        show: true,
        feature: {
            saveAsImage: {
              show: true,
              title: 'Save',
              type: 'svg',
            },
            restore: {
              show: true,
              title: 'Restore',
            },
            dataZoom: {
              show: true,
              title: {
                zoom: 'Zoom',
                back: 'Undo',
              },
            },
        },
    },
    tooltip: {},
    legend: {
    data: ['Sales'],
    right: 'right',
    top: 'middle',
    },
    xAxis: {
    data: ['shirt', 'cardign', 'chiffon shirt', 'pants', 'heels', 'socks'],
    },
    yAxis: {},
    series: [{
    name: 'Sales',
    type: 'bar',
    data: [5, 20, 36, 10, 10, 20],
    }],
}
