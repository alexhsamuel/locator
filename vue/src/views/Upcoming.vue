<template lang="pug">
div
  h1 Upcoming Coordinates
  p today is {{ date }}
  EventTable(
    :start='this.$store.state.date')
</template>

<script>
import EventTable from '@/components/EventTable.vue'
import { formatDate } from '@/date'

export default {
  name: 'Upcoming',
  components: {
    EventTable,
  },

  computed: {
    date() { return formatDate(this.$store.state.date) }
  },
}
</script>

<style lang="scss" scoped>

</style>
