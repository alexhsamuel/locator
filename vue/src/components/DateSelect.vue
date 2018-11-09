<template lang="pug">
span.uk-inline
  Datepicker(format="yyyy-MM-dd")
  // input(v-model="date" v-on:input="$emit('input', date)")
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
      'date': this.value,
    }
  },

}
</script>

<style lang="scss" scoped>
input {
  width: 8em;
}
</style>
