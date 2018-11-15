import Vue from 'vue'
import Vuex from 'vuex'

import { searchEvents } from '@/api'
import { date } from '@/date'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    statuses: [],
    users: [],
    events: [],
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

    addEvent(state, event) {
      state.events.push(event)
    },

    refreshEvents(state, events) {
      state.events = events
    }

  },

  actions: {

  },

})

function rollDate() {
  const now = new Date()
  const today = date(now)
  // Sleep until next midnight, then update the date again.
  const timeToMidnight = 86400000 - (now - today)
  window.setTimeout(rollDate, timeToMidnight)
}

// Initialize the date.
rollDate()

// Load events from the back end.
searchEvents().then(events => { 
  store.commit('refreshEvents', events)
})

export default store
