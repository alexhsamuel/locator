<template lang="pug">
.today
  h1 Today's Coordinates
  EventTable(
    :start='this.$store.state.date'
    :end='this.$store.state.date'
  )
</template>

<script>
import EventTable from '@/components/EventTable.vue'

export default {
  name: 'today',
  components: {
    EventTable,
  }
}
</script>

<style lang="scss" scoped>
</style>
