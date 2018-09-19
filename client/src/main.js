// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import { library } from '@fortawesome/fontawesome-svg-core';
import {
  faCheck,
  faUpload,
  faDatabase,
  faPlus,
  faMinus,
  faArrowCircleUp,
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon, FontAwesomeLayers } from '@fortawesome/vue-fontawesome';
import 'bulma/css/bulma.css';
import Vue from 'vue';
import App from './App';
import router from './router';

library.add(faCheck);
library.add(faUpload);
library.add(faDatabase);
library.add(faPlus);
library.add(faMinus);
library.add(faArrowCircleUp);
Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.component('font-awesome-layers', FontAwesomeLayers);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
