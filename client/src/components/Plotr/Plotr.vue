<template>
  <section class="section">
    <div class="container">
      <div class="columns">
        <div class="column is-3">
          <nav class="panel">
            <p class="panel-heading">
              Plotting Options
            </p>
            <div class="panel-block">
              <p class="control has-icons-left">
                <input class="input is-small" type="text" placeholder="search">
                <span class="icon is-small is-left">
                  <i class="fas fa-search" aria-hidden="true"></i>
                </span>
              </p>
            </div>
            <p class="panel-tabs">
              <a class="is-active">source</a>
              <a>plot</a>
              <a>filters</a>
              <a>formatting</a>
            </p>
            <a class="panel-block is-active">
              <span class="panel-icon">
                <i class="fas fa-book" aria-hidden="true"></i>
              </span>
              <div class="select">
                <select>
                  <option>x axis</option>
                  <option>time</option>
                </select>
              </div>
            </a>
            <div class="panel-block">
              <div class="columns">
                <div class="column is-9">
                  <p class="control has-icons-left">
                    <input class="input is-small" type="text" placeholder="text size">
                    <span class="icon is-small is-left">
                      <i class="fas fa-search" aria-hidden="true"></i>
                    </span>
                  </p>
                </div>
                <div class="column has-text-centered">
                  <p>
                    8
                  </p>
                </div>
              </div>
            </div>
            <a class="panel-block">
              <span class="panel-icon">
                <i class="fas fa-book" aria-hidden="true"></i>
              </span>
              marksheet
            </a>
            <a class="panel-block">
              <span class="panel-icon">
                <i class="fas fa-book" aria-hidden="true"></i>
              </span>
              minireset.css
            </a>
            <a class="panel-block">
              <span class="panel-icon">
                <i class="fas fa-book" aria-hidden="true"></i>
              </span>
              jgthms.github.io
            </a>
            <a class="panel-block">
              <span class="panel-icon">
                <i class="fas fa-code-branch" aria-hidden="true"></i>
              </span>
              daniellowtw/infboard
            </a>
            <a class="panel-block">
              <span class="panel-icon">
                <i class="fas fa-code-branch" aria-hidden="true"></i>
              </span>
              mojs
            </a>
            <label class="panel-block">
              <input type="checkbox">
              remember me
            </label>
            <div class="panel-block">
              <button class="button is-link is-outlined is-fullwidth">
                reset all filters
              </button>
            </div>
          </nav>
        </div>
        <div class="column">
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
      </div>
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
