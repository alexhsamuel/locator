<template lang="pug">
div
  h1 Upcoming Coordinates
  EventTable(
    :start='$store.state.date')
</template>

<script>
import EventTable from '@/components/EventTable.vue'

export default {
  name: 'Upcoming',
  components: {
    EventTable,
  },

  computed: {
  },
}
</script>

<style lang="scss" scoped>

</style>
