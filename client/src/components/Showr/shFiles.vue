<template>
  <div class="box">
    {{ activeFile }}
    <div
    class="notification"
    v-for="entry in database"
    v-bind:key="1"
    v-bind:entry="entry"
    >
      <button class="delete"></button>
      {{ entry }}
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
