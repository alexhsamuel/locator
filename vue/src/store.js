import Vue from 'vue'
import Vuex from 'vuex'

import { date, formatDate } from '@/date'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    statuses: [],
    users: [],
    date: null,
  },

  _updateDate() {
    this.setTime()
    // Update every second, on the second.
    window.setTimeout(() => this._tick(), 1000 - this.state.time % 1000) 
  },

  mutations: {
    setDate(state, date) {
      console.log('setDate', date)
      state.date = date
    },

    setStatuses(state, statuses) {
      state.statuses = statuses
    },

    setUsers(state, users) {
      state.users = users
    },

  },

  actions: {

  },

})

function rollDate() {
  const now = new Date()
  const today = date(now)
  store.commit('setDate', formatDate(today))
  const timeToMidnight = 86400000 - (now - today)
  console.log('timeToMidnight', timeToMidnight)
  window.setTimeout(rollDate, timeToMidnight)
}

rollDate()

export default store
