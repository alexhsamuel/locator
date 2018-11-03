import Vue from 'vue'
import UIkit from 'uikit'
import Icons from 'uikit/dist/js/uikit-icons'

import App from './App.vue'
import router from './router'
import store from './store'

UIkit.use(Icons)
window.UIkit = UIkit

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),

  created() {
    console.log('created')
    fetch('/api/v1/statuses')
      .then((rsp) => rsp.json())
      .then((rsp) => { this.$store.commit('setStatuses', rsp.statuses) })
    fetch('/api/v1/users')
      .then((rsp) => rsp.json())
      .then((rsp) => { this.$store.commit('setUsers', rsp.users) })
  }
}).$mount('#app')

