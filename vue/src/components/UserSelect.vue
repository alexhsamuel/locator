<template lang="pug">
span
  vk-button User: {{ userId }}
  vk-dropdown
    vk-nav-dropdown(v-for="user in users" :key="user.user_id")
      span(v-on:click="setUser(user.user_id)") {{ user.user_id }}
</template>

<script>
import { Button } from 'vuikit/lib/button'
import { Dropdown } from 'vuikit/lib/dropdown'
import { NavDropdown } from 'vuikit/lib/nav'

export default {
  name: 'UserSelect',
  components: {
    VkButton: Button,
    VkDropdown: Dropdown,
    VkNavDropdown: NavDropdown,
  },

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

