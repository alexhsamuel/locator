import Vue from 'vue'
import Router from 'vue-router'
import Today from './views/Today.vue'
import Upcoming from './views/Upcoming.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Today
    },
    {
      path: '/upcoming',
      name: 'Upcoming',
      component: Upcoming,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
