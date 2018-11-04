<template lang="pug">
.event-table
  .head.user User
  .head.status Status
  .head.start-date Start Date
  .head.end-date End Date
  .head.notes Notes
</template>

<style lang="scss">
.event-table {
  display: grid;
  grid-template-columns: 8em 8em 8em 8em auto;

  div {
    border: 1px solid red;
    padding: 2px 8px;
  }

  .head {
    font-weight: 700;
  }

  .user {

  }
  .status {

  }
  .start-date {

  }
  .end-date {

  }
  .notes {

  }
}
</style>

