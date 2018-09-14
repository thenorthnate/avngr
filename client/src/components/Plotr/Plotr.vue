<template>
  <section class="section">
    <div class="container">
      <div class="dropdown is-hoverable">
        <div class="dropdown-trigger">
          <button class="button" aria-haspopup="true" aria-controls="dropdown-menu4">
            <span>Hover me</span>
            <span class="icon is-small">
              <i class="fas fa-angle-down" aria-hidden="true"></i>
            </span>
          </button>
        </div>
        <div class="dropdown-menu" id="dropdown-menu4" role="menu">
          <div class="dropdown-content">
            <div class="dropdown-item">
              <p>You can insert <strong>any type of content</strong> within the dropdown menu.</p>
            </div>
          </div>
        </div>
      </div>
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
      };

      // use configuration item and data specified to show chart
      myChart.setOption(option);
    },
  },
};
</script>
