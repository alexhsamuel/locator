<template lang="pug">
span.uk-inline
  input(v-model="date" v-on:input="$emit('input', date)")
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

<style lang="scss" scoped>
input {
  width: 8em;
}
</style>
