<template>
  <div>
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li><a href="#">Data</a></li>
        <li class="is-active"><a href="#" aria-current="page">Folder 1</a></li>
      </ul>
    </nav>
    <div class="filenotification">
      <a>
        <div
          class="notification"
          v-for="file in appData"
          v-bind:key="file.id"
          v-bind:file="file"
          v-on:click="activeFile = file.name"
          v-bind:class="{
            'is-light': !file.loaded,
            'is-primary': file.loaded,
            'is-link': activeFile == file.name,
          }"
          v-on:mouseover="activeFile = file.name"
        >
          <div class="columns is-vcentered">
            <div class="column">
              <p class="title has-text-primary">
                <span class="icon is-large">
                  <font-awesome-icon icon="file-excel" />
                </span>
              </p>
            </div>
            <div class="column">
              <p class="has-text-weight-light is-size-7 has-text-right">
                {{ file.name }}
              </p>
            </div>
          </div>
        </div>
      </a>
    </div>
    <br>
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
  name: 'smFiles',
  props: ['appData'],
  data() {
    return {
      activeFile: '',
    };
  },
};
</script>

<style scoped>
.filenotification {
  height: 400px;
  overflow-y: scroll;
  overflow-x: hidden;
  word-wrap: break-word;
}
</style>
