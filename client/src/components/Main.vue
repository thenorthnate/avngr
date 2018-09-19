<template>
  <div>
    <Navbar
    v-on:file="uploadFile"
    />
    <Showr
    v-bind:appData="appData"
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
      dmPath: 'http://localhost:5000/data-manager',
      fuPath: 'http://localhost:5000/file-upload',
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
      const payload = { type: 'file_list' };
      axios.post(this.dmPath, payload, this.headers.json)
        .then((res) => {
          const tmpData = res.data;
          for (let i = 0; i < res.data.length; i += 1) {
            tmpData[i].loaded = false;
          }
          this.appData = tmpData;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    postToDataManager(payload) {
      axios.post(this.dmPath, payload, this.headers.json)
        .then((res) => {
          this.appData = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
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
      axios.post(this.fuPath, payload, this.headers.file)
        .then((res) => {
          this.option = res.data;
          this.update();
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
