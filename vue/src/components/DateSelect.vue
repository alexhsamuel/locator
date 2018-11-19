<template lang="pug">
span.uk-inline
  Datepicker.date(:value="value" format="yyyy-MM-dd")
</template>

<script>
import Datepicker from 'vuejs-datepicker'

export default {
  name: 'DateSelect',
  props: ['value'],
  components: {
    Datepicker,
  },
}
</script>

<style lang="scss">
.date input {
  width: 7em;
}
</style>
