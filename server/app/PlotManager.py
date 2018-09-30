# Extracts and shapes the data for specific plot types
# Builds the plot json data
# Nathan North


class PlotManager:
    def generate_plot_data(self, requestJson, data):
        if requestJson['info']['plotType'] == 'scatter':
            return self.make_scatter(requestJson, data)
        elif requestJson['info']['plotType'] == 'line':
            return self.make_line(requestJson, data)

    def make_scatter(self, requestJson, data):
        pass

    def make_line(self, requestJson, data):
        pass

    def make_bar(self, requestJson, data):
        pass

    def make_pie(self, requestJson, data):
        pass
