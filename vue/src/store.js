import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    statuses: [],
  },

  mutations: {
    setStatuses(state, statuses) {
      state.statuses = statuses
    },

  },

  actions: {

  },

})
