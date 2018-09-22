<template>
  <div>
    <div class="columns is-vcentered">
      <div class="column">
        <input class="input" type="text" placeholder="Search Files..." v-model="searchText">
      </div>
      <div class="column">
        <div class="file is-centered">
          <label class="file-label">
            <input
              class="file-input"
              type="file"
              name="file"
              multiple
              v-on:change="uploadFile($event.target.files)"
            />
            <span class="file-cta">
              <span class="file-icon">
                <font-awesome-icon icon="upload" />
              </span>
              <span class="file-label">
                Add File
              </span>
            </span>
          </label>
        </div>

      </div>
    </div>
    <p>{{ searchText }}</p>
    <br>
    <ul>
      <li
      v-for="file in appData.fileList"
      v-bind:key="file.id"
      v-bind:file="file"
      v-bind:class="{
        'has-text-light': !file.loaded,
        'has-text-primary': file.loaded,
        'has-text-link': activeFile == file.name,
      }"
      v-on:mouseover="activeFile = file.name"
      >
        <p>
          <span class="icon">
            <font-awesome-icon icon="file-excel" />
          </span>
          <span>
            <a
            v-on:click="$emit('s-menu', {type: 'fileSelection', data: file.name})"
            >
              {{ file.name }}
            </a>
          </span>
        </p>
      </li>
    </ul>
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
import axios from 'axios';

export default {
  name: 'smFiles',
  props: ['appData'],
  data() {
    return {
      activeFile: '',
      searchText: '',
    };
  },
  methods: {
    uploadFile(fileList) {
      if (fileList.length === 0) {
        return;
      }
      const payload = new FormData();
      for (let i = 0; i < fileList.length; i += 1) {
        payload.append(`datafiles${i}`, fileList[i]);
        if ('name' in fileList[i]) {
          payload.append(`names${i}`, fileList[i].name);
        } else {
          payload.append(`names${i}`, '');
        }
        if ('size' in fileList[i]) {
          payload.append(`sizes${i}`, fileList[i].size);
        } else {
          payload.append(`sizes${i}`, '');
        }
      }
      axios.post(`${this.appData.uri}${this.appData.settings.api.file.path}`, payload, this.appData.headers.file)
        .then((res) => {
          // eslint-disable-next-line
          console.log(res.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>
