<template>
  <section class="section">
    <div class="container">
      <a class="button is-primary" v-on:click="makePlot">Make Plot</a>
      <div id="plot" style="width:800px; height:600px;"></div>
    </div>
  </section>
</template>

<script>
import echarts from 'echarts';

export default {
  name: 'Plotr',
  data() {
    return {
      msg: 'AVNGR',
    };
  },
  methods: {
    makePlot() {
      // based on prepared DOM, initialize echarts instance
      const myChart = echarts.init(document.getElementById('plot'), null, { renderer: 'svg' });

      // specify chart configuration item and data
      const option = {
        title: {
          text: 'ECharts entry example',
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
      };

      // use configuration item and data specified to show chart
      myChart.setOption(option);
    },
  },
};
</script>
