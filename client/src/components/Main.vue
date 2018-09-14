<template>
  <div>
    <Navbar />
    <Plotr />
  </div>
</template>

<script>
import Plotr from './Plotr/Plotr';
import Navbar from './Main/Navbar';

export default {
  name: 'Main',
  components: {
    Navbar,
    Plotr,
  },
};
</script>
