<template>
  <div class="box">
    {{ activeFile }}
    <div
    class="notification"
    v-for="entry in newData"
    v-bind:key="entry.id"
    v-bind:entry="entry"
    >
      <button class="delete"></button>
      {{ entry.name }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'shFiles',
  props: ['database', 'activeFile'],
  data() {
    return {
      option: {},
    };
  },
  computed: {
    newData() {
      const newData = [];
      for (let i = 0; i < this.database.length; i += 1) {
        newData.push({ name: this.database[i], id: i });
      }
      return newData;
    },
  },
};
</script>
