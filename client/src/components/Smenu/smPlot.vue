<template>
  <div>
    <div class="select">
      <select>
        <option>Scatter</option>
        <option>Line</option>
        <option>Bar</option>
      </select>
    </div>
    <br>
    <nav class="level is-mobile">
      <div class="level-item">
        <a class="button is-primary">
          <span class="icon">
            <font-awesome-icon icon="plus" />
          </span>
          <span> Series</span>
        </a>
      </div>
      <div class="level-item">
        <a class="button is-danger">
          <span class="icon">
            <font-awesome-icon icon="minus" />
          </span>
          <span> Series</span>
        </a>
      </div>
    </nav>

    <br>
    <div class="notification is-dark">
    </div>
  </div>
</template>

<script>
export default {
  name: 'smPlot',
  data() {
    return {
      msg: 'AVNGR',
    };
  },
};
</script>
