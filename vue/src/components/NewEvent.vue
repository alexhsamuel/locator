<template lang="pug">
.form
  label User
  UserSelect.user(v-model="value.user_id")
  label Status
  StatusSelect.status(v-model="value.status")
  label Start Date
  DateSelect(v-model="value.dates.start")
  label End Date
  DateSelect(v-model="value.dates.end")
  label Notes
  input(v-model="value.notes")
  .buttons
    button(v-on:click="addEvent()") Add
    button(v-on:click="$emit('cxl')") Cancel

</template>

<script>
import { emptyEvent, postEvent } from '@/api'
import DateSelect from '@/components/DateSelect.vue'
import StatusSelect from '@/components/StatusSelect.vue'
import UserSelect from '@/components/UserSelect.vue'

export default {
  props: [],
  components: {
    DateSelect,
    StatusSelect,
    UserSelect,
  },

  data() {
    console.log(emptyEvent())
    return {
      value: emptyEvent(),
    }
  },

  methods: {
    addEvent() {
      postEvent(this.value).then(event => {
        this.$store.commit('addEvent', event)
        this.$emit('ok', event)
        console.log('before', this.value.user_id)
        this.$set(this, 'value', emptyEvent())
        console.log('after', this.value.user_id)
      })

    },

  },
}
</script>

<style lang="scss" scoped>
.form {
  display: grid;
  grid-template-columns: 8em auto;
  grid-template-rows: repeat(5, auto);
  border: 1px solid #ddd;
  padding: 16px 24px;
  margin: 12px 0;

  > * {
    margin: 8px 0;
  }

  label {
    box-sizing: border-box;
    font-size: 100%;
    line-height: 2.25;
    height: 40px;
    padding: 4px 12px;
  }

  .status {
    width: 8em;
  }

  .buttons {
    grid-column-end: span 2;
    margin-top: 32px;
    > * {
      margin-right: 12px;
    }
  }
}
</style>
