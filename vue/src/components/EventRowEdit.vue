<template lang="pug">
tr
  td.user
    UserSelect
  td.status
    StatusSelect
  td.start
    DateSelect
  td.end
    DateSelect
  td.notes
    input.uk-input
    button.uk-button.uk-button-default Add
    button.uk-button.uk-button-default Cancel
</template>

<script>
import DateSelect from '@/components/DateSelect.vue'
import StatusSelect from '@/components/StatusSelect.vue'
import UserSelect from '@/components/UserSelect.vue'

export default {
  components: {
    DateSelect,
    StatusSelect,
    UserSelect,
  }
}
</script>

<style lang="scss" scoped>
td.notes {
  display: flex;
  input {
    flex-grow: 1;
  }
  button {
    flex-grow: 0;
  }
}
</style>
