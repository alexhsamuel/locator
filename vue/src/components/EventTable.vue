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
      tr(
          v-for="event in events" 
          :class='{ current: inRange($store.state.date, event.dates.start, event.dates.end) }'
      )
        td.user: .field {{ event.user_id }}
        td.status: .field {{ event.status }}
        td.start-date: .field {{ event.dates.start }}
        td.end-date: .field {{ event.dates.end }}
        td.notes: .field {{ event.notes }}

      EventRowEdit(
        v-if="adding"
        v-model="newEvent"
        v-on:cxl="adding = false"
        v-on:ok="addEvent($event)"
        )

  button(v-if="!adding" v-on:click="onAdd()") Add

</template>

<script>
import { filter, sortBy } from 'lodash'

import EventRowEdit from '@/components/EventRowEdit.vue'
import { postEvent, emptyEvent } from '@/api'
import { inRange, overlap } from '@/date'

export default {
  props: ['start', 'end'],
  components: {
    EventRowEdit,
  },

  data() {
    return {
      adding: false,
      newEvent: null,
    }
  },

  computed: {
    events() {
      return sortBy(
        filter(
          this.$store.state.events, 
          e => overlap(this.start, this.end, e.dates.start, e.dates.end)), 
        e => e.dates.start)
    },
  },

  methods: {
    inRange,

    onAdd() {
      this.newEvent = emptyEvent()
      this.adding = true
    },

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


<style lang="scss">
.event-table {
  width: 100%;
  border-collapse: collapse;
  thead {
    border-bottom: 1px solid #666;
  }
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
  tbody {
    color: #bbb;
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
  .current {
    color: #666;
  }
}
</style>

