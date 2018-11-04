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

</style>
