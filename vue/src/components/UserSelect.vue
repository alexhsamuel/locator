<template lang="pug">
span.uk-inline
  button.uk-button.uk-button-default(type=button) User: {{ userId }}
  div(uk-dropdown="mode: click")
    ul.uk-nav.uk-dropdown-nav
      li(v-for="user in users" :key="user.user_id")
        span(v-on:click="setUser(user.user_id)") {{ user.user_id }}
</template>

<script>
export default {
  name: 'UserSelect',

  data() {
    return {
      'users': [],
      'userId': null,
    }
  },

  methods: {
    setUser(userId) {
      this.userId = userId
    }
  },

  created() {
    fetch('/api/v1/users')
      .then((rsp) => rsp.json())
      .then((rsp) => rsp.users)
      .then((users) => { this.users = users })
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

