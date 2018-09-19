<template>
  <div>
    <div class="table-container">
      <table class="table is-fullwidth">
        <thead>
          <tr>
            <th>
              File
            </th>
            <th>
              Size
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="file in appData"
            v-bind:key="file.id"
            v-bind:file="file"
          >
            <td>
              <button
                class="button is-small"
                v-on:click="activeFile = file.name"
              >
                <span
                  class="icon is-small is-left"
                  v-bind:class="{
                    'has-text-grey-lighter': !file.loaded,
                    'has-text-primary': file.loaded,
                  }"
                >
                  <font-awesome-icon icon="database" />
                </span>
                <span>File {{ file.id }}</span>
              </button>
            </td>
            <td>
              {{ file.name }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div
      v-if="activeFile"
      class="notification"
    >
      <p class="subtitle">{{ activeFile }}</p>
      Size: 20KB<br>
      Headers:<br>
      <span class="tag is-link">
        ID
      </span>
      <span class="tag is-light">
        2000r
      </span>
      <span class="tag is-info">
        10c
      </span>
      <div class="buttons is-right">
        <button class="button">
          <span>Load File </span>
          <span class="icon has-text-link">
            <font-awesome-icon icon="arrow-circle-up" />
          </span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'smData',
  props: ['appData'],
  data() {
    return {
      activeFile: '',
    };
  },
};
</script>
