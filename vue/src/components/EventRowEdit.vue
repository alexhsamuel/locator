<template lang="pug">
tr
  td.user
    UserSelect(v-model="value.user_id")
  td.status
    StatusSelect(v-model="value.status")
  td.start
    DateSelect(v-model="value.dates.start")
  td.end
    DateSelect(v-model="value.dates.end")
  td.notes
    input(v-model="value.notes")
    button(v-on:click="$emit('ok', value)") Add
    button(v-on:click="$emit('cxl')") Cancel

</template>

<script>
import DateSelect from '@/components/DateSelect.vue'
import StatusSelect from '@/components/StatusSelect.vue'
import UserSelect from '@/components/UserSelect.vue'

export default {
  props: ['value'],
  components: {
    DateSelect,
    StatusSelect,
    UserSelect,
  },

  data() {
    return {
    }
  },
}
</script>

<style lang="scss">
button {
  background: #fafaff;
  color: #444;
  font-size: 90%;
  text-transform: uppercase;
  width: 12em;
  line-height: 40px;
  border: 1px solid #ccc;
  padding: 4px 12px;
}

input {
  background: #fafafa;
  color: black;
  font-size: 100%;
  box-sizing: border-box;
  height: 40px;
  border: 1px solid #ccc;
  padding: 4px 12px;
}
</style>

<style lang="scss" scoped>
td.notes {
  display: flex;
  align-items: center;

  > * { margin: 0 5px; }    
  > :first-child { margin-left: 0; }
  > :last-child { margin-right: 0; }

  input {
    flex-grow: 1;
  }
  button {
    flex-grow: 0;
  }
}
</style>
