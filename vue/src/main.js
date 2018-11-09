import Vue from 'vue'
import UIkit from 'uikit'
import Icons from 'uikit/dist/js/uikit-icons'

import App from '@/App.vue'
import router from '@/router'
import store from '@/store'
import { getStatuses, getUsers } from '@/api'

UIkit.use(Icons)
window.UIkit = UIkit

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),

  created() {
    console.log('created')

    // Load "constants" up front.
    getStatuses().then(statuses => { 
      this.$store.commit('setStatuses', statuses)
    })
    getUsers().then(users => {
      this.$store.commit('setUsers', users)
    })
  }
}).$mount('#app')

