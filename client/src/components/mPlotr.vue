<template>
  <section class="section">
    <div class="container is-fluid">
      <p class="title">{{ persona }}</p>
      <div class="columns">
        <div class="column is-3">
          <div class="box">
            <div class="tabs is-small is-fullwidth">
              <ul>
                <li
                  v-bind:class="{ 'is-active': activeTab == 'Plot' }"
                  v-on:click="activeTab = 'Plot'"
                >
                  <a>
                    Plot
                  </a>
                </li>
                <li
                  v-bind:class="{ 'is-active': activeTab == 'Format' }"
                  v-on:click="activeTab = 'Format'"
                >
                  <a>
                    Format
                  </a>
                </li>
              </ul>
            </div>
            <!-- Here is the Plot Tab -->
            <div v-if="activeTab == 'Plot'">
              <br>
              <nav class="level is-mobile">
                <div class="level-item">
                  <div class="select">
                    <select v-model="plotType">
                      <option value="" disabled>Choose Plot Type</option>
                      <option>XY</option>
                      <option>Circle</option>
                    </select>
                  </div>
                </div>
                <div class="level-item">
                  <a
                  class="button is-primary"
                  v-bind:disabled="plotType == ''"
                  v-on:click="addSeries"
                  >
                    <span class="icon">
                      <font-awesome-icon icon="plus" />
                    </span>
                    <span> Series</span>
                  </a>
                </div>
              </nav>


              <div
              class="notification is-dark"
              v-for="item in series"
              v-bind:item="item"
              v-bind:key="item.id"
              >
              <button class="delete"></button>
              <p class="subtitle">Series {{ item.id }}</p>
              <div class="select">
                <select v-model="item.type">
                  <option value="" disabled>Choose Series Type</option>
                  <option>scatter</option>
                  <option>bar</option>
                  <option>line</option>
                </select>
              </div>
              {{ item.symbolSize }}
              </div>

            </div>
            <!-- Here is the Format Tab -->
            <div v-else-if="activeTab == 'Format'">
              <div class="columns is-vcentered">
                <div class="column">
                  <p class="subtitle">
                    Title
                  </p>
                </div>
                <div class="column has-text-right">
                  <a v-on:click="if(show.title){ show.title = false } else { show.title = true }">
                    <span class="icon is-large" v-if="show.title">
                      <font-awesome-icon icon="angle-down" />
                    </span>
                    <span class="icon is-large" v-else>
                      <font-awesome-icon icon="angle-right" />
                    </span>
                  </a>
                </div>
              </div>

              <div class="box" v-if="show.title">
                <input
                class="input"
                type="text"
                placeholder="Title..."
                v-model="option.title.text"
                v-on:input="update"
                />
                <br><br>
                <div class="columns is-vcentered">
                  <div class="column">
                    Font Size
                  </div>
                  <div class="column">
                    <input
                    class="input"
                    type="number"
                    placeholder="Title Font Size"
                    v-model="option.title.textStyle.fontSize"
                    v-on:input="update"
                    />
                  </div>
                </div>
              </div>

              <div class="columns is-vcentered">
                <div class="column">
                  <p class="subtitle">
                    Axes
                  </p>
                </div>
                <div class="column has-text-right">
                  <a v-on:click="if(show.axes){ show.axes = false } else { show.axes = true }">
                    <span class="icon is-large" v-if="show.axes">
                      <font-awesome-icon icon="angle-down" />
                    </span>
                    <span class="icon is-large" v-else>
                      <font-awesome-icon icon="angle-right" />
                    </span>
                  </a>
                </div>
              </div>

              <div class="box" v-if="show.axes">
                <input
                class="input"
                type="text"
                placeholder="X Axis..."
                />
                <br><br>
                <input
                class="input"
                type="text"
                placeholder="Y Axis..."
                />
                <br><br>
                <div class="columns is-vcentered">
                  <div class="column">
                    Axis Font Size
                  </div>
                  <div class="column">
                    <input
                    class="input"
                    type="number"
                    placeholder="Size..."
                    />
                  </div>
                </div>
              </div>

            </div>


          </div>


        </div>
        <div class="column">
          <a class="button is-primary" v-on:click="update">Update</a>
          <div id="plot" style="width:1100px; height:700px;"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import echarts from 'echarts';

export default {
  name: 'mPlotr',
  props: ['appData', 'persona', 'database'],
  data() {
    return {
      activeTab: 'Plot',
      show: {
        title: false,
        axes: false,
      },
      plotType: '',
      myChart: '',
      series: [],
      option: {
        title: {
          text: '',
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
        xAxis: {
          name: 'test',
          nameLocation: 'center',
          nameGap: 30,
          nameTextStyle: {
            fontSize: 20,
          },
        },
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
    addSeries() {
      // TODO: Set the id to the NEXT id... not just the length
      if (this.plotType === 'XY') {
        const tmpSeries = {
          symbolSize: 20,
          data: [[20, 1]],
          type: 'scatter',
          id: this.series.length,
        };
        this.series.push(tmpSeries);
      }
    },
    removeSeries() {
      // removes a series
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
