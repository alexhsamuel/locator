<template lang="pug">
span.uk-inline
  input.uk-input(v-model="date" v-on:input="$emit('input', date)")
</template>

<script>
export default {
  name: 'DateSelect',
  props: ['value'],

  data() {
    return {
      'date': this.value,
    }
  },

}
</script>
