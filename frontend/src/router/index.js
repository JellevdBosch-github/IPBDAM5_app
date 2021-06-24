import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import NotFound from '../views/NotFound.vue'
import Chart from '../views/Chart.vue'
import Trade from '../views/Trade.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/notfound',
    name: 'NotFound',
    component: NotFound
  },
  {
    path: '/trade',
    name: 'Trade',
    component: Trade
  },
  {
    path: '/trade/:id/:timestamp',
    name: 'Chart',
    component: Chart
  },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
  {
    path: '*',
    redirect: '/notfound',
    query: {
      code: 404,
      message: 'Page Not Found.'
    }
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
