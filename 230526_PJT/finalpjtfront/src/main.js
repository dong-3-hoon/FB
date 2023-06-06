import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'animate.css'
import VueYoutube from "vue-youtube"
import axios from 'axios'

Vue.use(BootstrapVue)
Vue.config.productionTip = false
Vue.use(VueYoutube)
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

