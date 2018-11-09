import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    statuses: [],
    users: [],
  },

  mutations: {
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
