<template>
  <nav class="navbar is-transparent">
    <div class="navbar-brand">
      <a class="navbar-item" href="#">
        <img src="../../assets/Logo.png" alt="AVNGR" width="112" height="28">
      </a>
      <div class="navbar-burger burger" data-target="navbarExampleTransparentExample">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>

    <div id="navbarExampleTransparentExample" class="navbar-menu">
      <div class="navbar-start">
        <a
          class="navbar-item"
          v-bind:class="{'has-text-link': persona == 'Loadr'}"
          v-on:click="$emit('cp', 'Loadr')"
        >
          Loadr
        </a>
        <a
          class="navbar-item"
          v-bind:class="{'has-text-link': persona == 'Analyzr'}"
          v-on:click="$emit('cp', 'Analyzr')"
        >
          Analyzr
        </a>
        <a
          class="navbar-item"
          v-bind:class="{'has-text-link': persona == 'Plotr'}"
          v-on:click="$emit('cp', 'Plotr')"
        >
          Plotr
        </a>
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link" href="/documentation/overview/start/">
            Docs
          </a>
          <div class="navbar-dropdown is-boxed">
            <a class="navbar-item" href="/documentation/overview/start/">
              Overview
            </a>
            <a class="navbar-item" href="">
              Modifiers
            </a>
            <a class="navbar-item" href="">
              Columns
            </a>
            <a class="navbar-item" href="">
              Layout
            </a>
            <a class="navbar-item" href="">
              Form
            </a>
            <hr class="navbar-divider">
            <a class="navbar-item" href="">
              Elements
            </a>
            <a class="navbar-item is-active" href="">
              Components
            </a>
          </div>
        </div>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">

          <div class="file is-centered">
            <label class="file-label">
              <input
                class="file-input"
                type="file"
                name="file"
                multiple
                v-on:change="handleFile($event.target.name, $event.target.files)"
              />
              <span class="file-cta">
                <span class="file-icon has-text-info">
                  <font-awesome-icon icon="upload" />
                </span>
                <span class="file-label">
                  Upload File
                </span>
              </span>
            </label>
          </div>

        </div>
        <div class="navbar-item">
          <button class="button">
            <span class="icon">
              <font-awesome-icon icon="cog" />
            </span>
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  props: ['persona'],
  methods: {
    handleFile(fileName, fileList) {
      this.$emit('file', fileList);
    },
  },
};
</script>
