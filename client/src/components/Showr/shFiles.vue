<template>
  <div class="box">
    <p class="subtitle">
      {{ activeFile }}
    </p>
    <div
    class="notification"
    v-for="item in entries"
    v-bind:key="item.id"
    v-bind:item="item"
    v-bind:class="{'is-primary': item.load }"
    v-on:click="item.load = false"
    >
      <div class="columns">
        <div class="column">
          <p class="subtitle is-5">{{ item.name }}</p>
        </div>
        <div class="column">
          {{ item.data }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'shFiles',
  props: ['database', 'activeFile'],
  data() {
    return {
      loaded: [],
    };
  },
  computed: {
    entries() {
      const entries = [];
      this.genLoaded();
      for (let i = 0; i < this.database.length; i += 1) {
        entries.push({
          name: this.database[i].name,
          id: i,
          data: this.database[i].data,
          load: true,
        });
      }
      return entries;
    },
  },
  methods: {
    genLoaded() {
      this.loaded = [];
      for (let i = 0; i < this.database.length; i += 1) {
        this.entries.push(true);
      }
    },
    toggleLoad(loaded) {
      if (loaded) {
        return false;
      }
      return true;
    },
  },
};
</script>
