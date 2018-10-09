<template lang="pug">
.home
  UserSelect
  | Status:
  StatusSelect
  | Notes:
  input.uk-input#notes
</template>

<script>
// @ is an alias to /src
import StatusSelect from '@/components/StatusSelect.vue'
import UserSelect from '@/components/UserSelect.vue'

export default {
  name: 'home',
  components: {
    StatusSelect,
    UserSelect,
  }
}
</script>

<style lang="scss" scoped>
#status {
  width: 12rem;
}
#notes {
  width: 20rem;
}
</style>
