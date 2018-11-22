<template lang="pug">
#app
  #nav
    .date {{ $store.state.date }}
    div
      span.logo Coordinates
      router-link(to="/") Home
      router-link(to="/upcoming") Upcoming
      //- router-link(to="/about") About

  .uk-container.uk-container-expand
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

  .uk-container {
    margin-top: 40px;
  }
}
#nav {
  padding: 30px;
  background-color: #ddd;
  .logo {
    font-size: 160%;
    margin-right: 18px;
  }
  a {
    // font-weight: bold;
    color: #666;
    margin-left: 12px;
    margin-right: 12px;
    text-transform: uppercase;
    &.router-link-exact-active {
      text-decoration: underline;
    }
  }
  .date {
    float: right;
    padding-top: 8px;
  }
}

.uk-dropdown-nav {
  font-size: 100%;
  line-height: 1.75;
}

</style>
