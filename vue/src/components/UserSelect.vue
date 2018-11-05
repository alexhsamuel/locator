<template lang="pug">
span.uk-inline
  button.uk-button.uk-button-default(type=button) {{ userId || '&nbsp;' }}
  div(uk-dropdown="mode: click")
    ul.uk-nav.uk-dropdown-nav
      li(v-for="user in users" :key="user.user_id")
        span(v-on:click="setUser(user.user_id)") {{ user.user_id }}
</template>

<script>
export default {
  name: 'UserSelect',
  props: ['value'],

  data() {
    return {
      userId: this.value,
    }
  },

  computed: {
    users() {
      return this.$store.state.users
    },
  },

  methods: {
    setUser(userId) {
      this.userId = userId
      this.$emit('input', userId)
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

