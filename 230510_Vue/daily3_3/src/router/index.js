import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from "../views/Home.vue"
import Happeed from "../views/Happeed.vue"
import Notfound from "../views/Notfound.vue"
import Happling from "../views/Happling.vue"
import Happlossome from "../views/Happlossome.vue"
import Happlower from "../views/Happlower.vue"
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/happeed',
    name: 'happeed',
    component: Happeed
  },
  {
    path: '/404',
    name: 'Notfound',
    component: Notfound
  },
  {
    path: '/happling',
    name: 'happling',
    component: Happling
  },
  {
    path: '/happlossome',
    name: 'happlossome',
    component: Happlossome
  },
  {
    path: '/happlower',
    name: 'happlower',
    component: Happlower
  },
  {
    path: '*',
    redirect: '/404'
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
