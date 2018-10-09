<template lang="pug">
span.uk-inline
  button.uk-button.uk-button-default(type=button) Status: {{ status }}
  div(uk-dropdown="mode: click")
    ul.uk-nav.uk-dropdown-nav
      li(v-for="status in statuses" :key="status")
        span(v-on:click="setStatus(status)") {{ status }}
</template>

<script>
export default {
  name: 'StatusSelect',

  data() {
    return {
      'status': null,
      'statuses': [],
    }
  },

  methods: {
    setStatus(status) {
      this.status = status
    }
  },

  created() {
    fetch('/api/v1/statuses')
      .then((rsp) => rsp.json())
      .then((rsp) => rsp.statuses)
      .then((statuses) => { this.statuses = statuses })
  },
}
</script>

<style lang="scss" scoped>
.uk-dropdown-nav {
  cursor: default;
  span {
    text-transform: uppercase;
  }
}
</style>

