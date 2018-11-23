<template lang="pug">
span.uk-inline
  Datepicker.date(v-model="date" v-on:input="$emit('input', date)" format="yyyy-MM-dd")
</template>

<script>
import Datepicker from 'vuejs-datepicker'

export default {
  name: 'DateSelect',
  props: ['value'],
  components: {
    Datepicker,
  },

  data() {
    return {
      date: this.value,
    }
  },
}
</script>

<style lang="scss">
.date input {
  font-size: 100%;
  width: 8em;
}
</style>
