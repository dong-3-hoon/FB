import Vue from 'vue'
import VueRouter from 'vue-router'
import AllTodoPage from '../views/AllTodoPage.vue'
import ImportantTodoPage from '../views/ImportantTodoPage.vue'
import TodayTodoPage from '../views/TodayTodoPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path:'/',
    name: 'alltodopage',
    component: AllTodoPage
  },
  {
    path:'/importanttodopage',
    name: 'importanttodopage',
    component: ImportantTodoPage
  },
  {
    path:'/todaytodopage',
    name: 'todaytodopage',
    component: TodayTodoPage
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
