import Vue from 'vue'
import Vuex from 'vuex'

import { searchEvents } from '@/api'
import { date, formatDate } from '@/date'

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

    deleteEvent(state, event_id) {
      state.events = state.events.filter((e) => (e.event_id != event_id))
    },

    refreshEvents(state, events) {
      state.events = events
    }

  },

  actions: {

  },

})

// Initialize the date, and update at midnight.
function rollDate() {
  const now = new Date()
  const today = date(now)
  store.commit('setDate', formatDate(today))
  // Sleep until next midnight, then update the date again.
  const timeToMidnight = 86400000 - (now - today)
  window.setTimeout(rollDate, timeToMidnight)
}
rollDate()

// Load events, and reload periodically.
const LOAD_PERIOD = 180
function loadEvents() {
  console.log('loading events')
  searchEvents().then(events => { store.commit('refreshEvents', events) })
  window.setTimeout(loadEvents, LOAD_PERIOD * 1000)
}
loadEvents()

export default store
