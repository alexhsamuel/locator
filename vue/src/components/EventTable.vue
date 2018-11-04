<template lang="pug">
table.event-table
  thead
    tr
      th.user User
      th.status Status
      th.start-date Start Date
      th.end-date End Date
      th.notes Notes


</template>

<script>
export default {
  data() {
    return {
      events: [],
    }
  },

  created() {
    fetch('/api/v1/events')
      .then((rsp) => rsp.json())
      .then((rsp) => { this.events = rsp.events })
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
    font-weight: 700;
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

