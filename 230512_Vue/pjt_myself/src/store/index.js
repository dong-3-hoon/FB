import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)
const apiKey = "d838f386c11255ef5f578f676243694f"
export default new Vuex.Store({
  state: {
    movies:[],
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, res){
      state.movies = res.data.results
    }
  },
  actions: {
    getMovies(context){
      axios({
        url: `https://api.themoviedb.org/3/movie/top_rated?api_key=${apiKey}&language=ko-KR&page=1`
      }).then((res)=>{
        console.log(res)
        context.commit("GET_MOVIES", res)
      }).catch((err)=>{
        console.log(err)
      })
    }
  },
  modules: {
  }
})
