<template lang="pug">
.home
  label.uk-form-label User:
  UserSelect.uk-form-width-small
  label.uk-form-label Status:
  StatusSelect.uk-form-width-small
  label.uk-form-label Notes:
  input.uk-input.uk-form-width-medium
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
label {
  width: 8rem;
  text-transform: uppercase;
  margin: 0 4px 0 12px;
}

</style>
