<template>
  <div>
    <a class="button is-primary" v-on:click="update">Update</a>
    <div id="plot" style="width:1100px; height:700px;"></div>
  </div>
</template>

<script>
import echarts from 'echarts';

export default {
  name: 'shPlot',
  props: ['userInputOptions'],
  data() {
    return {
      myChart: '',
      option: {
        title: {
          text: 'Test Chart',
          left: 'center',
          textStyle: {
            fontSize: 20,
          },
        },
        toolbox: {
          show: true,
          right: 10,
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
        tooltip: {
          trigger: 'item',
        },
        xAxis: {},
        yAxis: {},
        series: [{
          symbolSize: 20,
          data: [[0, 0], [1, 1], [2, 2]],
          type: 'scatter',
        }],

      },
    };
  },
  methods: {
    initialize() {
      this.myChart = echarts.init(document.getElementById('plot'), null, { renderer: 'svg' });
      this.myChart.setOption(this.option);
    },
    changeOption(option, value) {
      // changes any options set in UI
      // eslint-disable-next-line
      console.log(option, value);
    },
    update() {
      // rebuilds the chart with the latest contents of "option"
      this.myChart.setOption(this.option);
    },
  },
  mounted() {
    this.initialize();
  },
};
</script>
