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
            v-if="opt.persona == persona || opt.persona == 'ALL'"
          >
            <a>
              {{ opt.name }}
            </a>
          </li>
        </ul>
      </div>
      <smFiles
      v-if="active == 'Files'"
      v-bind:appData="appData"
      v-on:s-menu="$emit('s-menu', $event)"
      />
      <smPlot
      v-else-if="active == 'Plot'"
      />
      <smFormat
      v-else-if="active == 'Format'"
      />
    </div>
  </div>
</template>

<script>
import smFiles from './smFiles';
import smPlot from './smPlot';
import smFormat from './smFormat';

export default {
  name: 'smMenu',
  components: {
    smFiles,
    smPlot,
    smFormat,
  },
  props: ['appData', 'persona'],
  data() {
    return {
      msg: 'AVNGR',
      menuOptions: [
        { name: 'Files', persona: 'Loadr', id: 0 },
        { name: 'Filter', persona: 'Analyzr', id: 1 },
        { name: 'Plot', persona: 'Plotr', id: 2 },
        { name: 'Format', persona: 'Plotr', id: 3 },
      ],
      active: 'Files',
    };
  },
};
</script>
