<template lang="pug">
table.event-table
  thead
    tr
      th.user User
      th.status Status
      th.start-date Start Date
      th.end-date End Date
      th.notes Notes

  tbody
    tr(v-for="event in events")
      td.user {{ event.user_id }}
      td.status {{ event.status }}
      td.start-date {{ event.dates.start }}
      td.end-date {{ event.dates.end }}
      td.notes {{ event.notes }}

</template>

<script>
import { sortBy } from 'lodash'

export default {
  data() {
    return {
      events_: [],
    }
  },

  computed: {
    events() {
      return sortBy(this.events_, e => e.dates.start)
    },
  },

  created() {
    fetch('/api/v1/events')
      .then((rsp) => rsp.json())
      .then((rsp) => { this.events_ = rsp.events })
  },
}
</script>


<style lang="scss">
.event-table {
  width: 100%;
  border-collapse: collapse;
  tr {
    border: 1px solid red;
  }
  th, td {
    padding: 2px 8px;
  }
  th {
    text-align: left;
    text-transform: uppercase;
    font-weight: 400;
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

