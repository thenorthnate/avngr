<template>
  <div>
    <Navbar
      v-on:cp="changePersona"
      v-bind:persona="persona"
    />
    <Showr
    v-bind:appData="appData"
    v-bind:persona="persona"
    v-bind:database="database"
    v-on:ui="inputRequest"
    />
  </div>
</template>

<script>
import axios from 'axios';
import Showr from './Main/Showr';
import Navbar from './Main/Navbar';

export default {
  name: 'Main',
  components: {
    Navbar,
    Showr,
  },
  data() {
    return {
      uri: 'http://localhost:5000',
      paths: {
        dmPath: 'http://localhost:5000/data-manager',
        fuPath: 'http://localhost:5000/file-upload',
      },
      dmPath: 'http://localhost:5000/data-manager',
      fuPath: 'http://localhost:5000/file-upload',
      persona: 'Loadr',
      headers: {
        json: { headers: { 'Content-Type': 'application/json' } },
        file: { headers: { 'Content-Type': 'multipart/form-data' } },
      },
      database: '',
      appData: '',
    };
  },
  methods: {
    initializeApp() {
      axios.get(`${this.uri}/api/init`)
        .then((res) => {
          const tmpData = res.data;
          for (let i = 0; i < res.data.length; i += 1) {
            tmpData.fileList[i].loaded = false;
          }
          tmpData.uri = this.uri;
          tmpData.paths = this.paths;
          tmpData.headers = this.headers;
          this.appData = tmpData;
          // eslint-disable-next-line
          console.log(this.appData);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    changePersona(newPersona) {
      this.persona = newPersona;
    },
    inputRequest(userInput) {
      if (userInput.type === 'fileSelection') {
        // eslint-disable-next-line
        console.log('this is the input: ', userInput.data);
        // database = [{'name': 'filename.csv', 'data': [[], [], []]}]
        const payload = { type: 'load', params: { type: 'init', name: userInput.data } };
        this.getFileData(payload);
      }
    },
    getFileData(payload) {
      axios.post(`${this.uri}${this.appData.settings.api.data.path}`, payload, this.appData.settings.api.data.headers)
        .then((res) => {
          this.database = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.initializeApp();
  },
};
</script>
