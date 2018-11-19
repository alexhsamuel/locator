<template lang="pug">
.today
  h1 Today
  EventsToday
  NewEvent
</template>

<script>
import EventsToday from '@/components/EventsToday.vue'
import NewEvent from '@/components/NewEvent.vue'

export default {
  name: 'home',
  components: {
    EventsToday,
    NewEvent,
  }
}
</script>

<style lang="scss" scoped>
.today {
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}
</style>
