<template>
  <section class="section">
    <div class="container is-fluid">
      <div class="columns">
        <div class="column is-3">
          <p class="title">Plotr</p>
          <smMenu
          v-bind:appData="appData"
          />
        </div>
        <div class="column">
          <shPlot />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import smMenu from '../Smenu/smMenu';
import shPlot from '../Showr/shPlot';

export default {
  name: 'Showr',
  components: {
    smMenu,
    shPlot,
  },
  props: ['appData'],
  data() {
    return {
      msg: 'AVNGR',
      option: {},
    };
  },

};
</script>
