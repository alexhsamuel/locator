<template lang="pug">
tr
  td.user
    UserSelect(v-model="userId")
  td.status
    StatusSelect(v-model="status")
  td.start
    DateSelect(v-model="startDate")
  td.end
    DateSelect(v-model="endDate")
  td.notes
    input.uk-input(v-model="notes")
    button(v-on:click="onOk()") Add
    button(v-on:click="$emit('cxl')") Cancel

</template>

<script>
import DateSelect from '@/components/DateSelect.vue'
import StatusSelect from '@/components/StatusSelect.vue'
import UserSelect from '@/components/UserSelect.vue'

export default {
  components: {
    DateSelect,
    StatusSelect,
    UserSelect,
  },

  data() {
    return {
      userId: '',
      status: '',
      startDate: '',
      endDate: '',
      notes: '',
    }
  },

  methods: {
    onOk() {
      this.$emit('ok', {
        user_id: this.userId,
        status: this.status,
        dates: {
          start: this.startDate,
          end: this.endDate,
        },
        notes: this.notes,
      })
    }
  },
}
</script>

<style lang="scss">
button {
  background: #fafaff;
  color: #444;
  font-size: 90%;
  border: 1px solid #ccc;
  text-transform: uppercase;
  padding: 4px 12px;
  width: 12em;
  height: 3em;
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
