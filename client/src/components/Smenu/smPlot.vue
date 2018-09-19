<template>
  <div>
    <div class="dropdown is-hoverable">
      <div class="dropdown-trigger">
        <a disabled aria-haspopup="true" aria-controls="dropdown-menu4">
          <span>Plot Type</span>
          <span class="icon is-small">
            <i class="fas fa-angle-down" aria-hidden="true"></i>
          </span>
        </a>
      </div>
      <div class="dropdown-menu" id="dropdown-menu4" role="menu">
        <div class="dropdown-content">
          <div class="dropdown-item">
            <a>Scatter</a>
          </div>
        </div>
      </div>
    </div>

    <nav class="level">
      <div class="level-item has-text-centered">
        <div>
          Symbol Size
        </div>
      </div>
      <div class="level-item has-text-centered">
        <div>
          <a>
            <span class="icon">
              <font-awesome-icon icon="plus" />
            </span>
          </a>
          /
          <a>
            <span class="icon">
              <font-awesome-icon icon="minus" />
            </span>
          </a>
        </div>
      </div>
      <div class="level-item has-text-centered">
        <div class="dropdown is-hoverable">
          <div class="dropdown-trigger">
            <button class="button" aria-haspopup="true" aria-controls="dropdown-menu4">
              <span>20</span>
            </button>
          </div>
          <div class="dropdown-menu" id="dropdown-menu4" role="menu">
            <div class="dropdown-content">
              <div class="dropdown-item">
                <input class="input" type="number" value="20">
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>

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
