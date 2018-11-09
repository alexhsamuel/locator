<template lang="pug">
div
  table.event-table
    thead
      tr
        th.user: .field User
        th.status: .field Status
        th.start-date: .field Start Date
        th.end-date: .field End Date
        th.notes: .field Notes

    tbody
      tr(v-for="event in events")
        td.user: .field {{ event.user_id }}
        td.status: .field {{ event.status }}
        td.start-date: .field {{ event.dates.start }}
        td.end-date: .field {{ event.dates.end }}
        td.notes: .field {{ event.notes }}

      EventRowEdit(
        v-if="adding"
        v-on:cxl="adding = false"
        v-on:ok="addEvent($event)"
        )

  button(v-if="!adding" v-on:click="adding = true") Add

</template>

<script>
import { sortBy } from 'lodash'

import EventRowEdit from '@/components/EventRowEdit.vue'
import { postEvent, searchEvents } from '@/api.js'

export default {
  components: {
    EventRowEdit,
  },

  data() {
    return {
      events_: [],
      adding: false,
    }
  },

  computed: {
    events() {
      return sortBy(this.events_, e => e.dates.start)
    },
  },

  methods: {
    addEvent(event) {
      this.adding = false
      postEvent(event).then(event => {
        this.events_.push(event)
      })
    }
  },

  created() {
    searchEvents().then(events => { 
      this.events_ = events 
    })
  },
}
</script>


<style lang="scss">
.event-table {
  width: 100%;
  border-collapse: collapse;
  tr {
  }
  .field {
    padding: 2px 8px;
  }
  th {
    text-align: left;
    text-transform: uppercase;
    font-weight: 700;
    font-size: 90%;
  }

  .user {
    width: 8em;
  }
  .status {
    width: 8em;
  }
  .start-date {
    width: 8em;
  }
  .end-date {
    width: 8em;
  }
  .notes {

  }
}
</style>

