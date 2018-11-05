<template lang="pug">
span.uk-inline
  button.uk-button.uk-button-default(type=button) {{ status || '&nbsp;' }}
  div(uk-dropdown="mode: click")
    ul.uk-nav.uk-dropdown-nav
      li(v-for="status in statuses" :key="status")
        span(v-on:click="setStatus(status)") {{ status }}
</template>

<script>
export default {
  name: 'StatusSelect',
  props: ['value'],

  data() {
    return {
      status: this.value,
    }
  },

  computed: {
    statuses() {
      return this.$store.state.statuses
    },
  },

  methods: {
    setStatus(status) {
      this.status = status
      this.$emit('input', status)
    }
  },

}
</script>

<style lang="scss" scoped>
span {
  display: inline-block;
}

button {
  width: 100%;
  text-transform: none;
}

.uk-dropdown-nav {
  cursor: default;
  span {
  }
}

</style>

