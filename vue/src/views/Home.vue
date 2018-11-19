<template lang="pug">
.today
  h1 Today
  EventsToday

</template>

<script>
import EventsToday from '@/components/EventsToday.vue'

export default {
  name: 'home',
  components: {
    EventsToday,
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
