import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import MovieListView from '../views/MovieListView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import ArticleView from '../views/ArticleView.vue'
import AccountView from '../views/AccountView.vue'
import CreateView from '../views/CreateView.vue'
import DetailView from '../views/DetailView.vue'
import UpdateView from '../views/UpdateView.vue'
import CloudView from '../views/CloudView.vue'
import ProfileView from '../views/ProfileView.vue'
import TestRecommendView from '../views/TestRecommendView.vue'

import RecommendView from '../views/RecommendView.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/movielist',
    name: 'movielist',
    component: MovieListView
  },
  {
    path: '/moviedetail/:id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/articles',
    name: 'articles',
    component: ArticleView
  },
 
  {
    path: '/accounts',
    name : 'accounts',
    component : AccountView
  },
  {
    path: '/create',
    name : 'create',
    component : CreateView
  },
  {
    path: '/detail/:id/',
    name : 'detail',
    component : DetailView
  },
  {
    path: '/update/:id',
    name : 'update',
    component : UpdateView
  },
  {
    path: '/cloud',
    name : 'cloud',
    component : CloudView
  },
  {
    path: '/testrecommend',
    name : 'testrecommend',
    component : TestRecommendView
  },
  {
    path: '/recommend',
    name : 'recommend',
    component : RecommendView
  },
  {
    path: '/profile/:username/:user_id',
    name : 'profile',
    props :true,
    component : ProfileView
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
