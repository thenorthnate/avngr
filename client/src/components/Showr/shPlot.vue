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
  data() {
    return {
      myChart: echarts.init(document.getElementById('plot'), null, { renderer: 'svg' }),
      option: {},
    };
  },
  methods: {
    update() {
      // rebuilds the chart with the latest contents of "option"
      this.myChart.setOption(this.option);
    },
  },
};
</script>
