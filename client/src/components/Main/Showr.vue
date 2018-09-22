<template>
  <section class="section">
    <div class="container is-fluid">
      <p class="title">{{ persona }}</p>
      <div class="columns">
        <div class="column is-3">
          <smMenu
          v-bind:appData="appData"
          v-bind:persona="persona"
          v-on:s-menu="menuSelection"
          />
        </div>
        <div class="column">
          <shFiles
            v-if="persona == 'Loadr'"
            v-bind:database="database"
            v-bind:activeFile="activeFile"
          />
          <shTable
            v-if="persona == 'Loadr'"
          />
          <shPlot
            v-else-if="persona == 'Plotr'"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import smMenu from '../Smenu/smMenu';
import shFiles from '../Showr/shFiles';
import shPlot from '../Showr/shPlot';
import shTable from '../Showr/shTable';

export default {
  name: 'Showr',
  components: {
    smMenu,
    shFiles,
    shPlot,
    shTable,
  },
  props: ['appData', 'persona', 'database'],
  data() {
    return {
      msg: 'hello',
      activeFile: '',
    };
  },
  methods: {
    menuSelection(menuData) {
      if (menuData.type === 'fileSelection') {
        this.activeFile = menuData.data;
        this.$emit('ui', menuData);
      }
      // eslint-disable-next-line
      console.log(menuData);
    },
  },
};
</script>
