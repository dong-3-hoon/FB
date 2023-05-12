import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import Genres from './modules/genres.js'

Vue.use(Vuex)
const apiKey = "d838f386c11255ef5f578f676243694f"

export default new Vuex.Store({
  state: {
    movies:[],
    watchMovieList:[],
    
  },
  getters: {
    
  },
  mutations: {
    GET_MOVIES(state, res) {
      state.movies = res.data.results
    },
    ADD_WATCH_MOVIE(state, watchMovie){
      state.watchMovieList.push(watchMovie)

    }
  },
  actions: {
    getMovies(context){ 
      axios({
        url: `https://api.themoviedb.org/3/movie/top_rated?api_key=${apiKey}&language=ko-KR&page=1`
      }).then((res)=>{
        console.log(res)
        context.commit("GET_MOVIES", res)
      }).catch((err) => {
        console.log(err)
      })
    },
    addWatchMovie(context, getMovie){
      const watchMovie = {title : getMovie, is_completed:false}
      context.commit('ADD_WATCH_MOVIE', watchMovie)
    },
    watched(context, movie){
      const newMovie = movie
      newMovie.is_completed = !newMovie.is_completed
      const newIdx  = context.state.watchMovieList.indexOf(newMovie)
      context.state.watchMovieList[newIdx] = newMovie
      console.log(context.state.watchMovieList[newIdx].is_completed)
    }

  },
  modules: {
    Genres,
  }
})
