<template lang="pug">
.form
  label User
  UserSelect(v-model="value.user_id")
  label Status
  StatusSelect(v-model="value.status")
  label Start Date
  DateSelect(v-model="value.dates.start")
  label End Date
  DateSelect(v-model="value.dates.end")
  label Notes
  input(v-model="value.notes")
</template>

<script>
import { emptyEvent } from '@/api'
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
}
</script>

<style lang="scss" scoped>
.form {
  display: grid;
  grid-template-columns: 80px auto;
  grid-template-rows: repeat(5, auto);
  border: 1px solid #ddd;
  padding: 8px 16px;
  margin: 12px 0;

}
</style>
