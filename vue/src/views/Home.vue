<template lang="pug">
.today
  h1 Today
  EventsToday
  NewEvent(v-if="adding" v-on:ok="adding = false" v-on:cxl="adding = false")
  div(v-if="!adding")
    button(v-on:click="adding = true")
      span(uk-icon="plus") 
      | New Entry
</template>

<script>
import EventsToday from '@/components/EventsToday.vue'
import NewEvent from '@/components/NewEvent.vue'

export default {
  name: 'home',
  components: {
    EventsToday,
    NewEvent,
  },

  data() {
    return {
      adding: false,
    }
  },
}
</script>

<style lang="scss" scoped>
.today {
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

button > [uk-icon] {
  margin-right: 8px;
}
</style>
