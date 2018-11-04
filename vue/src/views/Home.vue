<template lang="pug">
.home
  div
    EventTable
  div
    label.uk-form-label User:
    UserSelect.uk-form-width-small
    label.uk-form-label Status:
    StatusSelect.uk-form-width-small
    label.uk-form-label Start:
    DateSelect.uk-form-width-small
    label.uk-form-label End:
    DateSelect.uk-form-width-small
    label.uk-form-label Notes:
    input.uk-input.uk-form-width-medium
</template>

<script>
import DateSelect from '@/components/DateSelect.vue'
import EventTable from '@/components/EventTable.vue'
import StatusSelect from '@/components/StatusSelect.vue'
import UserSelect from '@/components/UserSelect.vue'

export default {
  name: 'home',
  components: {
    DateSelect,
    EventTable,
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
