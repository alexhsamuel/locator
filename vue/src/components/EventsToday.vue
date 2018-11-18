<template lang="pug">
div
  div.event(v-for="event in events")
    div.dates {{ event.dates.start }} &ndash; {{ event.dates.end }}
    div.title {{ event.user_id }} {{ event.status }}
    div.notes {{ event.notes }}

</template>

<script>
import { filter, sortBy } from 'lodash'

import EventRowEdit from '@/components/EventRowEdit.vue'
import { postEvent } from '@/api'
import { inRange } from '@/date'

export default {
  props: [],
  components: {
    EventRowEdit,
  },

  data() {
    return {
      newEvent: null,
    }
  },

  computed: {
    events() {
      return sortBy(
        filter(
          this.$store.state.events, 
          e => inRange(this.$store.state.date, e.dates.start, e.dates.end)),
        e => e.dates.start)
    },
  },

  methods: {
    inRange,

    addEvent(event) {
      this.adding = false
      // FIXME: addEvent should be an action that posts the event.
      postEvent(event).then(event => {
        this.$store.commit('addEvent', event)
      })
    }
  },

}
</script>

<style lang="scss" scoped>
.event {
  border: 1px solid #ddd;
  padding: 8px 16px;
  margin: 12px 0;

  .title {
    font-size: 180%;
  }

  .dates {
    float: right;
    margin-top: 8px;
  }
}
</style>
