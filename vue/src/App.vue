<template lang="pug">
#app
  #nav
    router-link(to="/") Home
    |  | 
    router-link(to="/about") About
  .uk-container.uk-container-expand.uk-margin-top
    router-view
</template>

<style lang="scss">
@import "uikit/src/scss/variables-theme.scss";
@import "uikit/src/scss/mixins-theme.scss";

// 3. Your custom mixin overwrites.
@mixin hook-card() { color: #000; }

// 4. Import UIkit.
@import "uikit/src/scss/uikit-theme.scss";

html {
  font-family: Helvetica, monospace;
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
