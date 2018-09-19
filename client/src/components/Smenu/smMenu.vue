<template>
  <div>
    <div class="box">
      <div class="tabs is-small is-fullwidth">
        <ul>
          <li
            v-for="opt in menuOptions"
            v-bind:key="opt.id"
            v-bind:opt="opt"
            v-bind:class="{ 'is-active': active == opt.name }"
            v-on:click="active = opt.name"
          >
            <a>
              {{ opt.name }}
            </a>
          </li>
        </ul>
      </div>
      <smData
      v-if="active == 'Data'"
      v-bind:appData="appData"
      />
      <smPlot
      v-else-if="active == 'Plot'"
      />
    </div>
  </div>
</template>

<script>
import smData from './smData';
import smPlot from './smPlot';

export default {
  name: 'smMenu',
  components: {
    smData,
    smPlot,
  },
  props: ['appData'],
  data() {
    return {
      msg: 'AVNGR',
      menuOptions: [
        { name: 'Data', id: 0 },
        { name: 'Filter', id: 1 },
        { name: 'Plot', id: 2 },
        { name: 'Format', id: 3 },
      ],
      active: 'Data',
    };
  },
};
</script>
