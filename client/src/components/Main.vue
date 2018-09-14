<template>
  <div>
    <h1 class="title is-one has-text-centered">{{ msg }}</h1>
    <Plotr />
  </div>
</template>

<script>
import Plotr from './Plotr/Plotr';

export default {
  name: 'Main',
  components: {
    Plotr,
  },
  data() {
    return {
      msg: 'AVNGR',
    };
  },
};
</script>
